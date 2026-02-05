import subprocess
from incident_data import alert, logs, slack_messages, ticket
from prompt_builder import build_prompt

prompt = build_prompt(alert, logs, slack_messages, ticket)

def run_local_llm(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout

summary = run_local_llm(prompt)

print("\n=== INCIDENT SUMMARY ===\n")
print(summary)
