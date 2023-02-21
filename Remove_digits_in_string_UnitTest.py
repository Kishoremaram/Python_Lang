import unittest

class Test_Removeofdigit(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(removedigit("kishore123kumar"),"kishorekumar")
    def testcase_2(self):
        self.assertEqual(removedigit("Hello888world"),"Helloworld")

def removedigit(str1):
    num={"0","1","2","3","4","5","6","7","8","9"}
    str2=""
    for i in str1:
        if i not in num:
            str2=str2+i
    print("string:",str2)
    return str2

if __name__=="__main__":
    unittest.main()
