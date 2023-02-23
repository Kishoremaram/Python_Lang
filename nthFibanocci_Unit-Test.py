import unittest

class Test_nthFibanocci(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(nthfibanocci(8),13)
    def testcase_2(self):
        self.assertEqual(nthfibanocci(5),3)
    def testcase_3(self):
        self.assertEqual(nthfibanocci(6),5)

def nthfibanocci(n):
    a=[0,1]
    for i in range(2,n):
        a.append(a[i-1]+a[i-2])
    print(a)
    print(a[n-1])
    return a[n-1]

if __name__=="__main__":
    unittest.main()
