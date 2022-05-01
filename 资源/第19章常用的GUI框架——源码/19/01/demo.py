# -*- coding:utf-8 -*-
import wx 			# 导入wxPython
class App(wx.App):
    # 初始化方法
    def OnInit(self):
        frame = wx.Frame(parent=None, title='Hello wyPython') # 创建窗口
        frame.Show() # 显示窗口
        return True  # 返回值

if __name__ == '__main__':
    app = App()     # 创建App类的实例
    app.MainLoop()  # 调用App类的MainLoop()主循环方法










