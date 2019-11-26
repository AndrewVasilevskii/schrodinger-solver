import wx

class Settings(wx.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.panel = wx.Panel()
        self.mainSizer = mainSizer = wx.BoxSizer()
        self.panel.SetSizer(mainSizer)

        self.gateDiameterPickerBox = wx.StaticBox(self.panel, label="Gate diameter: ")
        self.gateDiameterPickerSizer = wx.StaticBoxSizer(self.gateDiameterPickerBox, wx.HORIZONTAL)
        self.gateDiameterPicker = wx.StaticText(self.panel, label="fdfdf")
        self.gateDiameterPickerSizer.Add(self.gateDiameterPicker)
        mainSizer.Add(self.gateDiameterPickerBox)