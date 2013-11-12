'''
Created on 2013-10-18

@author: TonyYu
'''
#coding=utf-8
from src.DbChecker import DbChecker
import unittest

class Test(unittest.TestCase):
    def setUp(self):  
        self.dbChecker = DbChecker()  
      
    def tearDown(self):  
        self.dbChecker = None 
    
    def testCheckSucuess(self):
       ret = self.dbChecker.checkDb("172.16.0.112","1521","FGWWW1","fgwoa","fgwoa")
       print ret.status,' ',ret.spend
       self.assertEqual(1,ret.status)
    
    # http://localhost:8085/newOA
    def testCheckFailure(self):
       ret = self.dbChecker.checkDb("172.16.0.112","1521","FGWWW1","fgwoa_faliure","fgwoa")
       print ret.status,' ',ret.spend
       self.assertEqual(0,ret.status)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()