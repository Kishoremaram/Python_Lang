import unittest

class Test_Palin(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(palindrome("malayalam"),True)
    def testcase_2(self):
        self.assertEqual(palindrome("malay"),False)
    def testcase_3(self):
        self.assertEqual(palindrome("19891"),True)
    def testcase_4(self):
        self.assertEqual(palindrome("kishore"),False)

def palindrome(str1):
    rev=""  
    for i in str1:
        rev=i+rev
    if str1==rev:
        print("This is palidrome")
        return True
    else:
        print("This is not palindrome")
        return False

if __name__=="__main__":
    unittest.main()
