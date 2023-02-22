import unittest

class Test_LEven(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(LargeEven([1,2,3,4,5,6,7,8]),8)
    def testcase_2(self):
        self.assertEqual(LargeEven([22,33,66,11,55,44]),66)

def LargeEven(a):
    b=[]
    for i in a:
        if i%2==0:
            b.append(i)
    b.sort()
    print(b[-1])
    return b[-1]

if __name__=="__main__":
    unittest.main()
