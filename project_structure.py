import os

# Define the folder structure
project_structure = [
        "agents/hr_agent.py",
        "agents/finance_agent.py",
        "agents/sales_agent.py",
        "agents/support_agent.py",
        "agents/pmo_agent.py",
        "agents/coordinator_agent.py",
        
        "workflows/main_workflow.py",
        
        "tools/pdf_parser.py",
        "tools/google_calendar.py",
        "tools/slack_notifier.py",
        "tools/notion_tasks.py",
        
        "data/resumes/.keep",
        "data/transactions/.keep",
        
        "memory/memory_store.py",
        
        "configs/settings.yaml",
        
        "logs/autoops.log",
        
        "frontend/dashboard.py",
        
        "utils/logger.py",
        "utils/prompts.py",
        
        "tests/test_hr_agent.py",
        
        ".env",
        ".gitignore",
        "README.md",
        "requirements.txt",
        "run.py"
    ]


# Create folders and files
def create_structure(structure):
    
    for file_path in structure:
        full_path = os.path.join(file_path)
        folder = os.path.dirname(full_path)
        os.makedirs(folder, exist_ok=True)
        with open(full_path, 'w') as f:
            if file_path.endswith(".gitignore"):
                f.write("__pycache__/\n.env\nlogs/\n*.pyc\nvenv/\n")
            elif file_path.endswith("requirements.txt"):
                f.write("openai\nlangchain\nlanggraph\ncrewai\npydantic\npandas\npython-dotenv\ntqdm\nstreamlit\nnotion-client\nslack-sdk\ngoogle-api-python-client\n")
            elif file_path.endswith("README.md"):
                f.write("# AutoOps - Agentic AI System\n\nA multi-agent AI automation system for enterprise ops.\n")
            elif file_path.endswith(".env"):
                f.write("# Add your API keys here\nOPENAI_API_KEY=\n")
            elif file_path.endswith(".keep"):
                pass  # Just to keep empty dirs
            else:
                f.write(f"# {file_path.split('/')[-1].replace('_', ' ').capitalize()}")

    print(f"\n✅ Project structure created")

# Run it
if __name__ == "__main__":
    create_structure(project_structure)

