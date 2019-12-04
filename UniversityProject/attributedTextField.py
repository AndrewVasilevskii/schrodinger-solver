import wx.richtext as rt
import wx
from enum import Enum, auto

BORDER = 10

class IndexStyle(Enum):
    super = auto()
    sub = auto()
    none = auto()

class AttributedTextField(rt.RichTextCtrl):

    def __init__(self, *args, baseText, indexText="", indexStyle:IndexStyle=IndexStyle.none, **kwargs):
        self.parent = args[0]
        self.baseText = baseText
        self.indexText = indexText
        self.indexStyle = indexStyle

        self.baseFont = wx.Font(pointSize = 12, family = wx.DEFAULT,
               style = wx.NORMAL, weight = wx.NORMAL,
               faceName = 'Consolas')
        self.indexFont = wx.Font(pointSize = 10, family = wx.DEFAULT,
               style = wx.NORMAL, weight = wx.NORMAL,
               faceName = 'Consolas')


        size = self.getTextSize()
        style = wx.TE_READONLY | wx.NO_BORDER
        super().__init__(self.parent, size=size, style=style)
        self.SetFont(self.baseFont)
        self.setIndex()
        self.EnableVerticalScrollbar(False)
        # self.SetBackgroundColour(self.parent.GetBackgroundColour())

    def getTextSize(self):
        dcBase = wx.MemoryDC()
        baseWidth, baseHeight, descent, externalLeading = dcBase.GetFullTextExtent(self.baseText, font=self.baseFont)
        dcIndex = wx.MemoryDC()
        indexWidth, indexHeihgt, descent, externalLeading = dcIndex.GetFullTextExtent(" "+self.indexText, font=self.indexFont)
        return (baseWidth+indexWidth+BORDER, baseHeight+BORDER)


    def setIndex(self):
        if self.indexStyle != IndexStyle.none:
            baseTextWithIndex = self.baseText + self.indexText
            textEffect = wx.TEXT_ATTR_EFFECT_SUPERSCRIPT if self.indexStyle == IndexStyle.super else wx.TEXT_ATTR_EFFECT_SUBSCRIPT
            attr = wx.richtext.RichTextAttr()
            attr.SetTextEffects(textEffect)
            attr.SetFlags(wx.TEXT_ATTR_EFFECTS)
            attr.SetTextEffectFlags(textEffect)
            self.AppendText(baseTextWithIndex)
            self.SetStyle(len(self.baseText), len(baseTextWithIndex), attr)
        else:
            self.AppendText(self.baseText)
        self.SetFont(self.baseFont)