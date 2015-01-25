"""
Sebastiaan de Vriend 06-01-15 Sequentie invoer maken.
Sebastiaan de Vriend 23-01-15 Afmaken, pep8 etc.

Script zorgt voor sequentie van gebruikert.
"""

import wx
import wx.lib.intctrl

from SubPaneel import SubPaneel


class SequentieInvoer(wx.Panel):
    """
    De class maakt de sequentie invoer. het checkt of de invoer
    goed is en geeft de mogelijkheid om de eind sequentie door
    te geven.
    """
    def __init__(self, parent, id=wx.ID_ANY, size=wx.DefaultSize):
        """
        Input: 3
            parent: wx element, ouder van dit paneel.
            id: wx id.
            size: grootte.
        Als eerste wordt de sequentie paneel aangemaakt, gevolgt
        door een statictext en een textctrl waar de sequentie
        ingevoerd kan worden.
        Daarna wordt een statictekst aangemaakt samen met een
        blader knop. Vervolgens wordt de functie MaakMiniOpties()
        aangeroepen waarmee de primer opties gemaakt mee worden.
        Dan wordt self.invoer gebind op keyboard events als de toets
        omhoog komt en elke event daarvan wordt doorgestuurd naar
        HandleInvoer.
        Daarna worden de tekst toegevoegd aan een horizontale boxsizer.
        Vervolgens worden alle elementen toegevoegd aan een verticale
        boxsizer en wordt de setsizer goed gezet.
        """
        self.SeqPan = wx.Panel.__init__(self, parent, id, size=size)
        self.uptext = wx.StaticText(self, id, 'Plak hier je sequentie:')
        self.invoer = wx.TextCtrl(self, id=-1, style=wx.TE_MULTILINE)
        self.dtext = wx.StaticText(self, id, 'Of blader vanaf je pc:',
                                   style=wx.ALIGN_LEFT)
        self.bknop = wx.Button(self, id=-1, label='Bladeren')
        self.OptiePan = self.MaakMiniOpties()
        self.invoer.Bind(wx.EVT_KEY_UP, self.HandleInvoer)
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
        """
        Input: 1
            Event: Wx event.
        De roept de functies SeqControlle, OptieBoxStatus en
        CheckOptieBoxen aan. De functie wordt zelf aangeroepen als
        er een toets op het toetsenbord is ingedrukt en losgelaten.
        Output: 0
        """
        self.SeqControlle()
        self.OptieBoxStatus()
        self.CheckOptieBoxen()

    def GetBladeren(self):
        """Fucntie returnt bladerknop."""
        return self.bknop

    def SetBoxVal(self, seq, fout=False):
        """
        Input: 1
            seq: str van de sequentie, mag markers bevatten,
        De functie veranderd de TextCtr invoer, de plek waar de
        sequentie ingevoerd kan worden, naar de waarde van seq. Daarna
        wordt invoer gerefreshed om de sequentie te tonen op het scherm.
        """
        curpos = self.invoer.GetInsertionPoint()
        self.invoer.SetValue(seq)
        if fout:
            self.invoer.SetInsertionPoint(curpos-1)
        else:
            self.invoer.SetInsertionPoint(curpos)
        self.invoer.Refresh()

    def GetSeq(self):
        """Functie returnt de str in de textctr van self.invoer."""
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
        self.OptieLijst = [{'Text': 'Uitgesloten Regio <>:', 'L': '<',
                            'R': '>', 'idL': 0, 'idR': 0, 'tb': 0},
                           {'Text': "3'-5' primer voorkeur []:", 'L': '[',
                            'R': ']', 'idL': 0, 'idR': 0, 'tb': 0},
                           {'Text': "5'-3' primer voorkeur {}: ", 'L': '{',
                            'R': '}', 'idL': 0, 'idR': 0, 'tb': 0}]
        self.OptieCtrl = []
        OptieBox = wx.BoxSizer(wx.VERTICAL)
        for lijst in self.OptieLijst:
            hbox = wx.BoxSizer(wx.HORIZONTAL)
            lijst['tb'] = wx.StaticText(self, id=-1, label=lijst['Text'])
            lijst['idL'] = wx.lib.intctrl.IntCtrl(self, -1, name='L')
            streepje = wx.StaticText(self, id=-1, label='-')
            lijst['idR'] = Rveld = wx.lib.intctrl.IntCtrl(self, -1, name='R')
            hbox.Add(lijst['tb'])
            hbox.Add(lijst['idL'])
            hbox.Add(streepje)
            hbox.Add(Rveld)
            OptieBox.Add(hbox)
            self.OptieCtrl.append(lijst['idL'])
            self.OptieCtrl.append(lijst['idR'])
        self.OptieBoxStatus()
        return OptieBox

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

    def VeranderSeg(self, pos, teken):
        """
        Input: 2
            pos: Integer, positie waar sequentie veranderd moet worden.
            teken: str, tekentje
        De functie kijkt als eerste of pos ongelijk is aan 0 en zet
        daarmee verander aan of uit. Vervolgens wordt de sequnetie
        opgehaald en in de variable seqoud gestopt. Daarna wordt
        er uit de sequentie het tekentje verwijderd.
        Vervolgens wordt het tekentie op de juiste positie
        terug gestopt als verander aan staat, en anders wordt
        newseq de totaal_seq. Als laatste wordt de sequentie
        doorgestuurd naar de functie SetBoxVal.
        """
        if pos != 0:
            verander = True
        else:
            verander = False
        seqoud = self.GetSeq()
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
        """
        De functie maakt als eerste controlle / begin variabelen aan
        en loopt vervolgens door de sequentie van de functie
        self.GetSeq().
        Daarin wordt gekeken of elk tekentje in de tekenlijst staat.
        Als dit zo is, dan wordt het tekentje uit de tekenlijst
        verwijderd, en wordt de functie VeranderOptieBox aangeroepen
        met het tekentje. Daarna wordt het tekentje toegevoegd aan
        de new_seq var. Als het tekentje in de DNA var staat, dan wordt
        het tekentje ook toegevoegd aan new_seq.
        Als teken niet in dna of tekenlijst staat, dan wordt fout
        op True gezet en wordt het tekentje niet toegevoegd. Hierdoor
        komen er geen dubbele tekens in de sequentie en worden
        foute letters verwijderd.
        Na de loop wordt er nog een keer geloopt door tekenlijst
        waarbij elke teken wordt doorgegeven aan VeranderOptieBox
        en wordt de nieuwe sequentie en de var fout doorgegeven aan
        SetBoxVal.
        """
        new_seq = ""
        tekenlijst = '<>{}[]'
        dna = 'AaTtCcGg'
        fout = False
        for teken in self.GetSeq():
            if teken in tekenlijst:
                tekenlijst = tekenlijst.replace(teken, "")
                self.VeranderOptieBox(teken)
                new_seq += teken
            elif teken in dna:
                new_seq += teken
            else:
                fout = True
        [self.VeranderOptieBox(teken) for teken in tekenlijst]
        self.SetBoxVal(new_seq, fout)

    def VeranderOptieBox(self, teken):
        """
        Input: 1
            teken: string, primer markeer teken.
        De functie loopt door de self.OptieLijst heen en vervolgens
        door de dictionary in de lijst. In de dictionary loop
        wordt gekeken of het tekentje overeenkomt met de dictionary
        waarde. Als dit zo is, dan wordt er een sleutel gevormd met de
        str 'id' + key. Daarna wordt er gezocht naar de locatie van het
        tekentje en wordt als laatste de wx element op de waarde
        van de positie gezet.
        Output: 0
        """
        for dictio in self.OptieLijst:
            for key in dictio:
                if dictio[key] == teken:
                    newkey = 'id' + str(key)
                    pos = self.GetSeq().find(teken)

                    dictio[newkey].SetValue(pos+1)

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

            if l['idL'].GetValue() - l['idR'].GetValue() >= 0:
                if l['idR'].GetValue() != 0:
                    l['tb'].SetBackgroundColour('red')
                else:
                    l['tb'].SetBackgroundColour(None)
            elif l['idL'].GetValue() - l['idR'].GetValue() <= 0:
                if l['idL'].GetValue() != 0:
                    l['tb'].SetBackgroundColour('green')
                else:
                    l['tb'].SetBackgroundColour(None)
            l['tb'].Refresh()
