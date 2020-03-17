
import wx
from mainFrame import MainFrame
import multiprocessing

if __name__ == '__main__':

    multiprocessing.freeze_support()
    app = wx.App()
    # size = wx.Size(945, 685)
    size = wx.Size(745, 750)
    pos = wx.Point(100, 100)
    frame = MainFrame(None, title='University work', size=size, pos=pos, style=wx.DEFAULT_FRAME_STYLE )
    frame.Show()
    app.MainLoop()