"""
Sebastiaan de Vriend 06-01-15 Sequentie invoer maken.

Script zorgt voor sequentie van gebruikert.
"""

import wx


from SubPaneel import SubPaneel

class SequentieInvoer(wx.Panel):
    def __init__(self, parent, id=wx.ID_ANY, size=wx.DefaultSize):
        self.SeqPan = wx.Panel.__init__(self, parent, id, size=size)
        
        self.uptext = wx.StaticText(self, id, 'Pasta hier je sequentie:')
        
        self.invoer = wx.TextCtrl(self, id=-1, style=wx.TE_MULTILINE)
        self.dtext = wx.StaticText(self, id, 'Of blader vanaf je pc:',
                                   style=wx.ALIGN_LEFT)
        self.bknop = wx.Button(self, id=-1, label='Bladeren')
        OptiePan = self.MaakMiniOpties()
        
        

        self.HBox = wx.BoxSizer(wx.HORIZONTAL)
        self.HBox.Add(self.dtext)
        self.HBox.Add(self.bknop)
        self.VBox = wx.BoxSizer(wx.VERTICAL)
        self.VBox.Add(self.uptext, 0.5, wx.ALL | wx.EXPAND)
        self.VBox.Add(self.invoer, 2, wx.ALL | wx.EXPAND)
        self.VBox.Add(self.HBox, 0.5, wx.ALL | wx.EXPAND)
        self.VBox.Add(OptiePan, 2, wx.ALL | wx.EXPAND)
        self.SetSizer(self.VBox)

    def GetBladeren(self):
        return self.bknop

    def GetTinvoer(self):
        return self.invoer.GetId()
        

    def SetBoxVal(self, seq):
        """
        Input: 1
            seq: str van de sequentie, mag markers bevatten,
        De functie veranderd de TextCtr invoer, de plek waar de
        sequentie ingevoerd kan worden, naar de waarde van seq. Daarna
        wordt invoer gerefreshed om de sequentie te tonen op het scherm.
        """
        self.invoer.SetValue(seq)
        self.invoer.Refresh()

    def GetSeq(self):
        return self.invoer.GetValue()

    def MaakMiniOpties(self):
        """
        De functie maakt de textvelden voor de standaard opties
        en zet deze in een boxsizer en in een globale lijst om
        waardes eruit te halen / erin te zetten.
        De functie start met een globale optielijst met daarin
        dictionaries die gebruikt worden voor de textctr, en de
        texten die gemaakt worden in de loop.
        De ID's in de dictionaries zorgen ervoor dat de bijbehorende
        waardes en objecten eenvoudig op te sporen zijn.
        Na de dictionary wordt de Verticale boxsizer Optiebox
        gemaakt. Hierin komen de objecten in te staan van de loop die
        daarna start.
        In de loop wordt hbox aangemaakt, dit is een horizontale
        boxsizer.
        Vervolgens wordt text, L(inker)veld, streepje en R(echter)veld
        aangemaakt met de text / id's van de dictionary. Deze worden
        op die volgorde ook toegevoegd aan de BoxSizer hbox en
        als laatste wordt hbox toegevoegd aan OptieBox.
        Na de loop wordt OptieBox teruggegeven.

        Output: 1
            OptieBox: BoxSizer met daarin aangemaakte objecten.
        """
        self.OptieLijst = [{'Text':'Uitgesloten Regio:', 'L':'<', 'R': '>',
                            'idL':wx.ID_ANY,'idR': wx.ID_ANY}, 
                           {'Text':'Primer binding regio:', 'L':'[',
                            'R':']', 'idL':wx.ID_ANY, 'idR': wx.ID_ANY}]
        self.OptieCtrl=[]
        OptieBox = wx.BoxSizer(wx.VERTICAL)
        for lijst in self.OptieLijst:
            hbox = wx.BoxSizer(wx.HORIZONTAL)
            text = wx.StaticText(self, id=-1, label=lijst['Text'])
            Lveld = wx.TextCtrl(self, id=lijst['idL'])
            streepje = wx.StaticText(self, id=-1, label='-')
            Rveld = wx.TextCtrl(self, id=lijst['idR'])
            hbox.Add(text)
            hbox.Add(Lveld)
            hbox.Add(streepje)
            hbox.Add(Rveld)
            OptieBox.Add(hbox)
            self.OptieCtrl.append(Lveld)
            self.OptieCtrl.append(Rveld)
        return OptieBox

    def CheckInvoer(self, inputID):
        print inputID
        
    
