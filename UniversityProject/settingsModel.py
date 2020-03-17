import wx
from customWx import radioBox as rb
from model import *

class SettingsModel(wx.Dialog):

    currentModel: Model = None
    innerModel: Model = None

    def __init__(self, *args, model=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.currentModel = model

        self.CenterOnParent()
        self.parent = args[0]
        self.SetFocus()
        self.panelSizer = wx.BoxSizer(wx.VERTICAL)

        self.panel = wx.Panel(self)
        self.horizonalMainSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.leftVerticalSizer = wx.BoxSizer(wx.VERTICAL)
        self.leftVerticalSizer.AddSpacer(5)
        self.rightVerticalSizer = wx.BoxSizer(wx.VERTICAL)
        self.rightVerticalSizer.AddSpacer(5)

        ## DONORS
        self.donorsBox = wx.StaticBox(self.panel, label="Donors: ")
        self.donorsBoxSizer = wx.StaticBoxSizer(self.donorsBox)
        self.donors = rb.RadioBox(self.panel, label="Number: ", size=(1,3), choices=range(3))
        self.Bind(rb.EVT_RADIOBOX, self.onDonor, self.donors)
        self.donors.create()
        self.donorsBoxSizer.Add(self.donors)

        self.rightVerticalSizer.Add(self.donorsBoxSizer)
        self.rightVerticalSizer.AddSpacer(30)

        ## GATES
        self.gatesBox = wx.StaticBox(self.panel, label="Gates: ")
        self.gatesBoxSizer = wx.StaticBoxSizer(self.gatesBox, wx.HORIZONTAL)
        self.gates = rb.RadioBox(self.panel, label="Number: " , size=(1,4), choices=range(4))
        self.Bind(rb.EVT_RADIOBOX, self.onGate, self.gates)
        self.gates.create()
        self.gateShape = rb.RadioBox(self.panel, label="Shape: ", size=(1,3), choices=("Disc", "Strip", "Rectangle"))
        self.gateShape.create()
        self.gatesBoxSizer.Add(self.gates)
        self.gatesBoxSizer.Add(self.gateShape)

        self.leftVerticalSizer.Add(self.gatesBoxSizer,1, wx.EXPAND)


        electronShieldGrid = wx.FlexGridSizer(rows=2, cols=1, vgap=2, hgap=0)

        ## ELECTRONS
        electronSizer = wx.BoxSizer(wx.HORIZONTAL)
        electronText = wx.StaticText(self.panel, label="Number of electrons:   ")
        self.electrons = wx.ComboBox(self.panel, value="", choices=("1", "2"))
        electronSizer.Add(electronText, 1, wx.ALIGN_CENTER_VERTICAL)
        electronSizer.Add(self.electrons)

        electronShieldGrid.Add(electronSizer)

        ## GROUNDED SHIELD
        self.groundedShield = wx.CheckBox(self.panel, label="Enable Grounded Shield")
        electronShieldGrid.Add(self.groundedShield)
        self.leftVerticalSizer.Add(electronShieldGrid)
        self.leftVerticalSizer.AddSpacer(5)


        buttonsGrid = wx.FlexGridSizer(rows=2, cols=1, hgap=0, vgap=5)

        ### OK BUTTON
        okButton = wx.Button(self.panel, label="Ok")
        okButton.SetBackgroundColour(wx.Colour(0,124,224))
        okButton.Bind(wx.EVT_BUTTON, self.onOk)
        buttonsGrid.Add(okButton)

        ### CANCEL BUTTON
        cancelButton = wx.Button(self.panel, label="Cancel")
        cancelButton.Bind(wx.EVT_BUTTON, self.onClose)
        buttonsGrid.Add(cancelButton)
        self.rightVerticalSizer.Add(buttonsGrid, 0, wx.ALIGN_RIGHT)
        ## RULE MESSAGE PANEL
        self.rulePanel = wx.Panel(self, style=wx.SUNKEN_BORDER)
        ruleText = wx.StaticText(self.rulePanel)
        ruleText.SetLabelMarkup("<small><span color='rgb(195,0,0)'>"
                                "* 0 donors and 0 gates impossible\n"
                                "* with 0 gates, the gate shape is not used\n"
                                "* with 0 donors, the 'Strip' shape is not available\n"
                                "* with 1 donor, the number of gates is not more than 1</span></small>")
        ruleTextSizer = wx.BoxSizer()
        ruleTextSizer.Add(ruleText)

        self.rulePanelSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.rulePanelSizer.AddSpacer(10)
        self.rulePanelSizer.Add(self.rulePanel, 1, wx.EXPAND)
        self.rulePanelSizer.AddSpacer(10)

        ## Set window sizers with horizontal spacing
        self.horizonalMainSizer.AddSpacer(10)
        self.horizonalMainSizer.Add(self.leftVerticalSizer)
        self.horizonalMainSizer.AddSpacer(5)
        self.horizonalMainSizer.Add(self.rightVerticalSizer)

        self.panel.SetSizer(self.horizonalMainSizer)
        self.rulePanel.SetSizer(ruleTextSizer)

        self.panelSizer.Add(self.panel)
        self.panelSizer.AddSpacer(15)
        self.panelSizer.Add(self.rulePanelSizer)

        self.SetSizer(self.panelSizer)
        self.setupModel(model)

    def onOk(self, event=None):
        donorNumber = self.donors.GetSelection()
        gateNumber = self.gates.GetSelection()
        gateShape = self.gateShape.GetSelection()
        electronNumberIndex = self.electrons.GetSelection()
        groundedShield = self.groundedShield.GetValue()
        self.innerModel = Model(DonorNumber(donorNumber), GateNumber(gateNumber), GateShape(gateShape), Electron(electronNumberIndex), GroundedShield(groundedShield))
        if self.innerModel == self.currentModel:
            self.parent.currentModell(self.currentModel)
        else:
            self.parent.currentModell(self.innerModel)
        self.EndModal(0)

    def onClose(self, event):
        self.Close()

    def onDonor(self, event):
        self.__ruleManager("donor", event.GetValue())

    def onGate(self, event):
        self.__ruleManager("gate", event.GetValue())

    def __ruleManager(self, box, value):
        if box == "donor":
            if value == "0":
                self.gates.Enable(True)
                self.gates.EnableItem(0, False)
                self.gateShape.EnableItem(1, False)
            else:
                if value == "1":
                    self.gates.Enable(True)
                    self.gates.EnableItem(2, False)
                    self.gates.EnableItem(3, False)
                    if self.gates.GetSelectionIndex() > 1:
                        self.gates.SetSelection(1)
                else:
                    self.gates.Enable(True)
                if self.gateShape.IsItemEnabled(0):
                    self.gateShape.EnableItem(1, True)
        elif box == "gate":
            if value == "0":
                self.donors.EnableItem(0, False)
                self.gateShape.Enable(False)
            else:
                self.donors.EnableItem(0, True)
                if self.donors.GetSelection() == "0":
                    self.gateShape.EnableItem(0, True)
                    self.gateShape.EnableItem(2, True)
                else:
                    self.gateShape.Enable(True)

    def setupModel(self, model:Model):
        self.donors.SetSelectionByName(model.donorNumber)
        self.gates.SetSelectionByName(model.gateNumber)
        self.gateShape.SetSelectionByName(model.gateShape)
        self.electrons.SetSelection(model.electronNumberIndex)
        self.groundedShield.SetValue(model.groundedShield)