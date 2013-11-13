#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import decimal
import ParserXml
import ServerCheck
from threading import Thread
from wx.tools.Editra.src.extern.pubsub import Publisher
import images
import sys
import time
import wx

try:
    from agw import pygauge as PG
except ImportError: # if it's not there locally, try the wxPython lib.
    try:
        import wx.lib.agw.pygauge as PG
    except:
        raise Exception("This demo requires wxPython version greater than 2.9.0.0")

'''
packages = [('数据库', '正式数据哭', '172.0.16.112', '通过'),('数据库', '正式数据哭', '172.0.16.112', '通过'),('数据库', '正式数据哭', '172.0.16.112', '通过'),('数据库', '正式数据哭', '172.0.16.112', '通过'),('数据库', '正式数据哭', '172.0.16.112', '通过'),
             ('url', 'org','172.0.16.112', '通过')]
'''
class MyFrame(wx.Frame):
    #----------------------------------------------------------------------
    def __init__(self, parent, id, title, size):
        
        Publisher().subscribe(self.updateDisplay, "update") 
        Publisher().subscribe(self.updateResult, "ispass")
        
        self.il = wx.ImageList(16, 16)
        self.idx1 = self.il.Add(images.Smiles.GetBitmap())
        
        bmp = wx.Bitmap('resource/images/red.jpg', wx.BITMAP_TYPE_JPEG)
        self.errImgIdx = self.il.Add(bmp)
        
        bmp = wx.Bitmap('resource/images/green.jpg', wx.BITMAP_TYPE_JPEG)
        self.rightImgIdx = self.il.Add(bmp)
        
        wx.Frame.__init__(self, parent, id, title, size)
        panel = wx.Panel(self, -1)
        self.panel = panel
        self.list = wx.ListCtrl(panel, -1, style=wx.LC_REPORT)
        self.list.InsertColumn(0, '类型', width=100)
        self.list.InsertColumn(1, '标题', width=150)
        self.list.InsertColumn(2, '地址标示', width=350)
        self.list.InsertColumn(3, '', width=50)
        self.list.InsertColumn(4, u'结果', width=100)
        '''需要添加图片列表'''
        self.list.SetImageList(self.il, wx.IMAGE_LIST_SMALL)        
        # 刷新检查结果  
        # self.checkAllTest()         
        """
        # 加载数据
        for i in packages:
            index = self.list.InsertStringItem(sys.maxint, i[0])
            self.list.SetStringItem(index, 1, i[1])
            self.list.SetStringItem(index, 2, i[2])
        """  
        # 列表sizer
        listBox = wx.BoxSizer(wx.HORIZONTAL)
        listBox.Add(self.list, proportion=2, flag= wx.EXPAND, border=1)
        
        # 操作sizer  
        handleBox = wx.BoxSizer(wx.HORIZONTAL)  
        self.process = PG.PyGauge(panel, -1, size=(100,25),style=wx.GA_HORIZONTAL)
        self.process.SetValue(0)
        
        self.process.SetBackgroundColour("#cbcbcb")
        self.process.SetBorderColor(wx.BLACK)
        handleBox.Add(self.process, proportion=14, flag= wx.EXPAND, border=5)
          
        # 空格标题
        self.title = wx.StaticText(panel, -1, ' ')
        handleBox.Add(self.title, proportion=1, flag= wx.EXPAND, border=1)  
        # 最终测试结果
        self.testResualtLabel = wx.StaticText(panel, -1, '',(100, 70))
        font = wx.Font(12, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)   
        self.testResualtLabel.SetFont(font)
        handleBox.Add(self.testResualtLabel, proportion=3, flag= wx.ALL, border=1)
        # btn
        self.muteBtn = wx.Button(panel, -1, u'开始测试')
        self.muteBtn.Bind(wx.EVT_BUTTON, self.OnClick, self.muteBtn)  
        self.muteBtn.SetDefault()
        self.muteBtn.SetFont(font)
        self.muteBtn.SetFocus()
        handleBox.Add(self.muteBtn, proportion=4, flag= wx.EXPAND, border=5)  
        
        # 主sizer   
        mainSizer = wx.BoxSizer(wx.VERTICAL)  
        mainSizer.Add(listBox, proportion=10, flag=wx.EXPAND)
        mainSizer.Add(handleBox, proportion=1, flag=wx.EXPAND)    
        
        panel.SetSizerAndFit(mainSizer)
        self.Centre()
        self.startCheck()
        
    #----------------------------------------------------------------------
    def OnClick(self, event):  
        """ 开始检查事件  """
        self.startCheck()
    #----------------------------------------------------------------------    
    def startCheck(self):  
        """ 开始检查  """
        self.process.SetBarColor("#9bbb58")
        self.process.SetValue(0);
        ''' Update 参数1:进度条的百分比，参数2:进度条速度
                                    进度条百分比需注意，每次累加如 第一次update 20，第二次update30，进度条当前进度是50%
        '''
        self.process.Update(20, 200)
        self.list.DeleteAllItems()
        self.testResualtLabel.SetLabel("testing...")         
        self.muteBtn.Disable()  
        """ 用线程来更新数据 不会阻塞界面 """   
        CheckThread()    
    #----------------------------------------------------------------------
        
    def updateDisplay(self, msg):  
        """ 更新列表显示 """
        retList = msg.data;
        for ret in retList:   
            index = self.list.InsertStringItem(sys.maxint, ret.type)
            self.list.SetStringItem(index, 1,ret.title)
            self.list.SetStringItem(index, 2,ret.urlSign)
            if str(ret.msg) == "正常":
                self.list.SetItemColumnImage(index, 3,self.rightImgIdx)
            else:
                self.list.SetItemColumnImage(index, 3,self.errImgIdx)
            self.list.SetStringItem(index, 4,ret.msg)
        #self.process.Refresh()
        
    #----------------------------------------------------------------------    
    def updateResult(self, msg):
        """ 更新测试总结果  """        
        isPass= msg.data
        if isPass == 1:            
            self.process.Update(80, 100)
            self.testResualtLabel.SetLabel('success')
            self.process.SetBarColor("#9bbb58")            
        else:
            self.process.Update(80, 100)
            self.testResualtLabel.SetLabel('failure')
            self.process.SetBarColor(wx.RED)
        
        self.process.SetValue(0);
        self.muteBtn.Enable()
        self.muteBtn.SetFocus()
        
