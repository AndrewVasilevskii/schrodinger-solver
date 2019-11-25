
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
#########
# import wx
#
# class MyFrame(wx.Frame):
#     def __init__(self, *args, **kwds):
#         kwds["style"] = wx.DEFAULT_FRAME_STYLE
#         wx.Frame.__init__(self, *args, **kwds)
#         self.window_1 = wx.SplitterWindow(self, wx.ID_ANY, style=wx.SP_LIVE_UPDATE| wx.SP_3DSASH)
#         self.window_1_pane_1 = wx.Panel(self.window_1, wx.ID_ANY)
#         self.window_1_pane_1.SetMinSize((300,200))
#         self.window_1_pane_2 = wx.Panel(self.window_1, wx.ID_ANY)
#         # self.window_1_pane_2.SetMinSize((300,150))
#         self.window_1.SetMinimumPaneSize(100)
#
#         self.window_1.SetSashGravity(1)
#
#
#         self.__set_properties()
#         self.__do_layout()
#
#     def __set_properties(self):
#         self.SetTitle("frame_1")
#         self.window_1_pane_1.SetBackgroundColour(wx.Colour(255, 255, 0))
#         self.window_1_pane_2.SetBackgroundColour(wx.Colour(50, 153, 204))
#
#     def __do_layout(self):
#         sizer_1 = wx.BoxSizer(wx.VERTICAL)
#         self.window_1.SplitHorizontally(self.window_1_pane_1, self.window_1_pane_2)
#         sizer_1.Add(self.window_1, 1, wx.EXPAND, 0)
#         self.SetSizer(sizer_1)
#         # sizer_1.Fit(self)
#         self.Layout()
#
# if __name__ == "__main__":
#     app = wx.App()
#     frame_1 = MyFrame(None, wx.ID_ANY, "")
#     frame_1.Show()
#     app.MainLoop()
#########
### WIZARD (PAGES)
# import wx
# import wx.adv as wiz
#
# class MyWizard(wiz.Wizard):
#     def __init__(self, *args, **kwargs):
#         super(MyWizard, self).__init__(*args, **kwargs)
#
#
# ########################################################################
# class TitledPage(wiz.WizardPageSimple):
#     """"""
#
#     #----------------------------------------------------------------------
#     def __init__(self, parent, title):
#         """Constructor"""
#         super(TitledPage, self).__init__(parent)
#
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         self.SetSizer(sizer)
#
#         title = wx.StaticText(self, -1, title)
#         title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
#         sizer.Add(title, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
#         sizer.Add(wx.StaticLine(self, -1), 0, wx.EXPAND|wx.ALL, 5)
#
#
#
# #----------------------------------------------------------------------
# def main():
#     """"""
#     wizard = MyWizard(None, -1, "Simple Wizard")
#     page1 = TitledPage(wizard, "Page 1")
#     page2 = TitledPage(wizard, "Page 2")
#     page3 = TitledPage(wizard, "Page 3")
#     page4 = TitledPage(wizard, "Page 4")
#
#     wiz.WizardPageSimple.Chain(page1, page2)
#     print(page1.GetNext())
#     wiz.WizardPageSimple.Chain(page2, page3)
#     print(page2.GetNext())
#     wiz.WizardPageSimple.Chain(page3, page4)
#     print(page3.GetNext())
#     print(page4.GetNext())
#
#     wizard.FitToPage(page1)
#
#     wizard.RunWizard(page1)
#
#     wizard.Destroy()
#
# #----------------------------------------------------------------------
# if __name__ == "__main__":
#     app = wx.App(False)
#     main()
#     app.MainLoop()

### WIZARD (PAGES)


# import wx
# import wx.lib.agw.pycollapsiblepane as PCP
#
# class MyFrame(wx.Frame):
#
#     def __init__(self, parent):
#
#         wx.Frame.__init__(self, parent, -1, "PyCollapsiblePane Demo")
#
#         panel = wx.Panel(self)
#
#         title = wx.StaticText(panel, label="PyCollapsiblePane")
#         title.SetFont(wx.Font(18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
#         title.SetForegroundColour("blue")
#
#         self.cp = cp = PCP.PyCollapsiblePane(panel, label="Some Data", style=1,agwStyle=PCP.CP_GTK_EXPANDER)
#         cp.SetButtonFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, True))
#         self.MakePaneContent(cp.GetPane())
#
#         self.cp.Bind(wx.EVT_COLLAPSIBLEPANE_CHANGED, self.ee)
#         self.sizer = wx.BoxSizer(wx.VERTICAL)
#         self.sizer.Add(title, 0, wx.ALL, 25)
#         self.sizer.Add(cp, 0, wx.RIGHT | wx.LEFT | wx.EXPAND, 25)
#         self.sizer.Add(wx.StaticText(panel, label="TEXT AFTER"))
#
#         panel.SetSizer(self.sizer)
#         self.sizer.Layout()
#
#     def ee(self, event):
#         self.sizer.Layout()
#
#
#     def MakePaneContent(self, pane):
#         ''' Just makes a few controls to put on `PyCollapsiblePane`. '''
#
#         nameLbl = wx.StaticText(pane, -1, "Name:")
#         name = wx.TextCtrl(pane, -1, "");
#
#         addrLbl = wx.StaticText(pane, -1, "Address:")
#         addr1 = wx.TextCtrl(pane, -1, "");
#         addr2 = wx.TextCtrl(pane, -1, "");
#
#         cstLbl = wx.StaticText(pane, -1, "City, State, Zip:")
#         city  = wx.TextCtrl(pane, -1, "", size=(150,-1));
#         state = wx.TextCtrl(pane, -1, "", size=(50,-1));
#         zip   = wx.TextCtrl(pane, -1, "", size=(70,-1));
#
#         addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
#         addrSizer.AddGrowableCol(1)
#         addrSizer.Add(nameLbl, 0,
#                       wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
#         addrSizer.Add(name, 0, wx.EXPAND)
#         addrSizer.Add(addrLbl, 0,
#                       wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
#         addrSizer.Add(addr1, 0, wx.EXPAND)
#         addrSizer.Add((5,5))
#         addrSizer.Add(addr2, 0, wx.EXPAND)
#
#         addrSizer.Add(cstLbl, 0,
#                       wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
#
#         cstSizer = wx.BoxSizer(wx.HORIZONTAL)
#         cstSizer.Add(city, 1)
#         cstSizer.Add(state, 0, wx.LEFT | wx.RIGHT, 5)
#         cstSizer.Add(zip)
#         addrSizer.Add(cstSizer, 0, wx.EXPAND)
#
#         border = wx.BoxSizer()
#         border.Add(addrSizer, 1, wx.EXPAND | wx.ALL, 5)
#         pane.SetSizer(border)
#
#
# # our normal wxApp-derived class, as usual
#
# app = wx.App(0)
#
# frame = MyFrame(None)
# app.SetTopWindow(frame)
# frame.Show()
#
# app.MainLoop()