# run.py
from agents.coordinator_agent import CoordinatorAgent
import os
def main():
    coordinator = CoordinatorAgent()
    file_path = os.path.join("data", "resumes", "sample.txt")

    task = {
        "task_type" : "screen_resume",
        "payload": {
            "file_path" : file_path,

        }
    }

    result = coordinator.dispatch(task['task_type'], task["payload"])
    print("\n📄 Task Result:")

    if result:
        for k, v in result.items():
            print(f"{k.capitalize()}: {v}")

if __name__ == "__main__":
    main()
