import unittest

class Test_Oddoccuring(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(Oddoccuring([1,1,2,2,6,6,6,6,6,7]),[6,7])
    def testcase_2(self):
        self.assertEqual(Oddoccuring([1,2,2,3,4,5,5]),[1,3,4])

def Oddoccuring(l):
    list1=[]
    list2=[]
    for i in range(0,len(l)):
        count=0
        for j in range(0,len(l)):
            if l[i]==l[j]:
                count=count+1
        if count%2!=0:
            list1.append(l[i])
    #list2=list(set(list1))
    #print(list2)
    for x in list1:
        if x not in list2:
            list2.append(x)
    print(list2)
    return list2

if __name__=="__main__":
    unittest.main()
