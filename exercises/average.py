# Store scores in a list
# Calculate: total, average, highest score, lowest score

scores = [89, 77, 90, 54, 61, 74, 32, 83, 50, 79, 73]

print(f"Scores: {scores}")
print(f"Total: {sum(scores)}")
print(f"Average: {(sum(scores)/len(scores)):.2f}")
print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")
