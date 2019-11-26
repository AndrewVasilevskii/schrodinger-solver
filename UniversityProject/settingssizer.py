import wx
from enum import Enum, auto
WRONG_SIZE = "size attribute should have the following structure <tuple(int, int)> "
WRONG_MODE = "mode attribute must be set to an instance of <enum \'ChoiceMode\'> '"

class ChoiceMode(Enum):
    single = auto()
    multiple = auto()
    notMoreThan = auto()

class SettingsSizer(wx.StaticBoxSizer):

    def __init__(self, parent, label, size:tuple, choices, orient, mode:ChoiceMode=ChoiceMode.single):
        if not isinstance(size, (tuple, list)):
            raise TypeError(WRONG_SIZE)
        if not isinstance(mode, ChoiceMode):
            raise TypeError(WRONG_MODE)
        self.panel = parent
        self.boxLabel = label
        self.size= size
        self.choices = choices
        self.mode = mode
        self.orient = orient
        super(SettingsSizer, self).__init__(orient=self.orient, parent=self.panel, label=self.boxLabel)
        self.checkBoxes = []
        self.selectedBoxes = []

        self.checkInit()


    def checkInit(self):
        if self.orient == wx.VERTICAL:
            columnNumber= self.size[0]
            rowNumber = self.size[1]
            state = wx.HORIZONTAL
        else:
            columnNumber = self.size[1]
            rowNumber = self.size[0]
            state = wx.VERTICAL

        for row in range(rowNumber):
            boxSizer = wx.BoxSizer(state)
            for column in range(columnNumber):
                currentCell = row * columnNumber + column
                if currentCell >= len(self.choices):
                    break
                checkBox = wx.CheckBox(self.panel, label=self.choices[currentCell])
                self.checkBoxes.append(checkBox)
                checkBox.Bind(wx.EVT_CHECKBOX, self.onCheck)
                boxSizer.Add(checkBox)
            self.Add(boxSizer)
        # columnNumber = self.size[0]
        # rowNumber = self.size[1]
        # if self.orient == wx.VERTICAL:
        #     for row in range(rowNumber):
        #         boxSizer = wx.BoxSizer(wx.HORIZONTAL)
        #         for column in range(columnNumber):
        #             currentCell = row*columnNumber+column
        #             if currentCell >= len(self.choices):
        #                 break
        #             checkBox = wx.CheckBox(self.panel, label=self.choices[currentCell])
        #             self.checkBoxes.append(checkBox)
        #             checkBox.Bind(wx.EVT_CHECKBOX, self.onCheck)
        #             boxSizer.Add(checkBox)
        #         self.Add(boxSizer)
        # else:
        #     print("HERE")
        #     for column in range(columnNumber):
        #         boxSizer = wx.BoxSizer(wx.VERTICAL)
        #         for row in range(rowNumber):
        #             currentCell = column * rowNumber + row
        #             if currentCell >= len(self.choices):
        #                 break
        #             checkBox = wx.CheckBox(self.panel, label=self.choices[currentCell])
        #             self.checkBoxes.append(checkBox)
        #             checkBox.Bind(wx.EVT_CHECKBOX, self.onCheck)
        #             boxSizer.Add(checkBox)
        #         self.Add(boxSizer)



    def onCheck(self, event):
        checkedBox = event.GetEventObject()
        if self.mode == ChoiceMode.single:
            for box in self.checkBoxes:
                box.SetValue(False)
            checkedBox.SetValue(True)
        if self.mode == ChoiceMode.notMoreThan:


    def GetValue(self):
        return list(map(lambda box: box.GetLabel(), list(filter(lambda box: box.GetValue() == True, self.checkBoxes))))