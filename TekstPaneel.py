"""
Sebastiaan de Vriend 05-01-2015 TekstPaneel schrijven

Classe maakt een tekst paneel aan met de gewenste tekst via type.
Zie documentatie TekstPaneel.
"""

import wx

from SubPaneel import SubPaneel

class TekstPaneel(wx.Panel):
    """Class maakt een scherm panel aan."""
    def __init__(self, parent, id=wx.ID_ANY, size=wx.DefaultSize, TekstTy=1):
        self.TekstPaneel = SubPaneel(self)
        self.TekstTy = TekstTy
        box = wx.BoxSizer()
        schermtekst = Teksten()
        paneeltekst = wx.StaticText(self, id, "".join(schermtekst))
        if self.Tekst == 1:
            FSize = 22
        font = wx.Font(FSize, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        tekst.SetFont(font)
        box.Add(tekst, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(box)
        

    def Teksten(self):
        if self.TekstTy == 1:
            return ("""HOLA HOLA SENIOR EN WELKOM IN HET PRIMERPROGRAMMA
                       VAN GROEP 2A""")
