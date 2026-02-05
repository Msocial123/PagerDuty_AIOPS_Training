def score_accuracy(summary):
    keywords = ["CPU", "database", "payment", "timeout"]
    score = sum(1 for k in keywords if k.lower() in summary.lower())
    return min(score / len(keywords), 1.0)

def score_readability(summary):
    sentences = summary.split(".")
    avg_length = sum(len(s.split()) for s in sentences) / max(len(sentences),1)
    return 1.0 if avg_length < 25 else 0.6

def score_groundedness(summary):
    hallucination_terms = ["memory leak", "network outage"]
    for term in hallucination_terms:
        if term in summary.lower():
            return 0.0
    return 1.0
