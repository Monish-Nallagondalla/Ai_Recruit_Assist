"""Candidate screening logic"""
from pydantic import BaseModel, Field
from typing import List
from src.Ai_Recruit_Assist.utils.groq_client import GroqClient

class ScreeningResult(BaseModel):
    name: str = Field(description="The name of the candidate")
    email: str = Field(description="The email of the candidate")
    score: float = Field(description="The score of the candidate from 0 to 10")
    feedback: str = Field(description="The feedback for the candidate")

class CandidateScreening:
    def __init__(self, groq_client: GroqClient):
        """Initialize screening component"""
        self.groq_client = groq_client
        self.instructions = [
            "You are an expert HR agent that screens candidates for a job interview.",
            "You are given a candidate's name, email, resume, and job description.",
            "You need to screen the candidate and determine if they are a good fit for the job.",
            "You must provide a score for the candidate from 0 to 10.",
            "You must provide feedback explaining why the candidate is a good fit or not.",
            "Return your response as a valid JSON object with the following fields: name (string), email (string), score (float), feedback (string).",
            "The 'name' field must exactly match the provided candidate name (e.g., if the name is 'Moni', use 'Moni').",
            "The 'email' field must exactly match the provided candidate email (e.g., if the email is 'nsmonish@gmail.com', use 'nsmonish@gmail.com'). It must be a valid email address.",
            "Do not modify or generate a different email address. Use the exact email provided.",
            "Example response: {\"name\": \"John Doe\", \"email\": \"john.doe@example.com\", \"score\": 8.5, \"feedback\": \"Strong Python skills, relevant experience.\"}",
            "Ensure the response is valid JSON, enclosed in curly braces, and contains only the specified fields.",
            "Do not include any additional text, code blocks, or unrelated content (e.g., phrases like 'king and queen') outside or inside the JSON object."
        ]

    def screen(self, name: str, email: str, resume_content: str, job_description: str) -> ScreeningResult:
        """Screen a candidate based on resume and job description"""
        prompt = "\n".join(self.instructions) + f"\nCandidate name: {name}\nCandidate email: {email}\nCandidate resume: {resume_content}\nJob description: {job_description}"
        return self.groq_client.run(prompt, ScreeningResult, email)