"""
Sebastiaan de Vriend 05-01-2015 TekstPaneel schrijven

Classe maakt een tekst paneel aan met de gewenste tekst via type.
Zie documentatie TekstPaneel.
"""

import wx

from SubPaneel import SubPaneel

class TekstPaneel(wx.Panel):
    """Class maakt een tekst panel aan."""
    def __init__(self, parent, id=wx.ID_ANY, size=wx.DefaultSize, TekstTy=1):
        """
        Input:  4
            Parent: Ouder van het paneel.
            id=wx.ID_ANY: Willekeurige ID, tenzij anders is ingevoegd.
            size=wx.DefaultSize: Standaard size voor paneel, tenzij
                                 anders is ingevoegd.
            TekstTy=1: TekstType is een integer waarmee je zelf kan
                       de tekst van het paneel kan aanpassen.
                       Zie verdere documentatie van de functie
                       voor gebruik van TekstTY

        De Functie maakt een panel aan met wx.Panel. Vervolgens wordt
        een boxsizer gemaakt waarin de tekst komt, ook wordt TekstTy
        global gemaakt.
        Daarna wordt er met de functie teksten de tekst opgehaald voor
        het paneeltje en wordt deze in de variable 'schermtekst'
        geplaatst.
        Daarna wordt wx.StaticText gebruikt om de tekst module aan te
        maken. Daarin wordt de tekst van schermtekst ingestopt.
        Vervolgens wordt er met een if statement gekeken welke
        TekstTy er is en wordt FSize gezet op een gepaste integer.
        Dit is de fontsize, deze wordt gebruikt in font.
        Als laatste wordt de font veranderd van paneeltekst en wordt
        deze aan de boxsizer 'box' toegevoegd.
        Als laatste wordt de size gezet op box.
        """
        self.TekstPaneel = wx.Panel.__init__(self, parent, id, size=size,
                                          style=wx.BORDER_SUNKEN)
        self.TekstTy = TekstTy
        box = wx.BoxSizer()
        schermtekst = self.Teksten()
        paneeltekst = wx.StaticText(self, id, "".join(schermtekst))
        if self.TekstTy == 1:
            FSize = 22
        font = wx.Font(FSize, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        paneeltekst.SetFont(font)
        box.Add(paneeltekst, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(box)
        

    def Teksten(self):
        """
        Input: 0
        De functie returnt tekst aan de hand van TekstTy. Hier is het
        mogelijk om de teksten van de panelen te veranderen en tekst
        toe te voegen aan de if statement.
        """
        if self.TekstTy == 1:
            return ("""HOLA HOLA SENIOR EN WELKOM IN HET PRIMERPROGRAMMA
                       VAN GROEP 2A""")
