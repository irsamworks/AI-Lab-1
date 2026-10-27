# Lab 1: Rule-Based Scholarship Eligibility System

# All eligibility thresholds are synthetic lab assumptions.
def check_eligibility(score, documents_complete,
                      minimum_age_met, essay_submitted):

    score_condition = score >= 70
    documents_condition = documents_complete
    age_condition = minimum_age_met
    essay_condition = essay_submitted

    if not score_condition:
        return "FAIL", "Score is below 70."

    if not documents_condition:
        return "FAIL", "Required documents are incomplete."

    if not age_condition:
        return "FAIL", "Minimum age requirement is not met."

    if not essay_condition:
        return "FAIL", "Required essay has not been submitted."

    return "PASS", "All four conditions are satisfied."

# Exactly four core test cases.

test_cases = [
{
"name": "Test 1 - Successful application",
"input": {
"score": 85,
"documents_complete": True,
"minimum_age_met": True,
"essay_submitted": True
},
"expected": "PASS"
},
{
"name": "Test 2 - Age condition fails",
"input": {
"score": 85,
"documents_complete": True,
"minimum_age_met": False,
"essay_submitted": True
},
"expected": "FAIL"
},
{
"name": "Test 3 - Essay condition fails",
"input": {
"score": 85,
"documents_complete": True,
"minimum_age_met": True,
"essay_submitted": False
},
"expected": "FAIL"
},
{
"name": "Test 4 - Score threshold boundary",
"input": {
"score": 70,
"documents_complete": True,
"minimum_age_met": True,
"essay_submitted": True
},
"expected": "PASS"
}
]

# Execute and display the four tests.

for test in test_cases:
  actual, reason = check_eligibility(**test["input"])

print("=" * 55)
print("Test:", test["name"])
print("Input:", test["input"])
print("Expected result:", test["expected"])
print("Actual result:", actual)
print("Reason:", reason)

if actual == test["expected"]:
    print("Test status: CORRECT")
else:
    print("Test status: INCORRECT")

print("=" * 55)
