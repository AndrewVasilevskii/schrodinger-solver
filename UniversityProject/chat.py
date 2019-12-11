
import wx

class Chat(wx.Frame):

    def __init__(self, *args, messagePanel, **kwargs):
        super().__init__(*args, **kwargs)

        self.panel = wx.Panel(self)
        self.messagePanel = messagePanel
        self.textField = wx.TextCtrl(self.panel, style=wx.TE_PROCESS_ENTER, size=(150, -1))
        self.textField.Bind(wx.EVT_TEXT_ENTER, self.textEnter)
        self.clearBut = wx.Button(self.panel, label="With params", size=(100, -1))
        self.clearBut.Bind(wx.EVT_BUTTON, self.onClear)
        tempSizer = wx.BoxSizer(wx.HORIZONTAL)
        tempSizer.AddSpacer(10)
        tempSizer.Add(self.textField)
        tempSizer.AddSpacer(10)
        tempSizer.Add(self.clearBut)
        tempSizer.AddSpacer(10)

        self.panel.SetSizer(tempSizer)


    def textEnter(self, event):
        self.messagePanel.Add(message=self.textField.GetValue())

    def onClear(self, event):
        self.messagePanel.Add(self.textField.GetValue(), True)