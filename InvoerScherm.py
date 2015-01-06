"""
Sebastiaan de Vriend 06-01-2015 Invoer scherm maken.

Script toont invoer scherm met diverse opties en mogelijkheden.
"""

import wx

from KnoppenPaneel import KnoppenPaneel
from SubPaneel import SubPaneel

class InvoerScherm(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title='Shreck is dreck',
                 pos=wx.DefaultPosition, size=(800, 450),
                 style=wx.DEFAULT_FRAME_STYLE &~(wx.RESIZE_BORDER |
                                                 wx.CLOSE_BOX |
                                                 wx.SYSTEM_MENU),
                 name='ogre'):
        super(InvoerScherm, self).__init__(parent, id, title, pos, size,
                                           style, name)
        self.MainPaneel = SubPaneel(self)
        self.Show()
