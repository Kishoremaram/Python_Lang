import unittest

class Test_withdrawal(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(withdraw(5000),"Transaction successful")
    def testcase_2(self):
        self.assertEqual(withdraw(2200),"Enter multiples of 500 & 2000")

def withdraw(a):
    #a=int(input("Enter withdrawal amount:"))
    if a%2000==0 or a%500==0:
        print("Transaction successful")
        return "Transaction successful"
    else:
        print("Enter multiples of 500 & 2000")
        return "Enter multiples of 500 & 2000"
    
if __name__=="__main__":
    unittest.main()
