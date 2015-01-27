"""
Sebastiaan de Vriend 06-01-15 Begin maken met knoppen paneel.

Script maakt een knoppenpaneel aan.
"""
import sys
import wx

from SubPaneel import SubPaneel

class KnoppenPaneel(wx.Panel):
    """
    Class maakt knoppen paneel aan. Heeft mogelijkheid om ID's
    op te vragen.
    """
    def __init__(self, parent, id=wx.ID_ANY, size=wx.DefaultSize, vraag=False,
                 knaam='Volgende'):
        """
        Input: 4
            Parent: Ouder van voor dit paneel.
            id=wx.ID_ANY: ID voor paneel, wordt random gemaakt.
            size=wx.DefaultSize: Grootte van paneel. Is standaard size.
            vraag=False: Optie om een extra knop te tonen. De knop
                         is voor help informatie te tonen. Staat
                         standaard uit.
            knaam: Naam voor de navigatie knop.
        De functie maakt als eerste de main paneel aan onder de naam
        self.KnopPaneel. Daarna wordt een Horizontale boxsizer
        aangemaakt die alles verticaal op volgorde plaatst.
        Daarna wordt de Doorgaan knop gemaakt met een automatische ID
        en label doorgaan. Vervolgens wordt er een tussenpaneel
        toegevoegd aan Hbox voor een kleine ruimte.
        Vervolgens wordt gekeken of de vraag knop nodig is met een if
        statement. Als deze nodig is, dan wordt de help knop aangemaakt
        en toegevoegd aan de hbox en daarna een tussenpaneel.
        Daarna wordt de stop knop gemaakt en gebind aan de functie
        Stoppen en wordt de stop knop toegevoegd aan de hbox.
        Als laatste wordt de self.SetSizer gezet op Hbox.
        """
        self.KnopPaneel = wx.Panel.__init__(self, parent, id, size=size)
        self.HBox = wx.BoxSizer(wx.HORIZONTAL)
        self.Doorgaan = wx.Button(self, id=-1, label=knaam)
        self.HBox.Add(self.Doorgaan, 1, wx.ALL | wx.EXPAND)
        self.HBox.Add(self.TussenPaneel(), 1, wx.ALL | wx.EXPAND)
        if vraag:
            self.Help = wx.Button(self, id=-1, label='Help')
            self.HBox.Add(self.Help, 1, wx.ALL | wx.EXPAND)
            self.HBox.Add(self.TussenPaneel(), 1, wx.ALL | wx.EXPAND)
        self.Stop = wx.Button(self, id=-1, label='Afsluiten')
        self.Bind(wx.EVT_BUTTON, self.Stoppen, self.Stop)
        self.HBox.Add(self.Stop, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(self.HBox)
        

    def GetDoorgaan(self):
        """Functie returnt Knop ID van Doorgaan."""
        return self.Doorgaan.GetId()

    def TussenPaneel(self):
        """Functie returned een leeg paneeltje voor opvulling. """
        return SubPaneel(self)
    
    def Stoppen(self, event):
        """Functie sluit het programma af als functie wordt aangeroepen."""
        sys.exit()

    def GetHelp(self):
        """Functie returnt de ID van de Help knop."""
        return self.Help.GetId()

    def SetDoorgaanAanUit(self, status):
        if status:
            self.Doorgaan.Disable()
        else:
            self.Doorgaan.Enable()
    
        
        
        
