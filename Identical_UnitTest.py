import unittest

class Test_Factorial(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(identical(), "lists are equal")

def identical():
    list1=[1,2,3,2,1]
    list2=[1,3,2,2,1]
    list1.sort()
    list2.sort()
    if list1 == list2:
        print("lists are equal")
        return "lists are equal"
    else:
        print("list are not equal")
        return "lists are not equal"

if __name__=="__main__":
    unittest.main()
