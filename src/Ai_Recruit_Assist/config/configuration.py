"""Configuration management for Ai_Recruit_Assist"""
import yaml
from pathlib import Path
from typing import Dict, Any

class Config:
    def __init__(self, config_path: str = "config/config.yaml"):
        """Initialize configuration from YAML file"""
        self.config_path = Path(config_path)
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        with open(self.config_path, 'r') as file:
            return yaml.safe_load(file)

    @property
    def groq_api_key(self) -> str:
        """Get Groq API key"""
        return self.config['groq']['api_key']

    @property
    def timezone(self) -> str:
        """Get timezone"""
        return self.config['app']['timezone']

    @property
    def interview_hours(self) -> Dict[str, int]:
        """Get interview hours"""
        return self.config['app']['interview_hours']

    @property
    def from_email(self) -> str:
        """Get sender email"""
        return self.config['email']['from_email']