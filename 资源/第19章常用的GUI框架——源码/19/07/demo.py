# -*- coding:utf-8 -*-
import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '用户登录', size = (400, 300))
        #创建面板
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel ,label="请输入用户名和密码")
        #添加容器，容器中控件按纵向排列
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.title,proportion=0,flag=wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER, border = 15 )
        panel.SetSizer(vsizer)
if __name__ == '__main__':
    app = wx.App()                      # 初始化
    frame = MyFrame(parent=None,id=-1)  # 实例MyFrame类，并传递参数
    frame.Show()                        # 显示窗口
    app.MainLoop()                      # 调用主循环方法
















