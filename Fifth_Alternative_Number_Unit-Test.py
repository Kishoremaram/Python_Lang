import unittest

class Test_5th_Alternate(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(alter(20),[5,10,15])
    def testcase_2(self):
        self.assertEqual(alter(30),[5,10,15,20,25])

def alter(n):
    list1=[]
    for i in range(1,n):
        list1.append(i)
    print("list:",list1)
    list2=[]
    for j in range(5,len(list1),5):
        list2.append(j)
    print(list2)
    return list2

if __name__=="__main__":
    unittest.main()
