import unittest

class Test_Average(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(Average([20,30,40,50,10]),30)
    def testcase_2(self):
        self.assertEqual(Average([5,10,30]),15)

def Average(a):
    sum=0
    count=0
    for i in a:
        count=count+1
        sum=sum+i
        avg=sum//count
    print(avg)
    return avg

if __name__=="__main__":
    unittest.main()
