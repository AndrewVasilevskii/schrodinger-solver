import wx
import wx.lib.newevent

radioBox_event = wx.NewEventType()
EVT_RADIOBOX = wx.PyEventBinder(radioBox_event, 1)

WRONG_SIZE = "size attribute should have the following structure <tuple(int, int)> "

class RadioBoxEvent(wx.PyCommandEvent):
    def __init__(self, evtType, id):
        wx.PyCommandEvent.__init__(self, evtType, id)
        __value = None

    def SetValue(self, value):
        self.__value = value

    def GetValue(self):
        return self.__value

class RadioBox(wx.StaticBoxSizer):

    __verticalSpacer = 7
    __horizontalSpacer = 10
    __left_border = 10
    isEnabled = True

    def __init__(self, parent, label, size:tuple, choices, orient=wx.VERTICAL):
        if not isinstance(size, (tuple, list)):
            raise TypeError(WRONG_SIZE)
        self.panel = parent
        self.boxLabel = label
        self.size= size
        self.choices = choices
        self.orient = orient
        self.staticBox = wx.StaticBox(parent, label=label, name="staticBox")
        super().__init__(self.staticBox, orient=self.orient)
        self.radioButtons = []
        self.radioButtonsByName = {}
        self.selectedbutton = None
        self.__ID = wx.NewId()

    def create(self):
        self.__radioBoxInit()

    def __radioBoxInit(self):
        columnNumber = self.size[0]
        rowNumber = self.size[1]
        for row in range(rowNumber):
            columnBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
            columnBoxSizer.AddSpacer(self.__left_border)
            for column in range(columnNumber):
                currentCell = row*columnNumber+column
                if currentCell >= len(self.choices):
                    break
                if column == 0 and row == 0:
                    radioButton = wx.RadioButton(self.panel, label=str(self.choices[currentCell]), style=wx.RB_GROUP)
                    self.selectedbutton = radioButton
                    radioButton.SetValue(True)
                else:
                    radioButton = wx.RadioButton(self.panel,label=str(self.choices[currentCell]))
                self.radioButtons.append(radioButton)
                self.radioButtonsByName[str(self.choices[currentCell])] = currentCell
                radioButton.Bind(wx.EVT_RADIOBUTTON, self.__onRadioButton)
                columnBoxSizer.Add(radioButton)
                if column + 1 < columnNumber: columnBoxSizer.AddSpacer(self.__horizontalSpacer)
            self.Add(columnBoxSizer)
            if row + 1 < rowNumber: self.AddSpacer(self.__verticalSpacer)

    def __onRadioButton(self, event=None, machinePush=None):
        if machinePush != None:
            label = str(machinePush)
        else:
            self.selectedbutton = event.GetEventObject()
            label = self.selectedbutton.GetLabel()
        event = RadioBoxEvent(radioBox_event, self.__ID)
        event.SetValue(label)
        wx.PostEvent(self.panel, event)

    def GetSelection(self):
        return self.selectedbutton.GetLabel()

    def GetSelectionIndex(self):
        return self.radioButtons.index(self.selectedbutton)

    def SetSelectionByName(self, name):
        buttonIndex = self.radioButtonsByName[name]
        self.SetSelection(buttonIndex)

    def SetSelection(self, n):
        self.radioButtons[n].SetValue(True)
        self.selectedbutton = self.radioButtons[n]
        self.__onRadioButton(machinePush=n)

    def EnableItem(self, n, bool):
        self.radioButtons[n].Enable(bool)
        if bool == False:
            if self.selectedbutton == self.radioButtons[n]:
                if len(self.radioButtons)-1 == n:
                    self.SetSelection(n-1)
                else:
                    self.SetSelection(n+1)

    def IsItemEnabled(self, n):
        return True if self.radioButtons[n].IsEnabled() else False

    def Enable(self, bool):
        self.isEnabled = bool
        for but in self.radioButtons: but.Enable(bool)

    def IsEnabled(self):
        return self.isEnabled

    def SetVerticalSpacer(self, number):
        self.__verticalSpacer = number

    def SetHorizontalSpacer(self, number):
        self.__horizontalSpacer = number

    def SetLeftBorder(self, number):
        self.__left_border = number

    def GetId(self):
        return self.__ID