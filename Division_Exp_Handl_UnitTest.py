import unittest

class Test_Division(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(Division())
    def testcase_2(self):
        self.assertEqual(Division())

def Division(x,y):
    
    try:
        x=int(input("Enter First Number:"))
        y=int(input("Enter Second Number:"))
        print(x/y)
    except ZeroDivisionError:
        print("can't divide with zero")
        return "can't divide with zero"
    except ValueError:
        print("please provide int value only")
        return "please provide int value only"
    
if __name__=="__main__":
    unittest.main()
