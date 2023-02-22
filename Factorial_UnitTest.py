import unittest

class Test_Factorial(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(fact(10),3628800)
    def testcase_2(self):
        self.assertEqual(fact(5),120)

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)

if __name__=="__main__":
    unittest.main()
