import unittest

class Test_removeoddchar(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(removeoddchar("helloteam"),"hloem")
    def testcase_2(self):
        self.assertEqual(removeoddchar("goodmorning"),"gomrig")

def removeoddchar(str1):
    res=""
    for i in range(len(str1)):
        if i%2==0:
            res=res+str1[i]
    print("removed odd Characters:",res)
    return res

if __name__=="__main__":
    unittest.main()
