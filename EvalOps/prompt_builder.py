def build_prompt(alert, logs, slack, ticket):
    prompt = f"""
You are an SRE assistant.

Alert:
- Name: {alert['alert_name']}
- Severity: {alert['severity']}
- Service: {alert['service']}
- Description: {alert['description']}

Logs:
{logs}

Slack Conversation:
{slack}

Ticket Summary:
- ID: {ticket['ticket_id']}
- Impact: {ticket['impact']}
- Status: {ticket['status']}

Task:
Generate a concise incident summary including:
1. What happened
2. Probable root cause
3. Actions taken
4. Current status
"""
    return prompt
