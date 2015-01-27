"""
Sebastiaan de Vriend 23-01-2015 Maken optiescherm.
Sebastiaan de Vriend 27-01-2015 Pep8 en afronding.
"""

import wx

from KnoppenPaneel import KnoppenPaneel
from Opties import Opties
from SubPaneel import SubPaneel


class OptieScherm(wx.Frame):
    """De classe maakt de frame aan voor het optiescherm. zie init
       voor meet informatie"""
    def __init__(self, parent, id=wx.ID_ANY, title='Primer_programma',
                 pos=wx.DefaultPosition, size=(600, 350),
                 style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU),
                 name="PrimerScherm", seq=''):
        """
        Input 8:
            parent: Ouder van dit scherm.
            id: id van dit scherm.
            title: Titel van dit scherm.
            pos: Positie van dit scherm.
            size: Formaat van dit scherm.
            style: Style van dit scherm.
            name: Naam van dit scherm.
            seq: De sequentie om te tonen.
        De init start met een super en vervolgens wordt het standaard
        paneeltje aangemaakt met daarna een vbox. Daarna
        wordt het knoppenpaneel aangeroepen en de optiepaneel waaraan
        de sequentie wordt meegegeven.
        Daarna worden de opties en knop toegevoegd aan de vertical
        boxsizer en wordt de SetSizer goed gezet gevolgt door
        een fit om alles netjes te tonen. Als laatste wordt Show
        aangeroepen om het scherm te tonen.
        """
        super(OptieScherm, self).__init__(parent, id, title, pos, size,
                                          style, name)
        self.MainPaneel = SubPaneel(self, id=-1)
        self.Vbox = wx.BoxSizer(wx.VERTICAL)
        self.Knop = KnoppenPaneel(self, vraag=True)
        self.Opties = Opties(self, seq)
        self.Vbox.Add(self.Opties, 1, wx.ALL | wx.EXPAND)
        self.Vbox.Add(self.Knop, 0, wx.ALL | wx.EXPAND)
        self.SetSizer(self.Vbox)
        self.Vbox.Fit(self)
        self.Show()

    def GetDoorgaan(self):
        """Functie returnt id van Knop.GetDoorgaan()."""
        return self.Knop.GetDoorgaan()

    def GetSettingVal(self):
        """Functie returnt waardes van self.Opties.GetWaardes()."""
        return self.Opties.GetWaardes()

    def GetHelp(self):
        """Functie returnt id van Knop.GetHelp()."""
        return self.Knop.GetHelp()


if __name__ == '__main__':
    app = wx.App(False)
    OptieScherm(None, -1, seq='atcg')
    app.MainLoop()
