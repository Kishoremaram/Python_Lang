import unittest

class Test_Prime(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(prime(11),"True")
    def testcase_2(self):
        self.assertEqual(prime(30),"False")

def prime(n):
    for i in range(2,n):
        if n%i==0:
            print(n,"is not prime")
            return "False"
            break
    else:
        print(n,"is prime")
    return "True"
        
if __name__=="__main__":
    unittest.main()
