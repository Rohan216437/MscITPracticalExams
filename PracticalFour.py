# Practical 4: FIND-S Algorithm
# Aim: Implement the FIND-S algorithm to find the most specific
# hypothesis based on the given training data.

# Create dataset
data = [
    ["Sunny", "Warm", "Weak", "Yes"],
    ["Sunny", "Warm", "Strong", "Yes"],
    ["Rainy", "Cold", "Strong", "No"],
    ["Sunny", "Cold", "Weak", "Yes"],
    ["Cloudy", "Warm", "Weak", "No"]
]

# Initial hypothesis
hypothesis = ["null", "null", "null"]

print("Initial Hypothesis:", hypothesis)

# Apply FIND-S algorithm
for row in data:

    # Consider only positive examples
    if row[3] == "Yes":

        # Initialize hypothesis with the first positive example
        if hypothesis == ["null", "null", "null"]:
            hypothesis[0] = row[0]
            hypothesis[1] = row[1]
            hypothesis[2] = row[2]

        else:
            # Generalize attributes when they do not match
            for i in range(3):
                if hypothesis[i] != row[i]:
                    hypothesis[i] = "?"

        print("Updated Hypothesis:", hypothesis)

# Display final hypothesis
print("\nFinal Most Specific Hypothesis:")
print(hypothesis)