def calculate_discount(price, discount):
    return price * (1 - discount / 100)

class TestCases():
    def test_integer_values(self):
        assert calculate_discount(60, 10) == 54
        assert calculate_discount(100, 50) == 50
        assert calculate_discount(50, 0) == 50  # No discount

    def test_float_values(self):
        assert round(calculate_discount(99.99, 10), 4) == 89.9910
        assert round(calculate_discount(150.5, 20.5), 4) == 119.6475
        assert round(calculate_discount(75.75, 0), 4) == 75.7500  # No discount