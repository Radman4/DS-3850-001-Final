import openai
import requests
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
#smtplib does not like useing .env files to get the required info.
emailUser = "Insert Host Email Here"
emailPassword = "Insert Password Here"
print("sending email...")
emailRecipient = "insert Recipitent here"
#.env loads to get API keys.
load_dotenv()
apiKey = os.getenv("key")
newsKey = os.getenv("news")
#setup openai
openai.api_key = apiKey
#setup the reqests library
url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={newsKey}'
response = requests.get(url)
# getting newes articles ( changed the articles variable so it only shows about 5 articles.)
if response.status_code == 200:
    news_data = response.json()
    articles = news_data.get('articles', [])
    articles = articles[:5]
    summaries = []
    for article in articles:
# openai will pull form these and summarize the articles. then it will send it to a email client
        aiTitle = article.get('title', 'No Title')
        aiDescription = article.get('description', 'No Description')
        aiContent = f"Title: {aiTitle}\n Description: {aiDescription}"
        #openai summary. 
        aiResponse = openai.responses.create(
            model="gpt-4.1",  
            input=[
                {"role": "system", "content": "you are a simple news aggregator, whose sole function is to write a summary of the following articles.:"},
                {"role": "user", "content": aiContent},])

        summary = aiResponse.output_text
        summaries.append(f"Summary for '{aiTitle}':\n{summary}\n")
#collecting the ai summaries and putting them in the body
    emailBody = "<h2>Your Daily Summaries</h2><ul>"
    for summary in summaries:
        emailBody += f"<li>{summary}</li>"
    emailBody += "</ul>"


#this is the data that the email client will use to send
    msg = MIMEMultipart()
    msg['From'] = emailUser
    msg['To'] = emailRecipient
    msg['Subject'] = "Daily AI-Powered News Summaries"
    msg.attach(MIMEText(emailBody, 'html'))
#email client atempts send.
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(emailUser, emailPassword)
            server.sendmail(emailUser, emailRecipient, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
else:
    print(f"Failed to fetch news: {response.status_code}")