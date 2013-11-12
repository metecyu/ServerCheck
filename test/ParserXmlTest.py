'''
Created on 2013-10-21

@author: TonyYu
'''
#coding=utf-8
from src.ParserXml import ParserXml
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        self.parserXml = ParserXml()  


    def tearDown(self):
        self.parserXml = None  

    def testDoParse(self):
        list = self.parserXml.doParseUrl()
        for UrlItem in list:            
            print  "url:",UrlItem.id,' ',UrlItem.title
            
        list2 = self.parserXml.doParseDb()
        for dbItem in list2:            
            print  "db:",dbItem.id,' ',dbItem.title
            
    def testGetGroupname(self):
        groupName  = self.parserXml.getGroupname()
        print groupName
       
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()