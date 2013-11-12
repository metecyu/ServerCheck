#coding=utf-8
'''
Created on 2013-10-22

@author: TonyYu
'''
import DbChecker
import HttpChecker
import ParserXml
#from src.ParserXml import ParserXml, DbItem
class CheckRet():
    id = '' 
    status = '0' #状态 1：成功 ；0：不成功
    msg = '正常'
    title =''
    spend =0
    urlSign =''
    type = '服务'
    
class ServerCheck():
   isPass = 1   
   
   
   def setIsPass(self,retList):
        for ret in retList:   
            if ret.status==0:
                self.isPass=0
                
   def doAllTest(self):
        retList = [] 
        parserXml = ParserXml.ParserXml()
        list = parserXml.doParseUrl()
        
        http = HttpChecker.HttpChecker()
        db = DbChecker.DbChecker()
        
        '''====检查 url列表===='''       
        for urlItem in list:      
            
            dbRet = http.checkUrl(urlItem.address)
            '''转换成统一检查项目'''
            ret = CheckRet() 
            ret.id = urlItem.id
            ret.status   = dbRet.status
            ret.title = urlItem.title
            ret.urlSign = urlItem.address
            if ret.status == 0:
                ret.msg = "无法连接"
            retList.append(ret)    
            
        '''====检查 Db列表===='''    
        list2 = parserXml.doParseDb()
        for dbItem in list2:            
            '''转换成统一检查项目'''
            dbRet = db.checkDb(dbItem.ip, dbItem.port, dbItem.dbase, dbItem.username, dbItem.password)
            ret = CheckRet()
            ret.id = dbItem.id
            ret.title = dbItem.title
            ret.status = dbRet.status
            ret.urlSign = dbRet.ip
            ret.type = '数据库'
            #print 'dbRet.status',dbRet.status
            if ret.status == 0:
                ret.msg = '无法连接'
            retList.append(ret)   
            self.setIsPass(retList) 
            #print  "db:",dbItem.id,' ',dbItem.title
        return retList
    
