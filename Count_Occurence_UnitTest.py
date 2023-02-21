import unittest

class Test_Occur(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(occur([2,3,4,2,3,2,2]),4)
    def testcase_2(self):
        self.assertEqual(occur([5,2,5,1,2,5]),2)

def occur(a):
        b=2
        count=0
        for i in a:
                if i==b:
                        count=count+1
        print(count)
        return count
    
if __name__=="__main__":
    unittest.main()
