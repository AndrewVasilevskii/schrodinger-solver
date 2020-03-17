import wx
import model as Model
from modelWithParameters import ModelWithParameters

class SettingsModelParameters(wx.Dialog):

    currentModel: Model.Model = None

    def __init__(self, *args, model=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.modelParameters = ModelWithParameters()
        self.CenterOnParent()
        self.parent = args[0]
        # self.SetFocus()
        self.currentModel = model

        self.panel = wx.Panel(self)

        self.horizonalMainSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.verticalMainSizer = wx.BoxSizer(wx.VERTICAL)
        self.horizonalMainSizer.AddSpacer(6)
        self.horizonalMainSizer.Add(self.verticalMainSizer)
        self.gridMainSizer = wx.FlexGridSizer(rows=1, cols=2, hgap=7, vgap=10)
        self.verticalMainSizer.AddSpacer(6)
        self.verticalMainSizer.Add(self.gridMainSizer)
        leftSizer = wx.FlexGridSizer(rows=3, cols=1, vgap=6, hgap=5)
        rightSizer = wx.BoxSizer(wx.VERTICAL)
        self.gridMainSizer.Add(leftSizer)
        self.gridMainSizer.Add(rightSizer)

        if self.currentModel.gateNumber >= Model.GateNumber.twoGates.value or\
                self.currentModel.donorNumber > Model.DonorNumber.zeroDonors.value:
            leftSizer.Add(self.createSpacing(), -1, wx.EXPAND)
        leftSizer.Add(self.createSemiconductorSizer())
        leftSizer.Add(self.createInsulatorSizer())

        rightSizer.Add(self.createGateSizer())

        buttonsGrid = wx.FlexGridSizer(rows=2, cols=1, hgap=5, vgap=5)
        ### OK BUTTON
        okButton = wx.Button(self.panel, label="Ok")
        okButton.SetBackgroundColour(wx.Colour(0, 124, 224))
        okButton.Bind(wx.EVT_BUTTON, self.onOk)
        buttonsGrid.Add(okButton)

        ### CANCEL BUTTON
        cancelButton = wx.Button(self.panel, label="Cancel")
        cancelButton.Bind(wx.EVT_BUTTON, self.onClose)
        buttonsGrid.Add(cancelButton)
        rightSizer.Add(buttonsGrid, 0, wx.ALIGN_RIGHT)

        self.panel.SetSizer(self.horizonalMainSizer)
        self.panel.DoGetBestSize()

    ### GATE
    def createGateSizer(self):
        self.gatesBox = wx.StaticBox(self.panel, label="Gates: ")
        self.gatesBoxSizerHorizontal = wx.StaticBoxSizer(self.gatesBox, wx.HORIZONTAL)
        self.gatesBoxSizerVertical = wx.BoxSizer(wx.VERTICAL)
        self.gatesBoxSizerHorizontal.Add(self.gatesBoxSizerVertical)

        def gatePhysicalDimensions():
            physicalDimensionsBox = wx.StaticBox(self.panel, label="Physical dimensions: ")
            physicalDimensionsBoxSizer = wx.StaticBoxSizer(physicalDimensionsBox, wx.VERTICAL)

            physicalDimensionGridSizer = wx.FlexGridSizer(rows=2, cols=2, hgap=5, vgap=5)
            physicalDimensionsBoxSizer.Add(physicalDimensionGridSizer)
            if self.currentModel.gateShape == Model.GateShape.disc.value:
                diameterText = wx.StaticText(self.panel, label="Diameter (d):", name='d_static')
                diameterCtrl = wx.SpinCtrlDouble(self.panel, value="0.1", size=(70, -1), name='d', inc=0.1, min=0.1)
                diameterCtrl.Bind(wx.EVT_TEXT, self.valueChanged)
                self.modelParameters.SetValueFor(diameterCtrl.GetName(), diameterCtrl.GetValue())
                physicalDimensionGridSizer.Add(diameterText, -1, wx.ALIGN_CENTER_VERTICAL)
                physicalDimensionGridSizer.Add(diameterCtrl, -1, wx.ALIGN_CENTER_VERTICAL)
            else:
                lengthText = wx.StaticText(self.panel, label="Length (a):", name='a_static')
                lengthCtrl = wx.SpinCtrlDouble(self.panel, value="0.1", size=(70, -1), name='a', inc=0.1, min=0.1)
                lengthCtrl.Bind(wx.EVT_TEXT, self.valueChanged)
                self.modelParameters.SetValueFor(lengthCtrl.GetName(), lengthCtrl.GetValue())
                physicalDimensionGridSizer.Add(lengthText, -1, wx.ALIGN_CENTER_VERTICAL)
                physicalDimensionGridSizer.Add(lengthCtrl, -1, wx.ALIGN_CENTER_VERTICAL)

                if self.currentModel.gateShape == Model.GateShape.rectangle.value:
                    widthText = wx.StaticText(self.panel, label="Width (b):", name='b_static')
                    widthCtrl = wx.SpinCtrlDouble(self.panel, value="0.1", size=(70, -1), name='b', inc=0.1, min=0.1)
                    widthCtrl.Bind(wx.EVT_TEXT, self.valueChanged)
                    self.modelParameters.SetValueFor(widthCtrl.GetName(), widthCtrl.GetValue())
                    physicalDimensionGridSizer.Add(widthText, -1, wx.ALIGN_CENTER_VERTICAL)
                    physicalDimensionGridSizer.Add(widthCtrl, -1, wx.ALIGN_CENTER_VERTICAL)

            return physicalDimensionsBoxSizer


        def gatePotentials():
            potentialsBox = wx.StaticBox(self.panel, label="Potentials: ")
            potentialsBoxSizer = wx.StaticBoxSizer(potentialsBox, wx.VERTICAL)
            potentialsGridSizer = wx.FlexGridSizer(rows=4, cols=1, vgap=5, hgap=5)
            potentialsBoxSizer.Add(potentialsGridSizer)

            if self.currentModel.gateNumber == Model.GateNumber.oneGate.value:
                potentialF0Text = wx.StaticText(self.panel)
                potentialF0Text.SetLabelMarkup(u"Shutter potential (\u03A6"
                                               u"<span size='xx-small'>0</span>"
                                               u")")
                f0GridSizer = wx.FlexGridSizer(rows=1, cols=2, vgap=0, hgap=10)
                f0CtrlText = wx.StaticText(self.panel, name='F0_static')
                f0CtrlText.SetLabelMarkup(u"\u03A6<span size='xx-small'>0</span>:")
                f0Ctrl = wx.SpinCtrlDouble(self.panel, value="0", size=(70, -1), name='F0', inc=0.1, min=0)
                f0Ctrl.Bind(wx.EVT_TEXT, self.valueChanged)
                self.modelParameters.SetValueFor(f0Ctrl.GetName(), f0Ctrl.GetValue())
                f0GridSizer.Add(f0CtrlText, -1, wx.ALIGN_CENTER_VERTICAL)
                f0GridSizer.Add(f0Ctrl, -1, wx.ALIGN_CENTER_VERTICAL)

                potentialsGridSizer.Add(potentialF0Text)
                potentialsGridSizer.Add(f0GridSizer)

            else:
                potentialFAText = wx.StaticText(self.panel)
                potentialFAText.SetLabelMarkup(u"Shutters (A) potentials ("
                                               u"\u03A6<span size='xx-small'>1</span>,"
                                               u"\u03A6<span size='xx-small'>2</span>"
                                               u")")
                fAGridSizer = wx.FlexGridSizer(rows=1, cols=4, vgap=0, hgap=5)
                fA1CtrlText = wx.StaticText(self.panel, name='F1_static')
                fA1CtrlText.SetLabelMarkup(u"\u03A6<span size='xx-small'>1</span>:")
                fA1Ctrl = wx.SpinCtrlDouble(self.panel, value="0", size=(70, -1), name='F1', inc=0.1, min=0)
                fA1Ctrl.Bind(wx.EVT_TEXT, self.valueChanged)
                self.modelParameters.SetValueFor(fA1Ctrl.GetName(), fA1Ctrl.GetValue())
                fA2CtrlText = wx.StaticText(self.panel, name='F2_static')
                fA2CtrlText.SetLabelMarkup(u"\u03A6<span size='xx-small'>2</span>:")
                fA2Ctrl = wx.SpinCtrlDouble(self.panel, value="0", size=(70, -1), name='F2', inc=0.1, min=0)
                fA2Ctrl.Bind(wx.EVT_TEXT, self.valueChanged)
                self.modelParameters.SetValueFor(fA2Ctrl.GetName(), fA2Ctrl.GetValue())

                fAGridSizer.Add(fA1CtrlText, -1, wx.ALIGN_CENTER_VERTICAL)
                fAGridSizer.Add(fA1Ctrl, -1, wx.ALIGN_CENTER_VERTICAL)
                fAGridSizer.Add(fA2CtrlText, -1, wx.ALIGN_CENTER_VERTICAL)
                fAGridSizer.Add(fA2Ctrl, -1, wx.ALIGN_CENTER_VERTICAL)

                potentialsGridSizer.Add(potentialFAText)
                potentialsGridSizer.Add(fAGridSizer)

                if self.currentModel.gateNumber == Model.GateNumber.threeGates.value:
                    potentialFjText = wx.StaticText(self.panel)
                    potentialFjText.SetLabelMarkup(u"Shutter (J) potential (\u03A6"
                                                   u"<span size='xx-small'>j</span>"
                                                   u")")
                    fjGridSizer = wx.FlexGridSizer(rows=1, cols=2, vgap=0, hgap=10)
                    fjCtrlText = wx.StaticText(self.panel, name='FJ_static')
                    fjCtrlText.SetLabelMarkup(u"\u03A6<span size='xx-small'>j</span>:")
                    fjCtrl = wx.SpinCtrlDouble(self.panel, value="0", size=(70, -1), name='FJ', inc=0.1, min=0)
                    fjCtrl.Bind(wx.EVT_TEXT, self.valueChanged)
                    self.modelParameters.SetValueFor(fjCtrl.GetName(), fjCtrl.GetValue())
                    fjGridSizer.Add(fjCtrlText, -1, wx.ALIGN_CENTER_VERTICAL)
                    fjGridSizer.Add(fjCtrl, -1, wx.ALIGN_CENTER_VERTICAL)

                    potentialsGridSizer.Add(potentialFjText)
                    potentialsGridSizer.Add(fjGridSizer)

            return potentialsBoxSizer

        def gateDielectricConstant():
            gateDielectricGrid = wx.FlexGridSizer(2)
            dielectricConstantText = wx.StaticText(self.panel, name='E3_static')
            dielectricConstantText.SetLabelMarkup(u"The dielectric constant (\uA72B"
                                                  u"<span size='xx-small'>3</span>"
                                                  u"):")
            dielectricConstantCtrl = wx.SpinCtrlDouble(self.panel, value="1", size=(70, -1), name='E3', inc=0.1, min=1)
            dielectricConstantCtrl.Bind(wx.EVT_TEXT, self.valueChanged)
            self.modelParameters.SetValueFor(dielectricConstantCtrl.GetName(), dielectricConstantCtrl.GetValue())
            gateDielectricGrid.Add(dielectricConstantText, -1, wx.ALIGN_CENTER_VERTICAL)
            gateDielectricGrid.Add(dielectricConstantCtrl, -1, wx.ALIGN_CENTER_VERTICAL)
            return gateDielectricGrid

        self.gatesBoxSizerVertical.Add(gatePhysicalDimensions())
        self.gatesBoxSizerVertical.Add(gatePotentials())
        self.gatesBoxSizerVertical.Add(gateDielectricConstant())

        return self.gatesBoxSizerHorizontal

    ### SPACING
    def createSpacing(self):
        self.spacingBox = wx.StaticBox(self.panel)
        self.spacingBoxSizerHorizontal = wx.StaticBoxSizer(self.spacingBox, wx.HORIZONTAL)
        self.spacingBoxSizerVertical = wx.BoxSizer(wx.VERTICAL)
        self.spacingBoxSizerHorizontal.Add(self.spacingBoxSizerVertical)

        self.spacingGrid = wx.FlexGridSizer(rows=4, cols=1, vgap=5, hgap=0)
        self.spacingBoxSizerVertical.Add(self.spacingGrid)
        if self.currentModel.gateNumber >= Model.GateNumber.twoGates.value or\
                self.currentModel.donorNumber == Model.DonorNumber.twoDonors.value:
            spacingRText = wx.StaticText(self.panel, label="Distance (R) between donor or the\n"
                                                           "center of the gates")

            spacingRGridSizer = wx.FlexGridSizer(rows=1, cols=2, vgap=0, hgap=5)
            spacingRCtrlText = wx.StaticText(self.panel, label="R:", name='R_static')
            spacingRCtrl =  wx.SpinCtrlDouble(self.panel, value="0.1", size=(70,-1), name='R', inc=0.1, min=0.1)
            spacingRCtrl.Bind(wx.EVT_TEXT, self.valueChanged)
            self.modelParameters.SetValueFor(spacingRCtrl.GetName(), spacingRCtrl.GetValue())

            spacingRGridSizer.Add(spacingRCtrlText, -1, wx.ALIGN_CENTER_VERTICAL)
            spacingRGridSizer.Add(spacingRCtrl, -1, wx.ALIGN_CENTER_VERTICAL)

            self.spacingGrid.Add(spacingRText)
            self.spacingGrid.Add(spacingRGridSizer)

        if self.currentModel.donorNumber == Model.DonorNumber.oneDonor.value:
            spacingZ0Text = wx.StaticText(self.panel)
            spacingZ0Text.SetLabelMarkup("Distance (z"
                                         "<span size='xx-small'>0</span>"
                                         ") from donor to\n"
                                         "semiconductor surface")
            spacingZ0GridSizer = wx.FlexGridSizer(rows=1, cols=2, vgap=0, hgap=5)

            spacingZ0CtrlText = wx.StaticText(self.panel, name='z0_static')

            spacingZ0CtrlText.SetLabelMarkup("z<span size='xx-small'>0</span>:")
            spacingZ0Ctrl = wx.SpinCtrlDouble(self.panel, value="0.1", size=(70,-1), name='z0', inc=0.1, min=0.1)
            spacingZ0Ctrl.Bind(wx.EVT_TEXT, self.valueChanged)
            self.modelParameters.SetValueFor(spacingZ0Ctrl.GetName(), spacingZ0Ctrl.GetValue())
            spacingZ0GridSizer.Add(spacingZ0CtrlText, -1, wx.ALIGN_CENTER_VERTICAL)
            spacingZ0GridSizer.Add(spacingZ0Ctrl, -1, wx.ALIGN_CENTER_VERTICAL)

            self.spacingGrid.Add(spacingZ0Text)
            self.spacingGrid.Add(spacingZ0GridSizer)

        if self.currentModel.donorNumber == Model.DonorNumber.twoDonors.value:
            spacingZ12Text = wx.StaticText(self.panel)
            spacingZ12Text.SetLabelMarkup("Distance (z"
                                          "<span size='xx-small'>1</span>, "
                                          "z<span size='xx-small'>2</span>"
                                          ") from donors to\n"
                                          "semiconductor surface")

            spacingZ12GridSizer = wx.FlexGridSizer(rows=1, cols=4, vgap=0, hgap=5)

            spacingZ1CtrlText = wx.StaticText(self.panel, name='z1_static')
            spacingZ1CtrlText.SetLabelMarkup("z<span size='xx-small'>1</span>:")
            spacingZ1Ctrl = wx.SpinCtrlDouble(self.panel, value="0.1", size=(70, -1), name='z1', inc=0.1, min=0.1)
            spacingZ1Ctrl.Bind(wx.EVT_TEXT, self.valueChanged)
            self.modelParameters.SetValueFor(spacingZ1Ctrl.GetName(), spacingZ1Ctrl.GetValue())
            spacingZ2CtrlText = wx.StaticText(self.panel, name='z2_static')
            spacingZ2CtrlText.SetLabelMarkup("z<span size='xx-small'>2</span>:")
            spacingZ2Ctrl = wx.SpinCtrlDouble(self.panel, value="0.1", size=(70, -1), name='z2', inc=0.1, min=0.1)
            spacingZ2Ctrl.Bind(wx.EVT_TEXT, self.valueChanged)
            self.modelParameters.SetValueFor(spacingZ2Ctrl.GetName(), spacingZ2Ctrl.GetValue())

            spacingZ12GridSizer.Add(spacingZ1CtrlText, -1, wx.ALIGN_CENTER_VERTICAL)
            spacingZ12GridSizer.Add(spacingZ1Ctrl, -1, wx.ALIGN_CENTER_VERTICAL)

            spacingZ12GridSizer.Add(spacingZ2CtrlText, -1, wx.ALIGN_CENTER_VERTICAL)
            spacingZ12GridSizer.Add(spacingZ2Ctrl, -1, wx.ALIGN_CENTER_VERTICAL)

            self.spacingGrid.Add(spacingZ12Text)
            self.spacingGrid.Add(spacingZ12GridSizer)

        return self.spacingBoxSizerHorizontal

    ### SEMICONDUCTOR
    def createSemiconductorSizer(self):
        self.semiconductorBox = wx.StaticBox(self.panel, label="Semiconductor: ")
        self.semiconductorBoxSizerHorizontal = wx.StaticBoxSizer(self.semiconductorBox, wx.HORIZONTAL)
        self.semiconductorBoxSizerVertical = wx.BoxSizer(wx.VERTICAL)
        self.semiconductorBoxSizerHorizontal.Add(self.semiconductorBoxSizerVertical)

        self.semiconductorGrid = wx.FlexGridSizer(2)
        self.semiconductorBoxSizerVertical.Add(self.semiconductorGrid)
        dielectricConstantText = wx.StaticText(self.panel, name='E1_static')
        dielectricConstantText.SetLabelMarkup(u"The dielectric constant (\uA72B"
                                              u"<span size='xx-small'>1</span>"
                                              u"):")
        dielectricConstantCtrl = wx.SpinCtrlDouble(self.panel, value="1", size=(70,-1), name='E1', inc=0.1, min=1)
        dielectricConstantCtrl.Bind(wx.EVT_TEXT, self.valueChanged)
        self.modelParameters.SetValueFor(dielectricConstantCtrl.GetName(), dielectricConstantCtrl.GetValue())
        self.semiconductorGrid.Add(dielectricConstantText, -1, wx.ALIGN_CENTER_VERTICAL)
        self.semiconductorGrid.Add(dielectricConstantCtrl, -1, wx.ALIGN_CENTER_VERTICAL)

        return self.semiconductorBoxSizerHorizontal

    ### INSULATOR
    def createInsulatorSizer(self):
        self.insulatorBox = wx.StaticBox(self.panel, label="Insulator: ")
        self.insulatorBoxSizerHorizontal = wx.StaticBoxSizer(self.insulatorBox, wx.HORIZONTAL)
        self.insulatorBoxSizerVertical = wx.BoxSizer(wx.VERTICAL)
        self.insulatorBoxSizerHorizontal.Add(self.insulatorBoxSizerVertical)

        self.insulatorGrid = wx.FlexGridSizer(rows=2, cols=2, vgap=5, hgap=0)
        self.insulatorBoxSizerVertical.Add(self.insulatorGrid)
        self.toxText = wx.StaticText(self.panel, name='tox_static')
        self.toxText.SetLabelMarkup("Depth (t"
                                      "<span size='xx-small'>ox</span>"
                                      "):")
        self.toxCtrl = wx.SpinCtrlDouble(self.panel, value="0", size=(70,-1), name='tox', inc=0.1, min=0)
        self.toxCtrl.Bind(wx.EVT_TEXT, self.valueChanged)
        self.modelParameters.SetValueFor(self.toxCtrl.GetName(), self.toxCtrl.GetValue())
        self.insulatorGrid.Add(self.toxText,-1,wx.ALIGN_CENTER_VERTICAL)
        self.insulatorGrid.Add(self.toxCtrl)

        dielectricConstantText = wx.StaticText(self.panel, name="E2_static")
        dielectricConstantText.SetLabelMarkup(u"The dielectric constant (\uA72B"
                                                   u"<span size='xx-small'>2</span>"
                                                   u"):")
        dielectricConstantCtrl = wx.SpinCtrlDouble(self.panel, value="1", size=(70,-1), name='E2', inc=0.1, min=1)
        dielectricConstantCtrl.Bind(wx.EVT_TEXT, self.valueChanged)
        self.modelParameters.SetValueFor(dielectricConstantCtrl.GetName(), dielectricConstantCtrl.GetValue())
        self.insulatorGrid.Add(dielectricConstantText)
        self.insulatorGrid.Add(dielectricConstantCtrl)

        return self.insulatorBoxSizerHorizontal

    def createItem(self, staticText, value, name, minBoard=0):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(wx.StaticText(self.panel, label=staticText, name=name + "_static"))
        sizer.AddSpacer(10)
        inputFrame = wx.TextCtrl(self.panel, size=(150, -1), value=str(value), name=name)
        inputFrame.Bind(wx.EVT_TEXT, self.valueChanged)
        sizer.Add(inputFrame)
        return sizer

    def valueChanged(self, event):
        fieldName = event.GetEventObject().GetName()
        print(fieldName)
        fieldCapacity = event.GetString()
        try:
            fieldCapacity = float(fieldCapacity)
            self.FindWindowByName(fieldName + '_static').SetForegroundColour(wx.BLACK)
        except:
            self.FindWindowByName(fieldName + '_static').SetForegroundColour(wx.RED)

        self.modelParameters.__setattr__(fieldName, fieldCapacity)

    def onOk(self, event=None):
        print(self.modelParameters)
        self.currentModel.parameters = self.modelParameters
        # self.parent.currentModell(model)
        self.EndModal(0)

    def onClose(self, event):
        self.Close()