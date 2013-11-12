#coding=utf-8
import time,platform,cx_Oracle
class DbCheckRet():
    status =0 # 状态 1：成功 ；0：不成功
    errorMsg = '' # 错误消息
    spend =0 
    ip = ""
    
    
'''
用于检查 数据库联通是否正常
'''
class DbChecker(): 
    '''
    检查是否可以正常连接
    返回：DbCheckRet 对象
    '''
    def checkDb(self,host,port,dbase,login,passwrd):
       #print platform.python_version()
       ret = DbCheckRet()
       try:
           ret.ip = host
           
           st = time.time()   
           dsn = cx_Oracle.makedsn(host, port, dbase) 
           connection = cx_Oracle.connect(login, passwrd, dsn)
           #connection = cx_Oracle.connect('fgwoa', 'fgwoa', '(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=172.16.0.112)(PORT=1521)))(CONNECT_DATA=(SID=FGWWW1))) ') 
           # print connection.version    
           end = time.time()  
           ret.status=1;           
           ret.spend = end - st
           
       except cx_Oracle.DatabaseError as e:
           ret.errorMsg= e
           # print ret.errorMsg
       return ret


 