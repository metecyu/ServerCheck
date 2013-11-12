'''
Created on 2013-10-18

@author: TonyYu
'''
from src.HttpChecker import HttpChecker, UrlCheckRet
import unittest


class Test(unittest.TestCase):
    def setUp(self):  
        self.httpChecker = HttpChecker()  
      
    def tearDown(self):  
        self.httpChecker = None  

    
    def testCheckSucuess(self):
       ret = self.httpChecker.checkUrl("http://172.16.0.166:8080/org/exclude/OrgService.ws") 
       status = ret.status
       print 'spend:',ret.spend
       self.assertEqual(1,status)
    
    # http://localhost:8085/newOA
    def testCheckFailure(self):
       ret = self.httpChecker.checkUrl("http://172.16.0.166:8080/org/exclude/noAddress.ws")
       status = ret.status
       print 'info:',ret.spend,
       self.assertEqual(0,status)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()