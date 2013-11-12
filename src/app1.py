import ParserXml

import wx
if  __name__ ==  '__main__' :  
    app = wx.PySimpleApp()  
    frame = wx.Frame(parent=None )  
    frame.Show(True )  
    parser = ParserXml.ParserXml()
    print parser.getGroupname()
    app.MainLoop()
    