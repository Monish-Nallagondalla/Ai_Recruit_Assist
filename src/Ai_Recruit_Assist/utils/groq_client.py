"""Groq API client for LLM interactions"""
from groq import Groq
from pydantic import BaseModel
from typing import Type, Any
import re
import json

class GroqClient:
    def __init__(self, api_key: str):
        """Initialize Groq client"""
        self.client = Groq(api_key=api_key)

    def run(self, prompt: str, response_model: Type[BaseModel], email: str = None) -> Any:
        """Run Groq API with prompt and parse response to model"""
        try:
            response = self.client.chat.completions.create(
                model="llama3-8b-8192",  # Switched to a smaller, potentially more reliable model
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,  # Reduced to avoid rate limits
            )
            content = response.choices[0].message.content
            print(f"Raw Groq response: {content}")  # Debug log

            # Extract JSON from code block if present
            json_match = re.search(r'```json\n(.*?)\n```', content, re.DOTALL)
            if json_match:
                content = json_match.group(1)
            else:
                # Try to find JSON object directly
                json_match = re.search(r'\{[^{}]*\}', content, re.DOTALL)
                if json_match:
                    content = json_match.group(0)
                else:
                    raise ValueError("No valid JSON object found in response")

            # Parse JSON and apply email fallback if provided
            parsed_json = json.loads(content)
            if email and isinstance(parsed_json, dict) and "email" in parsed_json:
                parsed_json["email"] = email  # Override email field with input email

            # Convert back to JSON string for Pydantic validation
            content = json.dumps(parsed_json)
            return response_model.model_validate_json(content)
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON response: {content}\nError: {str(e)}")
            raise ValueError("Invalid JSON response from Groq API")
        except Exception as e:
            print(f"Error processing Groq response: {str(e)}")
            raise