students = [("Ravi", 82), ("Anu", 91), ("Kabir", 75)]

by_score = sorted(students, key=lambda s: s[1], reverse=True)

print(by_score)

