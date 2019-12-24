import wx
from enum import Enum, auto

WRONG_SIZE = "size attribute should have the following structure <tuple(int, int)> "
WRONG_MODE = "mode attribute must be set to an instance of <enum \'ChoiceMode\'> '"

class ChoiceMode(Enum):
    single = auto()
    multiple = auto()
    notMoreThan = auto()

class LRUCache:
    __items = []
    __maxSize = 1

    def SetMaxSize(self, size):
        self.__maxSize = size
        while len(self) > self.__maxSize:
            del self.__items[0]

    def __len__(self):
        return len(self.__items)

    def Add(self, item):
        if  len(self) >= self.__maxSize:
            del self.__items[0]
        self.__items.append(item)

    def GetValues(self):
        return self.__items

    def __iter__(self):
        return iter(self.__items)


class SettingsSizer(wx.StaticBoxSizer):

    __verticalSpacer = 7
    __horizontalSpacer = 10
    __mode = ChoiceMode.single
    __maxSelectionNumber = 1

    def __init__(self, parent, label, size:tuple, choices, orient=wx.VERTICAL):
        if not isinstance(size, (tuple, list)):
            raise TypeError(WRONG_SIZE)
        self.panel = parent
        self.boxLabel = label
        self.size= size
        self.choices = choices
        self.orient = orient
        super(SettingsSizer, self).__init__(orient=self.orient, parent=self.panel, label=self.boxLabel)
        self.checkBoxes = []
        self.selectedBoxes = []

        self.__checkInit()

    def __checkInit(self):
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
                checkBox = wx.CheckBox(self.panel, label=str(self.choices[currentCell]))
                self.checkBoxes.append(checkBox)
                checkBox.Bind(wx.EVT_CHECKBOX, self.__onCheck)
                boxSizer.Add(checkBox)
                if column + 1 < columnNumber: boxSizer.AddSpacer(self.__horizontalSpacer if state == wx.VERTICAL else self.__verticalSpacer)
            self.Add(boxSizer)
            if row + 1 < rowNumber: self.AddSpacer(self.__verticalSpacer if state == wx.VERTICAL else self.__horizontalSpacer)

    def __onCheck(self, event):
        checkedBox = event.GetEventObject()
        if self.__mode == ChoiceMode.single:
            for box in self.checkBoxes:
                box.SetValue(False)
            checkedBox.SetValue(True)
        if self.__mode == ChoiceMode.notMoreThan:
            if checkedBox in self.selectedBoxes:
                self.selectedBoxes.remove(checkedBox)
            else:
                self.selectedBoxes.append(checkedBox)
            self.__toggleHiddenIfNeeded()

    def __toggleHiddenIfNeeded(self):
        boxesStates = [True if box in self.selectedBoxes else False for box in self.checkBoxes]
        if len(self.selectedBoxes) >= self.__maxSelectionNumber:
            for index, item in enumerate(boxesStates):
                self.checkBoxes[index].Enable(item)
        else:
            for item in self.checkBoxes:
                item.Enable(True)

    def GetValue(self):
        return list(map(lambda box: box.GetLabel(), list(filter(lambda box: box.GetValue() == True, self.checkBoxes))))

    def SetVerticalSpacer(self, number):
        self.__verticalSpacer = number

    def SetHorizontalSpacer(self, number):
        self.__horizontalSpacer = number

    def SetSelectionMode(self, mode:ChoiceMode):
        if not isinstance(mode, ChoiceMode):
            raise TypeError(WRONG_MODE)
        self.__mode = mode

    def SetMaxSelectionNumber(self, number):
        self.__maxSelectionNumber = number