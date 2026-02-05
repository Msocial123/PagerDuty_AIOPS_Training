from summarizer import summary
from evalops import score_accuracy, score_readability, score_groundedness

accuracy = score_accuracy(summary)
readability = score_readability(summary)
groundedness = score_groundedness(summary)

final_score = round((accuracy + readability + groundedness) / 3, 2)

print("\n=== EVALOPS RESULTS ===")
print(f"Accuracy: {accuracy}")
print(f"Readability: {readability}")
print(f"Groundedness: {groundedness}")
print(f"Final Score: {final_score}")
