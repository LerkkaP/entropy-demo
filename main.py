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

file_content = read_file("sample.txt")
char_counts = compute_char_counts(file_content)