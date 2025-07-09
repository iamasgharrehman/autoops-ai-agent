# agents/coordinator_agent.py

from agents.hr_agent import HrAgent
from utils.logger import logger
from utils.exceptions import handle_exception

class CoordinatorAgent:
    def __init__(self):
        self.hr_agent = HrAgent()
        self.available_agents = {
            "hr": self.hr_agent,
            # Add more agents like "finance", "support" later
        }

    def dispatch(self, task_type: str, payload: dict) -> dict:
        try:
            logger.info(f"Received task: {task_type}")

            if task_type == "screen_resume":
                file_path = payload.get("file_path") if payload else None
                if not file_path:
                    logger.error("Missing 'file_path' in payload.")
                    return {"error": "Missing 'file_path' in payload."}

                logger.info("Dispatching to HR Agent for resume screening.")
                return self.hr_agent.parse_resume(file_path)

            # You can add routing for other task types here
            else:
                logger.warning(f"Unknown task type: {task_type}")
                return {"error": "Unknown task type"}

        except Exception as e:
            handle_exception(e, context="CoordinatorAgent > dispatch")
            return {"error": str(e)}
