# run.py

from utils.exceptions import handle_exception, WorkflowExecutionError

def main():
    try:
        5/0
        
    except Exception as e:
        handle_exception(e, context="run.py > main()")

if __name__ == "__main__":
    main()
