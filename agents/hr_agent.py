# Hr agent.py
from utils.logger import logger
from utils.exceptions import handle_exception, FileOperationError

import os

class HrAgent:
    def __init__(self):
        self.name = "HR Agent"

    def parse_resume(self, file_path: str) -> dict:
        try:
            if not os.path.exists(file_path):
                raise FileOperationError(f"resume file not found {file_path}")
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            
            logger.info("Resume Parsed")
            return self.extract_info(text)

        except Exception as e:
            handle_exception(e, context="HR Agent> parse_resume")
        

    def extract_info(self, text) -> dict:
        lower_text = text.lower()

        skills = []
        for skill in ['python', 'sql', 'excel', 'power bi', 'machine learning']:
            if skill in lower_text:
                skills.append(skill)

        experience = "fresher"
        if "years" in lower_text or "experience" in lower_text:
            experience = "experienced"

        return {
            "summary": "Candidate with skills: " + ', '.join(skills),
            "skills": skills,
            "experience": experience,
            "score": len(skills) * 20,
            "interview": "Yes" if len(skills) >= 3 else "No"
        }

