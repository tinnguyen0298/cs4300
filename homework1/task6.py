def count_words(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
        return len(text.split())  # Count words by splitting on whitespace
    except FileNotFoundError:
        return -1  # Return -1 if the file is not found


# Metaprogramming: Dynamically generate test function names
test_cases = {
    "task6_read_me.txt": 127, # expected word count associated with task6_read_me.txt
}

def generate_test_function(filename, expected_count): # dynamically generates a test function.
    def test_func():
        assert count_words(filename) == expected_count
    return test_func

# dynamically create test cases
for filename, expected in test_cases.items():
    test_name = f"test_word_count_{filename.replace('.', '_')}"
    globals()[test_name] = generate_test_function(filename, expected)

# test file not found case
def test_file_not_found():
    assert count_words("non_existent_file.txt") == -1
