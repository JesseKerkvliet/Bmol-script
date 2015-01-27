"""
Sebastiaan de Vriend 05-01-2015 Begin maken met beginscherm.

Programma toon beginscherm voor primerprogramma. bla
"""

import wx


from KnoppenPaneel import KnoppenPaneel
from SubPaneel import SubPaneel
from TekstPaneel import TekstPaneel


class BeginScherm(wx.Frame):
    """
    De klasse maakt de frame 'Beginscherm' aan met daarin een
    welkoms boodschap. Meer informatie staat in de init documentatie.
    """
    def __init__(self, parent, id=wx.ID_ANY, title='Primer_programma',
                 pos=wx.DefaultPosition, size=(600, 450),
                 style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU),
                 name="PrimerScherm"):
        """
        De init heeft de volgende input waardes:
            parent: Ouder van dit scherm.
            id: willekeurige wx id. is benodigd voor wx.
            title: titel van dit scherm.
            pos: Positie van dit scherm.
            size: Grootte van dit scherm.
            style: Standaard style voor dit scherm.
            name: Naam van dit scherm.
        De classe begint met een super statement om de Frame class
        te gebruiken.
        Vervolgens wordt het mainpaneel aangemaakt en daarna
        een verticale boxsizer.
        In de boxsizer worden de elementen KnoppenPaneel en TekstPaneel
        geplaatst.
        Als laatste wordt het scherm zichtbaar gemaakt.
        """
        super(BeginScherm, self).__init__(parent, id, title, pos, size,
                                          style, name)
        self.MainPaneel = SubPaneel(self)
        Vbox = wx.BoxSizer(wx.VERTICAL)
        self.Text = TekstPaneel(self.MainPaneel, TekstTy=1)
        self.Knop = KnoppenPaneel(self.MainPaneel)
        Vbox.Add(self.Text, 9.5, wx.ALL | wx.EXPAND)
        Vbox.Add(self.Knop, 0.5, wx.ALL | wx.EXPAND)
        self.MainPaneel.SetSizer(Vbox)
        self.Show()

    def GetDoorgaan(self):
        """Functie returned aanroep van Knop."""
        return self.Knop.GetDoorgaan()
