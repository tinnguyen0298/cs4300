# declares variables
a = 10 #int
b = 20.5 #float
c = 'string' #string
d = True #boolean

class TestCases(): # test class to test each data type
    def test_int(self):
        assert isinstance(a, int) == True

    def test_float(self):
        assert isinstance(b, float) == True

    def test_string(self):
        assert isinstance(c, str) == True

    def test_boolean(self):
        assert isinstance(d, bool) == True
