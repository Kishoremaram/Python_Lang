import unittest

class Test_Armstrong(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(armstrong(153),"Num is armstrong")
    def testcase_2(self):
        self.assertEqual(armstrong(185),"Not armstrong")

def armstrong(num):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if num==sum:
        print("Num is armstrong")
        return "Num is armstrong"
    else:
        print("Not armstrong")
        return "Not armstrong"

if __name__=="__main__":
    unittest.main()
