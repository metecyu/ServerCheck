#coding=utf-8
import time
import urllib2
class UrlCheckRet(): 
    
    status =0 # 状态 1：成功 ；0：不成功
    code = 0 # http code
    spend =0 # 花费时间
    
'''
用于检查 url是否连接正常
'''
class HttpChecker(): 
    '''
    检查url是否可以正常连接
    返回：UrlCheckRet 对象
    '''
    def checkUrl(self,url):
       ret = UrlCheckRet()
       try:
           st = time.time()   
           r = urllib2.urlopen(url,timeout=1)
           end = time.time()   
           if r.code in (200, 401):
               
               #print '[{}]: '.format(url), r.code
               ret.status = 1
               ret.code = r.code
               ret.spend = end - st
          
       except urllib2.URLError as e:
           r = e
           #print r  
       return ret


 