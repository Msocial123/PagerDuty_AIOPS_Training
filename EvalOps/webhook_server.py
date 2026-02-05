from flask import Flask, request, jsonify
import subprocess
from prompt_builder import build_prompt
from evalops import score_accuracy, score_readability, score_groundedness

app = Flask(__name__)

# -----------------------------
# Local LLM execution (Ollama)
# -----------------------------
def run_local_llm(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout


# -------------------------------------------------
# PagerDuty Webhook Endpoint (V3 Generic Webhook)
# -------------------------------------------------
@app.route("/pagerduty/webhook", methods=["POST"])
def pagerduty_webhook():
    payload = request.json

    # 🔍 DEBUG LOGGING (VERY IMPORTANT)
    print("===== RECEIVED PAGERDUTY PAYLOAD =====")
    print(payload)

    # ✅ Correct PagerDuty V3 payload path
    incident = payload["event"]["data"]["incident"]

    # Build alert object
    alert = {
        "alert_name": incident["title"],
        "severity": incident["severity"],
        "service": incident["service"]["summary"],
        "description": incident.get("description") or incident["title"]
    }

    # Placeholders (can be replaced later with real sources)
    logs = "Logs not available yet (placeholder)"
    slack = "Slack messages not available yet (placeholder)"

    ticket = {
        "ticket_id": incident["id"],
        "impact": incident.get("impact", "unknown"),
        "status": incident["status"]
    }

    # Build GenAI prompt
    prompt = build_prompt(alert, logs, slack, ticket)

    # Generate summary
    summary = run_local_llm(prompt)

    # EvalOps scoring
    accuracy = score_accuracy(summary)
    readability = score_readability(summary)
    groundedness = score_groundedness(summary)

    # Return response (PagerDuty ignores body, but useful for debugging)
    return jsonify({
        "incident_id": incident["id"],
        "summary": summary,
        "evalops": {
            "accuracy": accuracy,
            "readability": readability,
            "groundedness": groundedness
        }
    })


# -----------------------------
# App Runner
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
