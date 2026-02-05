alert = {
    "alert_name": "HighCPUUsage",
    "severity": "critical",
    "service": "payment-service",
    "timestamp": "2026-02-05 10:00 UTC",
    "description": "CPU usage exceeded 90% for 5 minutes"
}

logs = """
2026-02-05 09:58:12 ERROR PaymentProcessor Timeout while calling DB
2026-02-05 09:58:45 WARN Connection pool exhausted
2026-02-05 09:59:10 ERROR Failed to process transaction
"""

slack_messages = """
10:01 DevOps: Seeing high CPU on payment pods
10:03 Backend: DB queries are slow
10:05 SRE: Scaling replicas now
"""

ticket = {
    "ticket_id": "INC-1023",
    "summary": "Payment failures reported by customers",
    "impact": "Checkout failures for 30% users",
    "status": "Investigating"
}
