#coding=utf-8
from xml.dom import minidom
import time
class UrlItem(): 
    id = ""
    title = ""
    address = ""
    detail = ""
    
class DbItem():
    id = "" 
    ip = ""
    port = ""
    dbase = ""
    username = ""
    password = ""
    detail = ""
    
'''
解析xml文件
'''    
filePos = 'resource/checkItem.xml'

class ParserXml():
    '''
            解析出需要检查的 url项列表
    '''    
    
    def doParseUrl(self):
        dom = minidom.parse(filePos)
        root = dom.documentElement
        urlList = []
        for urlItem in root.getElementsByTagName('urlItem'):
            idNode = urlItem.getElementsByTagName('id')[0] 
            titleNode = urlItem.getElementsByTagName('title')[0] 
            addressNode = urlItem.getElementsByTagName('address')[0]
            detailNode = urlItem.getElementsByTagName('detail')[0]
            #print titleNode.toxml()
            #print  (titleNode.childNodes[0].nodeValue)
            urlItemObj = UrlItem()
            urlItemObj.id = idNode.childNodes[0].nodeValue
            urlItemObj.title = titleNode.childNodes[0].nodeValue
            urlItemObj.address = addressNode.childNodes[0].nodeValue
            urlItemObj.detail = detailNode.childNodes[0].nodeValue
            
            urlList.append(urlItemObj)
        return urlList
    '''
            解析出需要检查的db项列表
    '''
    def doParseDb(self):
        dom = minidom.parse(filePos)
        root = dom.documentElement
        dblist = []
        for urlItem in root.getElementsByTagName('dbItem'):
            id = urlItem.getElementsByTagName('id')[0] 
            title = urlItem.getElementsByTagName('title')[0] 
            ip = urlItem.getElementsByTagName('ip')[0] 
            port = urlItem.getElementsByTagName('port')[0]
            dbase = urlItem.getElementsByTagName('dbase')[0]
            username = urlItem.getElementsByTagName('username')[0]
            password = urlItem.getElementsByTagName('password')[0]
            #print titleNode.toxml()
            #print  (titleNode.childNodes[0].nodeValue)
            dbItemObj = DbItem()
            dbItemObj.id =  id.childNodes[0].nodeValue
            dbItemObj.title =  title.childNodes[0].nodeValue
            dbItemObj.ip = ip.childNodes[0].nodeValue
            dbItemObj.port = port.childNodes[0].nodeValue
            dbItemObj.dbase = dbase.childNodes[0].nodeValue
            dbItemObj.username = username.childNodes[0].nodeValue
            dbItemObj.password = password.childNodes[0].nodeValue
            
            dblist.append(dbItemObj)
    
        return dblist
    
    def getGroupname(self):
        dom = minidom.parse(filePos)
        root = dom.documentElement
        groupnameNode = root.getElementsByTagName('groupname')[0]
        groupname = groupnameNode.childNodes[0].nodeValue
        return groupname
    


 