def check_number(value):
    if value > 0:
        return "Positive"
    elif value < 0:
        return "Negative"
    else:
        return "Zero"
    
def prime_numbers(): # get the first 10 prime numbers
    primes = []
    num = 2
    while len(primes) < 10: # calculate until get the first 10 prime numbers
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

def sum():
    total = 0
    num = 1
    while num <= 100:
        total += num 
        num += 1
    return total

class TestCases():
    def test_check_number(self):
        assert check_number(10) == "Positive"
        assert check_number(-2) == "Negative"
        assert check_number(0) == "Zero"

    def test_prime_numbers(self):
        assert prime_numbers() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
    def test_sum(self):
        assert sum() == 5050