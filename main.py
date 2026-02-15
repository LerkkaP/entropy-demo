from math import log2

def read_file(file_name):
    with open(file_name, "r") as f:
        return f.read()
    
def compute_char_counts(file_content):
    char_counts = {}
    for char in file_content:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts

def char_probabilities(char_counts):
    N = sum(char_counts.values())
    char_probabilities = {}
    for key, value in char_counts.items():
        char_probability = value / N
        char_probabilities[key] = char_probability
    return char_probabilities

def char_informations(char_probabilities):
    informations = {key: log2(1/value) for key, value in char_probabilities.items()}
    return informations

def entropy(informations, probabilities):
    total_entropy = 0
    for key in probabilities:
        total_entropy += probabilities[key] * informations[key]
    return total_entropy

file_content = read_file("sample.txt")
char_counts = compute_char_counts(file_content)
probabilities = char_probabilities(char_counts)
informations = char_informations(probabilities)
total_entropy = entropy(informations, probabilities)
print(f"Entropy: {total_entropy}")