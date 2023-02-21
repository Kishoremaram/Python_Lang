import unittest

class Test_Fibanocci(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(fibanocci(10),[0,1,1,2,3,5,8,13,21,34])
    def testcase_2(self):
        self.assertEqual(fibanocci(5),[0,1,1,2,3])
    def testcase_3(self):
        self.assertEqual(fibanocci(7),[0,1,1,2,3,5,8])

def fibanocci(n):
    f=[0,1]
    for i in range(2,n):
        f.append(f[i-1]+f[i-2])
    print(f)
    return f

if __name__=="__main__":
    unittest.main()
