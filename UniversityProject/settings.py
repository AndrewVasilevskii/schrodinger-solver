import wx
import attributedTextField as atf

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
        k_super = atf.AttributedTextField(self.panel, baseText="t", indexText="01", indexStyle=atf.IndexStyle.super)
        k_sub = atf.AttributedTextField(self.panel, baseText="t", indexText="01", indexStyle=atf.IndexStyle.sub)
        k_none = atf.AttributedTextField(self.panel, baseText="t")
        self.gateDiameterPickerSizer.Add(k_super)
        self.gateDiameterPickerSizer.AddSpacer(4)
        self.gateDiameterPickerSizer.Add(k_sub)
        self.gateDiameterPickerSizer.AddSpacer(4)
        self.gateDiameterPickerSizer.Add(k_none)


        mainSizer.Add(self.gateDiameterPickerSizer)