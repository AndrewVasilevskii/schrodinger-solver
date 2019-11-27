import wx
import wx.richtext as rt
class Settings(wx.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.panel = wx.Panel(self)
        self.mainSizer = mainSizer = wx.BoxSizer()
        self.panel.SetSizer(mainSizer)


        self.gateDiameterPickerBox = wx.StaticBox(self.panel, label="--(Gate diameter)--: ")
        self.gateDiameterPickerSizer = wx.StaticBoxSizer(self.gateDiameterPickerBox, wx.HORIZONTAL)
        self.gateDiameterPicker = wx.SpinCtrlDouble(self.panel, min=0.1, initial=0.1, inc=0.1)
        self.gateDiameterPickerSizer.Add(self.gateDiameterPicker)
        k = rt.RichTextCtrl(self.panel,style=wx.TE_READONLY|wx.NO_BORDER)
        k.SetBackgroundColour(self.panel.GetBackgroundColour())
        k.AppendText("HOHO")

        k.SetMinSize((100,100))

        self.gateDiameterPickerSizer.Add(k)


        mainSizer.Add(self.gateDiameterPickerSizer)