#coding=utf-8
'''
Created on 2013-10-18

@author: TonyYu
'''

from src.ServerCheck import ServerCheck
import unittest

class Test(unittest.TestCase):
    def setUp(self):  
        self.serverCheck = ServerCheck()  
      
    def tearDown(self):  
        self.serverCheck = None 
    
    def testCheckSucuess(self):
        retList  = self.serverCheck.doAllTest()
        print retList.__len__()
        for ret in retList:   
            print ret.id,' ',ret.title,' status:',ret.status,' ',ret.msg ," ",ret.urlSign
        print '测试结果:',self.serverCheck.isPass
        self.assertEqual(0,self.serverCheck.isPass)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()