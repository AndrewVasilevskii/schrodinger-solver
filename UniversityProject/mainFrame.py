import wx
from customWx.messagesPanel import MessagesPanel
from canvas import Canvas
from model import Model

class MainFrame(wx.Frame):

    currentModel = Model()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        icon = wx.Icon('bitmaps/icon.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        self.splitterWindow = splitterWindow = wx.SplitterWindow(self, wx.ID_ANY, style=wx.SP_NO_XP_THEME)
        splitterWindow.SetSashGravity(0)
        splitterWindow.SetMinimumPaneSize(150)
        mainSizer = wx.BoxSizer()
        mainSizer.Add(splitterWindow, 1, wx.EXPAND, 0)
        self.SetSizer(mainSizer)

        self.canvasPanel = canvasPanel = wx.Panel(splitterWindow, )
        # self.canvasPanel.SetBackgroundColour(wx.RED)
        canvasPanel.SetMinSize((450, 450))
        self.canvas = canvas = Canvas(canvasPanel, -1)
        self.canvasSizer = canvasSizer = wx.BoxSizer(wx.VERTICAL)
        self.canvasPanel.SetSizer(canvasSizer)
        canvasSizer.Add(canvas, 1, wx.SHAPED)

        canvasSizer.AddSpacer(4)

        self.scrollPan = MessagesPanel(splitterWindow, style=wx.SUNKEN_BORDER)
        # self.scrollPan.SetBackgroundColour(wx.BLUE)
        splitterWindow.SplitHorizontally(canvasPanel, self.scrollPan)

        self.Layout()

        # self.panel = panel = wx.Panel(self)
        #
        # self.mainSizer = mainSizer = wx.BoxSizer(wx.VERTICAL)
        # panel.SetSizer(self.mainSizer)
        #
        # self.canvas = Canvas(self.panel, -1)
        #
        # # Canvas
        # self.canvas_box = wx.BoxSizer()
        # self.canvas_box.Add(self.canvas, 1, wx.SHAPED)
        #
        # mainSizer.Add(self.canvas_box, 2, wx.EXPAND)
        # self.textField = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(150,-1))
        # self.textField.Bind(wx.EVT_TEXT_ENTER, self.textEnter)
        #
        # self.clearBut = wx.Button(panel, label="With params", size=(90,-1))
        # self.clearBut.Bind(wx.EVT_BUTTON, self.onClear)

        # tempSizer = wx.BoxSizer()
        # tempSizer.AddSpacer(10)
        # tempSizer.Add(self.textField)
        # tempSizer.AddSpacer(10)
        # tempSizer.Add(self.clearBut)
        # from settingssizer import SettingsSizer
        # setSizer = SettingsSizer(parent=panel, label="BOX", choices=("box1", "box2","box3", "box4","box5", "box6"), size=(2,3), orient=wx.HORIZONTAL)
        # setSizer.SetMaxSelectionNumber(3)
        # setSizer.SetSelectionMode(ChoiceMode.notMoreThan)
        # tempSizer.Add(setSizer)
        #
        #
        # mainSizer.AddSpacer(4)
        # mainSizer.Add(tempSizer,0)
        # mainSizer.AddSpacer(4)
        #
        # self.scrollPan = MessagesPanel(self.panel)
        # mainSizer.Add(self.scrollPan, 1, wx.EXPAND | wx.FIXED_MINSIZE)

        # Creating and filling the top menu bar
        self.topMenuBar = wx.MenuBar()
        self.createMenuBar()

    def createMenuBar(self):

        self.fileMenu = fileMenu = wx.Menu()
        screenshotButton = wx.MenuItem(fileMenu, wx.ID_SAVEAS, '&Screenshot\tCtrl+S')
        screenshotButton.SetBitmap(wx.Bitmap('bitmaps/screenshot.png'))
        saveButton = wx.MenuItem(fileMenu, wx.ID_SAVE, '&Save')
        saveButton.SetBitmap(wx.Bitmap('bitmaps/save.png'))
        openButton = wx.MenuItem(fileMenu, wx.ID_OPEN, '&Open')
        openButton.SetBitmap(wx.Bitmap('bitmaps/open.png'))
        quitButton = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+Q')
        quitButton.SetBitmap(wx.Bitmap('bitmaps/exit.png'))

        fileMenu.Append(screenshotButton)
        fileMenu.AppendSeparator()
        fileMenu.Append(saveButton)
        fileMenu.Append(openButton)
        fileMenu.AppendSeparator()
        fileMenu.Append(quitButton)

        self.Bind(wx.EVT_MENU, self.onScreenshot, screenshotButton)
        self.Bind(wx.EVT_MENU, self.onSave, saveButton)
        self.Bind(wx.EVT_MENU, self.onOpen, openButton)
        self.Bind(wx.EVT_MENU, self.onExit, quitButton)
        #
        self.modelMenu = modelMenu = wx.Menu()
        self.solveMenu = solveMenu = wx.Menu()
        solveMenu.AppendSeparator()
        self.canvasMenu = canvasMenu = wx.Menu()
        canvasMenu.AppendSeparator()

        # Help menu
        self.helpMenu = helpMenu = wx.Menu()

        aboutButton = wx.MenuItem(helpMenu, wx.ID_ABOUT, '&About')
        aboutButton.SetBitmap(wx.Bitmap('bitmaps/about.png'))

        helpMenu.Append(aboutButton)
        helpMenu.AppendSeparator()
        self.Bind(wx.EVT_MENU, self.onAbout, aboutButton)

        # Chat menu
        self.chat = chat = wx.Menu()

        # Gathering menu
        self.topMenuBar.Append(fileMenu, 'File')
        self.topMenuBar.Append(modelMenu, '&Model')
        self.topMenuBar.Append(solveMenu, '&Solve')
        self.topMenuBar.Append(canvasMenu, '&Canvas')
        self.topMenuBar.Append(helpMenu, '&Help')
        self.topMenuBar.Append(chat, '&Chat')

        self.SetMenuBar(self.topMenuBar)
        self.Bind(wx.EVT_CLOSE, self.onExit)
        self.Bind(wx.EVT_MENU_OPEN, self.onMenuOpen)

    def onScreenshot(self, event):
        print("SCREENSHOT")

    def onSave(self, event):
        print("SAVE")

    def onOpen(self, event):
        print("OPEN")

    def onExit(self, event):
        import sys
        sys.exit()

    def onModel(self):
        from settingsModel import SettingsModel
        print(self.currentModel.parameters)
        with SettingsModel(self, model=self.currentModel, style=wx.CLOSE_BOX, size=(340,330)) as dia:
            dia.ShowModal()
        print(self.currentModel.parameters)

    def onSolve(self):
        from settingsModelParameters import SettingsModelParameters
        with SettingsModelParameters(self, model=self.currentModel, style=wx.CLOSE_BOX, size=(560,270)) as dia:
            dia.ShowModal()

    def onAbout(self, event):
        message = 'Program for a university project.\nBy Andrew Vasilevskii.'
        wx.MessageBox(message, 'About', wx.OK | wx.ICON_ASTERISK)

    def onMenuOpen(self, event):
        selectedMenu = event.GetMenu()
        if selectedMenu == self.chat:
            self.onChat()
        if selectedMenu == self.modelMenu:
            self.onModel()
        if selectedMenu == self.solveMenu:
            self.onSolve()

    def onChat(self):
        from customWx.TEMP import chat
        chatFrame = chat.Chat(self, messagePanel=self.scrollPan, size=(280, 50))
        chatFrame.Show()

    def currentModell(self, model):
        self.currentModel = model
        print(model)
        print(model.ModelName)