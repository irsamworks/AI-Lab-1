# Lab 1: Conversational Test vs Reliable Task Performance

def conversational_response(score, documents_complete):
    if score >= 70 and documents_complete:
        return (
            "You appear eligible because your score is at least 70 "
            "and your documents are complete."
        )
    else:
        return (
            "You do not meet the score and document conditions "
            "for this lab example."
        )


def rule_based_decision(score, documents_complete):
    if score >= 70 and documents_complete:
        return "PASS"
    else:
        return "FAIL"


# Scholarship example
score = 75
documents_complete = True

print("SCHOLARSHIP CASE")
print("Score:", score)
print("Documents complete:", documents_complete)

print("\nConversational response:")
print(conversational_response(score, documents_complete))

print("\nRule-based result:")
print(rule_based_decision(score, documents_complete))


# Example of incorrect reasoning
print("\nINCORRECT REASONING EXAMPLE")
score = 69

print("Score:", score)
print("Incorrect claim: The applicant passes because 69 is at least 70.")
print("Correct rule-based result:",
      rule_based_decision(score, True))