"""Email writing and sending logic"""
from pydantic import BaseModel, Field
from ..utils.groq_client import GroqClient
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

class Email(BaseModel):
    subject: str = Field(description="The subject of the email")
    body: str = Field(description="The body of the email")

class EmailHandler:
    def __init__(self, groq_client: GroqClient, from_email: str):
        """Initialize email handler"""
        self.groq_client = groq_client
        self.from_email = from_email
        self.instructions = [
            "You are an expert email writer agent that writes emails to selected candidates.",
            "You need to write an email that is concise, friendly, and professional.",
            "Include the call time, URL, and congratulate the candidate.",
            "Return your response as a valid JSON object with the following fields: subject (string), body (string).",
            "Example response: {\"subject\": \"Interview Invitation\", \"body\": \"Dear John, Congratulations on advancing to the interview stage! Your interview is scheduled for 2025-05-10 at 10:00 AM via Zoom: https://zoom.us/j/123. Best regards, HR Team\"}",
            "Ensure the response is valid JSON, enclosed in curly braces, and contains only the specified fields.",
            "Do not include any additional text or code blocks outside the JSON object."
        ]

    def write_email(self, candidate_name: str, candidate_email: str, call_time: str, call_url: str) -> Email:
        """Write an email for a scheduled interview"""
        prompt = "\n".join(self.instructions) + f"\nCandidate name: {candidate_name}\nCandidate email: {candidate_email}\nCall time: {call_time}\nCall URL: {call_url}"
        return self.groq_client.run(prompt, Email)

    def send_email(self, to_email: str, subject: str, body: str):
        """Send email (mock implementation due to no free email API)"""
        # In a real scenario, use a free email API or SMTP server
        print(f"Mock sending email to {to_email}\nSubject: {subject}\nBody: {body}")