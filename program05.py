import csv
num_attribute = 6
a = []
with open('program06.csv', 'r') as file:
    reader = csv.reader(file)
    a = list(reader)

hypothesis = a[1][:-1]  # Use the first positive example for initialization

print(f"Initial Hypothesis: {hypothesis}\n")

for i in a:
    if i[-1] == 'yes':
        for j in range(num_attribute):
            if i[j] != hypothesis[j]:
                hypothesis[j] = '?'

print("\nThe Maximally Specific Hypothesis for a given Training Examples :\n")
print(hypothesis)

