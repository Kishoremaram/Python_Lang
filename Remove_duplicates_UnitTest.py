import unittest

class Test_Duplicates(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(dupli([2,3,4,2,3,5]),[2,3,4,5])
    def testcase_2(self):
        self.assertEqual(dupli([2,3,7,2,8,5]),[2,3,7,8,5])

def dupli(list1):
    new_list=[]
    for i in list1:
        if i not in new_list:
            new_list.append(i)
    print(new_list)
    return(new_list)

if __name__=="__main__":
    unittest.main()
