answer_key = "ABCDA"
student_answers = "AB-DA"

correct = 0
incorrect = 0
unanswered = 0

for i in range(len(answer_key)):
    ans = student_answers[i]

    if ans == '-':
        unanswered += 1
    elif ans == answer_key[i]:
        correct += 1
    else:
        incorrect += 1

final_score = (correct * 1.0) - (incorrect * 0.25)

print("--- Examination Result Summary ---")
print(f"Correct Answers:   {correct}")
print(f"Incorrect Answers: {incorrect}")
print(f"Unanswered:        {unanswered}")
print(f"Final Score:       {final_score:.2f}")