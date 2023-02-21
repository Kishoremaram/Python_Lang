import unittest

class Test_Swap(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(swapping([1,5,3,4,7,10]),[10,5,3,4,7,1])
    def testcase_2(self):
        self.assertEqual(swapping([5,10,15,20,25]),[25,10,15,20,5])

def swapping(l):
    temp=l[0]
    l[0]=l[-1]
    l[-1]=temp
    #l[0],l[-1]=l[-1],l[0]
    print(l)
    return(l)

if __name__=="__main__":
    unittest.main()
