#!/usr/bin/env python
import sys
from ticket_classification_and_response_automation.crew import TicketClassificationAndResponseAutomationCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs1 = {
        'subject': 'Getting deployment errors while deploying crewai',
        'content': """Hello, I am getting deployment errors while trying to deploycrews "Deployment error: CodeBuild failed: PLA......." Can you please help? Thanks Satya""",
        'ticket_id': '17218122917'
    }

    inputs2 = {
        'subject': 'Cancel my subscription please',
        'content': """Hello, I've been in the community pages and the chat box for nearly two
weeks now with multiple bugs and issues that are being resolved or
addressed.

Thank you,
Alex Christian""",
        'ticket_id': '16680689177'
    }

    TicketClassificationAndResponseAutomationCrew().crew().kickoff(inputs=inputs1)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'subject': 'sample_value',
        'content': 'sample_value'
    }
    try:
        TicketClassificationAndResponseAutomationCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TicketClassificationAndResponseAutomationCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'subject': 'sample_value',
        'content': 'sample_value'
    }
    try:
        TicketClassificationAndResponseAutomationCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
