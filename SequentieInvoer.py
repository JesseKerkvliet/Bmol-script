"""
Sebastiaan de Vriend 06-01-15 Sequentie invoer maken.

Script zorgt voor sequentie van gebruikert.
"""

import wx
import wx.lib.intctrl

from SubPaneel import SubPaneel

class SequentieInvoer(wx.Panel):
    def __init__(self, parent, id=wx.ID_ANY, size=wx.DefaultSize):
        self.SeqPan = wx.Panel.__init__(self, parent, id, size=size)
        
        self.uptext = wx.StaticText(self, id, 'Pasta hier je sequentie:')
        
        self.invoer = wx.TextCtrl(self, id=-1, style=wx.TE_MULTILINE)
        self.dtext = wx.StaticText(self, id, 'Of blader vanaf je pc:',
                                   style=wx.ALIGN_LEFT)
        self.bknop = wx.Button(self, id=-1, label='Bladeren')
        self.OptiePan = self.MaakMiniOpties()
        
        self.invoer.Bind(wx.EVT_KEY_UP, self.HandleInvoer)
        #self.OptieCtrl[0].Bind(wx.EVT_KEY_UP, self.HandleOptiePan)
        #[x.Bind(wx.EVT_KEY_UP, self.HandleOptiePan) for x in self.OptieCtrl]
        self.HBox = wx.BoxSizer(wx.HORIZONTAL)
        self.HBox.Add(self.dtext)
        self.HBox.Add(self.bknop)
        self.VBox = wx.BoxSizer(wx.VERTICAL)
        self.VBox.Add(self.uptext, 0.5, wx.ALL | wx.EXPAND)
        self.VBox.Add(self.invoer, 2, wx.ALL | wx.EXPAND)
        self.VBox.Add(self.HBox, 0.5, wx.ALL | wx.EXPAND)
        self.VBox.Add(self.OptiePan, 2, wx.ALL | wx.EXPAND)
        self.SetSizer(self.VBox)

        
    def HandleInvoer(self, event):
        self.SeqControlle()
        self.OptieBoxStatus()
        self.CheckOptieBoxen()

    def HandleOptiePan(self, event):
        
        print 'yolo in seq'
    
    def GetBladeren(self):
        return self.bknop

    def GetTinvoer(self):
        return self.invoer.GetId()
     
    def GetInvoer(self):
        print 'get invoer'
        return self.invoer
        

    def SetBoxVal(self, seq, fout=False):
        """
        Input: 1
            seq: str van de sequentie, mag markers bevatten,
        De functie veranderd de TextCtr invoer, de plek waar de
        sequentie ingevoerd kan worden, naar de waarde van seq. Daarna
        wordt invoer gerefreshed om de sequentie te tonen op het scherm.
        """
        #if fout:
        curpos = self.invoer.GetInsertionPoint()
        self.invoer.SetValue(seq)
        if fout:
            self.invoer.SetInsertionPoint(curpos-1)
        else:
            self.invoer.SetInsertionPoint(curpos)
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
        self.OptieLijst = [{'Text':'Uitgesloten Regio <>:', 'L':'<', 'R': '>',
                            'idL':0,'idR': 0, 'tb':0}, 
                           {'Text':"3'-5' primer voorkeur []:", 'L':'[',
                            'R':']', 'idL':0, 'idR': 0, 'tb':0},
                            {'Text':"5'-3' primer voorkeur {}:", 'L':'{',
                            'R':'}', 'idL':0, 'idR': 0, 'tb':0}]
        self.OptieCtrl=[]
        OptieBox = wx.BoxSizer(wx.VERTICAL)
        for lijst in self.OptieLijst:
            hbox = wx.BoxSizer(wx.HORIZONTAL)
            lijst['tb'] = wx.StaticText(self, id=-1, label=lijst['Text'])
            lijst['idL'] = wx.lib.intctrl.IntCtrl(self, -1, name='L')
            streepje = wx.StaticText(self, id=-1, label='-')
            lijst['idR'] = Rveld = wx.lib.intctrl.IntCtrl(self, -1, name='R')
            self.BindNummerEvent(lijst['idR'])
            self.BindNummerEvent(lijst['idL'])
            hbox.Add(lijst['tb'])
            hbox.Add(lijst['idL'] )
            hbox.Add(streepje)
            hbox.Add(Rveld)
            OptieBox.Add(hbox)
            self.OptieCtrl.append(lijst['idL'])
            self.OptieCtrl.append(lijst['idR'])
        self.OptieBoxStatus()
        return OptieBox
    def BindNummerEvent(self, invoer):
        self.Bind(wx.EVT_KEY_UP, self.HandleOptiePan, invoer)
    def OptieBoxStatus(self):
        """
        De functie kijkt of de lengste van self.invoer groter is dan 0.
        Als dit zo is, dan worden de opties aangezet door een kleine
        for loop.
        Als dit niet zo is, dan wordt alles uitgezet door een kleine
        for loop.
        """
        
        if len(self.invoer.GetValue()) > 0:
            [x.Enable() for x in self.OptieCtrl]
        else:
            [x.Disable() for x in self.OptieCtrl]
    def GetOptiePan(self):
        print self.OptiePan
        return self.OptiePan
     
    def VeranderSeg(self, pos, teken):
        
        if pos != 0:
            verander = True
        else:
            verander = False
        seqoud = self.GetSeq()
        
        print pos
        newseq = seqoud.replace(teken, "")
        if verander:
            totaal_seq = str(newseq[0:pos] + teken + newseq[pos:])
        else:
            totaal_seq = newseq
        
        self.SetBoxVal(totaal_seq)
    
    def CheckInvoer(self, inputID):
        """
        Input: 1
            InputID: Id van wx element die een event heeft getriggerd.
        De functie loopt loop de optie lijst heen en kijkt of inputID
        overeen komt met de linker of rechter boxen. De juiste functie
        wordt aangeroepen voor een overeenkomende id.
        Als laatste worden de functies OptieBoxStatus en 
        CheckOptieBoxen gecheckt.
        """
        
        
        for l in self.OptieLijst:
            if inputID == l['idL'].GetId():
                
                self.VeranderSeg(l['idL'].GetValue(), l['L'])
                
            elif inputID == l['idR'].GetId():
                self.VeranderSeg(l['idR'].GetValue(), l['R'])

        self.OptieBoxStatus()
        self.CheckOptieBoxen()
        
    
    def SeqControlle(self):
        new_seq = ""
        tekenlijst = '<>{}[]'
        dna = 'AaTtCcGg'
        fout = False
        teller = 0
        print 'seq_contr'
        for teken in self.GetSeq():
            if teken in tekenlijst:
                tekenlijst = tekenlijst.replace(teken, "")
                teller += 1
                self.VeranderOptieBox(teken)
                new_seq += teken
            elif teken in dna:
                teller += 1
                new_seq += teken
            else:
                fout = True
        
        self.SetBoxVal(new_seq, fout)
        
                
    def VeranderOptieBox(self, teken):
        
        for dict in self.OptieLijst:
            for key in dict:
                if dict[key] == teken:
                    newkey =  'id' + str(key)
                    pos = self.GetSeq().find(teken)
                    
                    dict[newkey].SetValue(pos+1)
                
        
    def CheckOptieBoxen(self):
        """
        De functie loopt de waardes na van de checkboxen en kijkt of
        de tekentjes goed staan. Dit wordt gedaan door te kijken
        naar de uitkomst van links - rechts. Als deze namelijk
        hoger is dan 0, dan staan de tekens niet goed. Ook wordt
        er gekeken of de rechterkant en de linkerkant niet de waarde 0
        bevatten. Dan is er namelijk niks aan de hand. In de if statement
        wordt de achtergrond veranded naar de bijbehorende kleur. Na de
        if wordt de achtergrond van de tekst gerefreshed zodat deze
        op het scherm van de gebruiker getoont wordt.
        """
        for l in self.OptieLijst:
            
            if l['idL'].GetValue() - l['idR'].GetValue() >=0:
                if l['idR'].GetValue() != 0:
                    l['tb'].SetBackgroundColour('red')
                else:
                    l['tb'].SetBackgroundColour(None)
            elif l['idL'].GetValue() - l['idR'].GetValue() <=0:
                if l['idL'].GetValue() != 0:
                    l['tb'].SetBackgroundColour('green')
                else:
                    l['tb'].SetBackgroundColour(None) 
            l['tb'].Refresh() 
                
    
    
        
    
