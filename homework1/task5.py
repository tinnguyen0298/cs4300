favorite_books = [
    ("The Intelligent Investor", "Benjamin Graham"),
    ("Wonder", "R.J. Palacio"),
    ("1984", "George Orwell"),
    ("Inner Excellence", "Jim Murphy"),
    ("The Great Gatsby", "F. Scott Fitzgerald")
]

# Print the first three books
first_three_books = favorite_books[:3]
print("First three books:", first_three_books)

# Dictionary representing a student database (Name -> Student ID)
student_database = {
    "Alice Johanson": 111,
    "Wilson Smith": 112,
    "Anna Brown": 113
}

# Function to retrieve student ID by name
def get_student_id(name):
    return student_database.get(name, "Student not found")


class TestCases:
    def test_favorite_books(self):
        assert isinstance(favorite_books, list)
        assert len(favorite_books) >= 3  # Ensure it is the first 3 books

    def test_list_slicing(self):
        expected_books = [
            ("The Intelligent Investor", "Benjamin Graham"),
            ("Wonder", "R.J. Palacio"),
            ("1984", "George Orwell")
        ]
        assert first_three_books == expected_books  # Ensure first 3 books match

    def test_student_database_dict(self):
        assert isinstance(student_database, dict)
        assert student_database["Alice Johanson"] == 111
        assert student_database["Wilson Smith"] == 112
        assert student_database["Anna Brown"] == 113

    def test_get_student_id(self):
        assert get_student_id("Alice Johanson") == 111
        assert get_student_id("Wilson Smith") == 112
        assert get_student_id("Unknown") == "Student not found"  # Test missing student