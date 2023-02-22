import unittest

class Test_Longestlen(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(Longest(["apple","banana","cat"]),6)
    def testcase_2(self):
        self.assertEqual(Longest(["goat","chicken","egg"]),7)

def Longest(l):
    for i in range(0,len(l)-1):
        if len(l[i])>len(l[i+1]):
            temp=l[i]
            l[i]=l[i+1]
            l[i+1]=temp
    print(len(l[-1]))
    return(len(l[-1]))

if __name__=="__main__":
    unittest.main()
