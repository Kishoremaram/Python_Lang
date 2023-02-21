import unittest

class Test_Divisible(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(divis(100),8)
    def testcase_2(self):
        self.assertEqual(divis(50),4)

def divis(n):
    count=0
    for i in range(1,n):
        if i%3==0 and i%4==0:
            count=count+1
    print(count)
    return count

if __name__=="__main__":
    unittest.main()
