import wx.lib.scrolledpanel as scrolled
import wx
import datetime
import wx.lib.agw.pycollapsiblepane as PCP

class MessagesPanel(wx.Panel):

    def __init__(self, *args, **kwargs):
        super(MessagesPanel, self).__init__(*args, **kwargs)
        self.parent = args[0]

        self.scrolledPanel = scrolled.ScrolledPanel(self, style=wx.TAB_TRAVERSAL | wx.SUNKEN_BORDER)
        self.scrolledPanel.SetAutoLayout(1)
        self.scrolledPanel.SetupScrolling()


        self.verticalBorderSizer = wx.BoxSizer(wx.VERTICAL)
        self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.verticalBorderSizer.AddSpacer(5)
        self.verticalBorderSizer.Add(self.mainSizer, 1, wx.EXPAND)
        self.verticalBorderSizer.AddSpacer(5)

        self.instrumentsSizer = wx.BoxSizer(wx.VERTICAL)
        clearButton = wx.BitmapButton(self, bitmap=wx.Bitmap("bitmaps/trash@5x.png"))
        clearButton.Bind(wx.EVT_LEFT_DOWN, self.clear)

        self.instrumentsSizer.Add(clearButton)
        self.messagesSizer = wx.BoxSizer(wx.VERTICAL)
        self.mainSizer.AddSpacer(5)
        self.mainSizer.Add(self.scrolledPanel, 1, wx.EXPAND)
        self.mainSizer.AddSpacer(2)
        self.mainSizer.Add(self.instrumentsSizer, 0, wx.RIGHT)
        self.mainSizer.AddSpacer(2)
        self.messagesSizer.AddSpacer(2)
        self.scrolledPanel.SetSizer(self.messagesSizer)
        self.SetSizerAndFit(self.verticalBorderSizer)
        self.onNewSession()

    def onNewSession(self):
        time = datetime.datetime.now().strftime("%B %d, %A %Y %H:%M:%S")
        messageField = wx.StaticText(self.scrolledPanel, label="New session: {time}".format(time=time))
        self.messagesSizer.Add(messageField)
        self.messagesSizer.AddSpacer(3)
        self.scrolledPanel.Scroll(0, self.scrolledPanel.GetSize()[1])
        self.Layout()

    def Add(self, message, withparams=False):
        time = datetime.datetime.now().strftime("%H:%M:%S")
        if not withparams:
            messageWithTimestamp = "   [{time}]: {mess}".format(time=time, mess=message)
            messageField = wx.StaticText(self.scrolledPanel, label=messageWithTimestamp)
            self.messagesSizer.Add(messageField)
            self.messagesSizer.AddSpacer(3)
        else:
            messageWithTimestamp = "   [{time}]: {mess}".format(time=time, mess=message)
            messageField = wx.StaticText(self.scrolledPanel, label=messageWithTimestamp)
            self.messagesSizer.Add(messageField)
            self.messagesSizer.AddSpacer(3)

            self.cp = cp = PCP.PyCollapsiblePane(self.scrolledPanel, label="Some Data", style=1, agwStyle=PCP.CP_GTK_EXPANDER)
            cp.SetButtonFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, True))
            self.MakePaneContent(cp.GetPane())
            self.cp.Bind(wx.EVT_COLLAPSIBLEPANE_CHANGED, self.onCollapsePanel)

            self.messagesSizer.Add(cp)
            self.messagesSizer.AddSpacer(3)

        self.scrolledPanel.Scroll(0, self.scrolledPanel.GetSize()[0])
        self.mainSizer.Layout()
        self.parent.Layout()

    def onCollapsePanel(self, event):
        self.mainSizer.Layout()
        self.parent.Layout()

    def clear(self, event=None):
        self.messagesSizer.Clear(True)
        self.onNewSession()

    def MakePaneContent(self, pane):

            nameLbl = wx.StaticText(pane, -1, "Name:")
            name = wx.TextCtrl(pane, -1, "")

            addrLbl = wx.StaticText(pane, -1, "Address:")
            addr1 = wx.TextCtrl(pane, -1, "")
            addr2 = wx.TextCtrl(pane, -1, "")

            cstLbl = wx.StaticText(pane, -1, "City, State, Zip:")
            city  = wx.TextCtrl(pane, -1, "", size=(150,-1))
            state = wx.TextCtrl(pane, -1, "", size=(50,-1))
            zip   = wx.TextCtrl(pane, -1, "", size=(70,-1))

            addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
            addrSizer.AddGrowableCol(1)
            addrSizer.Add(nameLbl, 0,
                          wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
            addrSizer.Add(name, 0, wx.EXPAND)
            addrSizer.Add(addrLbl, 0,
                          wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
            addrSizer.Add(addr1, 0, wx.EXPAND)
            addrSizer.Add((5,5))
            addrSizer.Add(addr2, 0, wx.EXPAND)

            addrSizer.Add(cstLbl, 0,
                          wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)

            cstSizer = wx.BoxSizer(wx.HORIZONTAL)
            cstSizer.Add(city, 1)
            cstSizer.Add(state, 0, wx.LEFT | wx.RIGHT, 5)
            cstSizer.Add(zip)
            addrSizer.Add(cstSizer, 0, wx.EXPAND)

            border = wx.BoxSizer()
            border.Add(addrSizer, 1, wx.EXPAND | wx.ALL, 5)
            pane.SetSizer(border)
