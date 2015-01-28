"""
Sebastiaan de Vriend 27-01-2015 maken resultaatscherm.

"""

import wx

from KnoppenPaneel import KnoppenPaneel
from PrimerPaneel import PrimerPaneel
from SubPaneel import SubPaneel
from TekstPaneel import TekstPaneel


class ResultaatScherm(wx.Frame):
    """De classe maakt de resultaat frame aan."""
    def __init__(self, parent, id=wx.ID_ANY, title='Primer_programma',
                 pos=wx.DefaultPosition, size=(600, 350),
                 style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU),
                 name="PrimerScherm", primers=[], seq=''):
        """
        Input 9:
            parent: Ouder van dit scherm.
            id: id van dit scherm.
            title: Titel van dit scherm.
            pos: Positie van dit scherm.
            size: Formaat van dit scherm.
            style: Style van dit scherm.
            name: Naam van dit scherm.
            primers: Lijst met primers.
            seq: str met sequentie.
        De init begint met een super en maakt een main paneel aan.
        Vervolgens  wordt er gekeken of de lengte van de primerlijst
        0 is. Als deze 0 is, dan is er geen resultaat en wordt
        de tekstpaneel aangeroepen. Anders wordt primerpaneel
        aangeroepen. Als laatste wordt knop paneel aangeroepen en
        wordt alles toegevoegd aan de sizers.
        """
        super(ResultaatScherm, self).__init__(parent, id, title, pos, size,
                                          style, name)
        self.MainPaneel = SubPaneel(self, id=-1)
        self.Vbox = wx.BoxSizer(wx.VERTICAL)
        if len(primers[0]) == 0 or len(primers[1]) == 0:
            self.tekst = TekstPaneel(self, TekstTy=2)
            self.Vbox.Add(self.tekst, 1, wx.ALL | wx.EXPAND)
        else:
            self.Vbox.Add(PrimerPaneel(self, primers, seq))
        self.Knop = KnoppenPaneel(self, knaam='Opnieuw')
        self.Vbox.Add(self.Knop, 0, wx.ALL | wx.EXPAND)
        self.SetSizer(self.Vbox)
        self.Vbox.Fit(self)
        self.Show()

    def GetDoorgaan(self):
        """Functie returnt Knop.Doorgaan()."""
        return self.Knop.GetDoorgaan()
