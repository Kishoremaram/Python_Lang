import unittest

class Test_Reverse(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(reverse([2,5,3,6,5,4]),[4,5,6,3,5,2])
    def testcase_2(self):
        self.assertEqual(reverse([23,52,33,65,53,41]),[41,53,65,33,52,23])

def reverse(list1):
    print("List before reversed:",list1)
    list2=[]
    for value in list1:
        list2=[value]+list2
    print("List after reverse:",list2)
    return list2

if __name__=="__main__":
    unittest.main()