class MyApp(wx.App):
    def OnInit(self):
        parserXml = ParserXml.ParserXml()  
        frame = MyFrame(None, id=-1, title="ServerCheck 1.0.0  [" +parserXml.getGroupname()+"]", size=(1200,1100))

        frame.Show(True)
        frame.SetSize((780, 480))
        self.SetTopWindow(frame)
        
        icon=wx.EmptyIcon()   
        icon.LoadFile("resource/images/sc.ico",wx.BITMAP_TYPE_ICO)   
        frame.SetIcon(icon)
        #frame.tbicon=wx.TaskBarIcon()   
        #frame.tbicon.SetIcon(icon,"wxPython Demo")   
        return True
    
#----------------------------------------------------------------------    
class CheckThread(Thread): 
    """ 防止主界面不流畅，把耗时较慢的业务操作放在线程中 """
    #----------------------------------------------------------------------
    def __init__(self):        
        Thread.__init__(self)
        self.start()    # start the thread
    #----------------------------------------------------------------------
    def run(self):
        """Run Worker Thread."""
        serverCheck = ServerCheck.ServerCheck()     
        retList  = serverCheck.doAllTest()
        ''' 所有'''
        if serverCheck.isPass == 1: 
            time.sleep(1)
        wx.CallAfter(Publisher().sendMessage, "update", retList,"noMessage")
        wx.CallAfter(Publisher().sendMessage, "ispass", serverCheck.isPass,"noMessage")  
    #----------------------------------------------------------------------
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
        