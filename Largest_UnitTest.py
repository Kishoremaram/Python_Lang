import unittest

class Test_Large(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(Largest([9,3,4,5,63,2]),63)
    def testcase_2(self):
        self.assertEqual(Largest([95,30,41,22]),95)

def Largest(a):
    a.sort()
    print(a[-1])
    return a[-1]

if __name__=="__main__":
    unittest.main()
