import wx
import attributedTextField as atf
import settingssizer as SS

class Settings(wx.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.panel = wx.Panel(self)
        self.mainSizer = mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.panel.SetSizer(mainSizer)
        mainSizerr = wx.BoxSizer(wx.VERTICAL)
        # self.donorBox = wx.StaticBox(self.panel, label="Number of donors: ")
        # self.donorBoxSizer = wx.StaticBoxSizer(self.donorBox)
        self.donor = SS.SettingsSizer(self.panel, label="Number of donors: ", size=(1,3), choices=("0 donors", "1 donor", "2 donors"))
        self.gate = SS.SettingsSizer(self.panel, label="Number of gates: ", size=(1,4), choices=("0 gates", "1 gate", "2 gates", "3 gates"))
        self.gateForm = SS.SettingsSizer(self.panel, label="Gate form: ", size=(1,3), choices=("disc", "strip", "rectangle"))
        self.electron = SS.SettingsSizer(self.panel , label="Number of electrons: ", size=(1,2), choices=("1 electron", "2 electrons"))
        self.groundedShield= SS.SettingsSizer(self.panel, label="Presence of grounded shield: ", size=(1,2), choices=("yes","missing"))

        # self.donorBoxSizer.Add(self.donor)
        mainSizerr.Add(self.donor)
        mainSizerr.Add(self.gate)
        mainSizerr.Add(self.gateForm)
        mainSizerr.Add(self.electron)
        mainSizerr.Add(self.groundedShield)

        mainSizer.Add(mainSizerr)
        comboSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.AddSpacer(50)
        mainSizer.Add(comboSizer)

        donorSizer = wx.BoxSizer(wx.HORIZONTAL)
        donorText = wx.StaticText(self.panel, label="Number of donors:  ")
        donorCombo = wx.ComboBox(self.panel,value="",choices=("0 donors", "1 donor", "2 donors"))
        donorSizer.Add(donorText)
        donorSizer.Add(donorCombo)

        gateSizer = wx.BoxSizer(wx.HORIZONTAL)
        gateText = wx.StaticText(self.panel, label="Number of gates:  ")
        gateCombo = wx.ComboBox(self.panel, value="", choices=("0 gates", "1 gate", "2 gates", "3 gates"))
        gateSizer.Add(gateText)
        gateSizer.Add(gateCombo)

        gateFormSizer = wx.BoxSizer(wx.HORIZONTAL)
        gateFormText = wx.StaticText(self.panel, label="Gate form:  ")
        gateFormCombo = wx.ComboBox(self.panel, value="", choices=("disc", "strip", "rectangle"))
        gateFormSizer.Add(gateFormText)
        gateFormSizer.Add(gateFormCombo)

        electronSizer = wx.BoxSizer(wx.HORIZONTAL)
        electronText = wx.StaticText(self.panel, label="Number of electrons:   ")
        electronCombo = wx.ComboBox(self.panel, value="", choices=("1 electron", "2 electrons"))
        electronSizer.Add(electronText)
        electronSizer.Add(electronCombo)

        shieldSizer = wx.BoxSizer(wx.HORIZONTAL)
        shieldText = wx.StaticText(self.panel, label="Presence of grounded shield:   ")
        shieldCombo = wx.ComboBox(self.panel, value="", choices=("yes", "missing"))
        shieldSizer.Add(shieldText)
        shieldSizer.Add(shieldCombo)

        comboSizer.Add(donorSizer)
        comboSizer.Add(gateSizer)
        comboSizer.Add(gateFormSizer)
        comboSizer.Add(electronSizer)
        comboSizer.Add(shieldSizer)
        #
        # self.gateDiameterPickerBox = wx.StaticBox(self.panel, label="--(Gate diameter)--: ")
        # self.gateDiameterPickerSizer = wx.StaticBoxSizer(self.gateDiameterPickerBox, wx.HORIZONTAL)
        # self.gateDiameterPicker = wx.SpinCtrlDouble(self.panel, min=0.1, initial=0.1, inc=0.1)
        # self.gateDiameterPickerSizer.Add(self.gateDiameterPicker)
        # k_super = atf.AttributedTextField(self.panel, baseText="t", indexText="01", indexStyle=atf.IndexStyle.super)
        # k_sub = atf.AttributedTextField(self.panel, baseText="t", indexText="01", indexStyle=atf.IndexStyle.sub)
        # k_none = atf.AttributedTextField(self.panel, baseText="t")
        # self.gateDiameterPickerSizer.Add(k_super)
        # self.gateDiameterPickerSizer.AddSpacer(4)
        # self.gateDiameterPickerSizer.Add(k_sub)
        # self.gateDiameterPickerSizer.AddSpacer(4)
        # self.gateDiameterPickerSizer.Add(k_none)
        #
        #
        # mainSizer.Add(self.gateDiameterPickerSizer)
