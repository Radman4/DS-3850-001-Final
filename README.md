# DS-3850-001-Final
This is my Final Project for DS-3850-001. it is an AI-Powered News Newsletter Generator

Quarterly Assessment 4:
AI-Powered News Newsletter
Project Overview
The goal of this project is to create an AI-Powered News Newsletter
Generator that automates the process of keeping users informed about the
latest news.
Problem Statement
Staying up-to-date with the latest news on specific topics can be time-
consuming. You want a system that: 1) fetches the latest news by retrieving
articles on topics of interest from reliable sources, 2) summarizes the main
points with an LLM to condense the lengthy article into a concise email-
friendly summary, and 3) deliver the information via email to recipients.
Since this email should be “automated,” you can do this by scheduling a
script to run daily using a task scheduler (e.g., cron on macOS/Linux or Task
Scheduler on Windows). It should run your python file.
Implementation Tips
Search for an Existing GitHub Repository
 Start by exploring GitHub for similar projects that automate
newsletters. Some useful repositories might include:
o https://github.com/aws-samples/generative-ai-newsletter-app.git
o https://github.com/samestrin/llm-newsletter-generator.git
o https://github.com/tychurch74/AI_newsletter.git
o https://github.com/jahwi/ai_newsie.git
 Look for repositories that:
o Fetch news from an API.
o Integrate with an AI LLM model for summarization.
o Use an email API to send newsletters.
o Tip: have AI help you decide if a repo is what you’re looking for
Break It Down
One of the biggest issues we’ve been having is by not knowing exactly where
the errors are coming from in our code. Break it down one step at a time.
Here’s how you can approach the project in smaller parts:
1. Fetch the Articles:
o Use Python’s requests library to query the news API.
o Test by printing the headlines and article links.
2. Summarize the Articles:
o Use an LLM (e.g., OpenAI API) to summarize one article.
o Iterate for multiple articles, generating summaries for each.
o Test by printing the summary
3. Send an Email:
o Create a test email using Python’s smtplib or a service like
SendGrid.
o Format the email with a clear structure (e.g., bulleted list of
summaries) ensuring it looks clean and neat.
Deliverable
The final deliverable for this project is a 5-8-minute-long demonstration of
your AI-Powered News Newsletter application. This demonstration should
showcase your work, explain the steps involved in the project, and prove that
your application functions as intended.
Presentation Format
You can choose how to present your demonstration:
1. In-Person Meeting: Schedule a live, in-person presentation with me
where you run the application and explain it to me directly.
2. Pre-Recorded Video: Submit a video recording of your demonstration,
approximately 5-8 minutes long, showing how your application works.
Requirements for the Demonstration
Your demonstration must include the following:
1. Overview of the Application Workflow:
o Clearly explain each of the three core steps in your application:
1. Fetching Data: Show how your application retrieves articles
from a news API.
2. Summarizing Data: Demonstrate how an LLM summarizes
the articles into concise content.
3. Email Formatting and Sending: Show how your application
formats the summaries into an email and sends it. The
email should be well-formatted, appearing clean, neat, and
professional.
2. Live Example of the Application in Action:
o Run the application and demonstrate the entire process, from
fetching the news to receiving the email.
o Open your inbox to show that the email was sent and verify its
content matches the expected output.
Partial Credit for Incomplete Projects
If you encounter issues and cannot finish the application by the deadline, you
can still earn partial credit by:
 Clearly explaining the error(s) you encountered.
 Demonstrating your application up to the point where the error occurs.
 Showing your debugging efforts, such as attempts to resolve the
problem (e.g., code changes, research, testing).
Be prepared to discuss:
 What is causing the error.
 Steps you’ve taken to fix it.
 What you would do next with more time.