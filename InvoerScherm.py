"""
Sebastiaan de Vriend 06-01-2015 Invoer scherm maken.
Sebastiaan de Vriend 25-01-2015 bugfix en afronding.

Script toont invoer scherm met diverse opties en mogelijkheden.
"""
import os
import wx

from KnoppenPaneel import KnoppenPaneel
from SequentieInvoer import SequentieInvoer
from SubPaneel import SubPaneel


class InvoerScherm(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY,
                 title='', pos=wx.DefaultPosition, size=(600, 450),
                 style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER |
                                                  wx.CLOSE_BOX |
                                                  wx.SYSTEM_MENU),
                 name='Primer programma'):
        """
        Input 7:
            parent: Ouder van dit scherm.
            id: id van dit scherm.
            title: Titel van dit scherm.
            pos: Positie van dit scherm.
            size: Formaat van dit scherm.
            style: Style van dit scherm.
            name: Naam van dit scherm.
        De class wordt eerst super gemaakt om elementen van de geneste
        class beter aan te roepen.
        Vervolgens wordt het mainpaneel aangemaakt en wordt het knoppen
        paneel aangeroepen en uigezet. Daarna wordt sequentieinvoer
        toegevoegd aan self.seq.
        Meteen daarna worden twee elementen gebind. De eerste is voor
        de bladerknop en de tweede is voor elke textverandering in
        self.seq.
        Als laatste wordt alles toegevoegd aan de verticale boxsizer en
        wordt de self.SetSizer op de verticale boxsizer gezet en
        het scherm wordt zichtbaar gemaakt.
        """
        super(InvoerScherm, self).__init__(parent, id, title, pos, size,
                                           style, name)
        self.MainPaneel = SubPaneel(self)
        self.Vbox = wx.BoxSizer(wx.VERTICAL)
        self.Knoppen = KnoppenPaneel(self, vraag=True)
        self.Knoppen.SetDoorgaanAanUit(True)
        self.seq = SequentieInvoer(self)
        self.Bind(wx.EVT_BUTTON, self.Openen, self.seq.GetBladeren())
        self.Bind(wx.EVT_TEXT, self.HandelBox)
        self.Vbox.Add(self.seq, 19, wx.ALL | wx.EXPAND)
        self.Vbox.Add(self.Knoppen, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(self.Vbox)
        self.Show()

    def GetDoorgaan(self):
        """De functie roept self.Knoppen.GetDoorgaan an en retruend."""
        return self.Knoppen.GetDoorgaan()

    def GetSeq(self):
        """Functie returnt de sequentie in seq.GetSeq()."""
        return self.seq.GetSeq()

    def GetHelp(self):
        """Functie returnt de id van Knoppen.GetHelp()."""
        return self.Knoppen.GetHelp()

    def HandelBox(self, event):
        """
        Input: 1
            event: Event van wx python. Integer.
        De functie pakt de eventid en geeft deze door aan
        self.seq.CheckInvoer. Vervolgens wordt de functie
        ChecklistCheck aangeroepen en als laatste wordt de event
        geskipped om nieuwe events toe te laten.
        """
        eventid = event.GetId()
        self.seq.CheckInvoer(eventid)
        self.ChecklistCheck()
        event.Skip()

    def Openen(self, event):
        """
        Input: 1
            event: wx id van event.
        De functie opent een filedialog met als bestandstype een .fa
        Daarna wordt er gekeken met een if statement of de ok knop is
        ingedrukt.
        In de if statement wordt de filepath gepakt en het
        overeenkomende bestand wordt daarmee geopend.
        Daarna wordt er met een one line loop de inhoud overgenmen en
        wordt de eventuele header niet meegenomen.
        Na het filteren wordt de sequentie doorgegeven aan
        self.seq.SetBoxVal en wordt de functie HandleInvoer
        van self.seq aangeroepen om de interface te updaten.
        Als laatste wordt de file dialoog verwijderd.
        """
        wildcard = """Fasta(*.fa)|*.fa"""
        self.blad = wx.FileDialog(self, "Bladeren", os.getcwd(), "",
                                  wildcard, wx.OPEN)
        if self.blad.ShowModal() == wx.ID_OK:
            bestandsnaam = self.blad.GetPath()
            with open(bestandsnaam, 'r') as f:
                data = f.readlines()
            seqff = [x for x in data if x[0] != '>']
            seqnew = "".join(seqff)
            seqnew.replace("\n", "")
            self.seq.SetBoxVal(seqnew)
            self.seq.HandleInvoer(0)
        self.blad.Destroy()

    def ChecklistCheck(self):
        """
        Input: 0
        De functie leegt de dictionary self.chceklist.
        Vervolgens wordt de 2d lijst tekens aangemaakt waarin
        lijsten met tekens zitten. Dan wordt er gekeken of
        de lengte van de sequentei in self.seg.GetSeq kleiner is dan
        30. Als dit zo is, dan is de sequentie te klein voor primers te
        maken en wordt de dictionary waaarde op 0 gezet.
        Daarna wordt er geloopt door de tekenlijst en in de loop
        wordt er gekeken of het linker tekentje in de seq zit.
        Als dit zo is, dan wordt er gekeken of rechts van het tekentje
        de rechter teken zit door de sequentie te splitten op het linker
        tekentje en te zoeken in het de 2e deel van de lijst op het
        rechter tekentje. Als het tekentje erin zit, dan wordt de
        dictionary waarde op 1 gezet.
        Als laatste wordt de functie SwitchDoorgaan aangeroepen om
        de doorgaan knop aan of uit te zetten.
        """
        self.checklist = {}
        tekens = [['<', '>'], ['[', ']'], ['{', '}']]
        if len(self.seq.GetSeq()) < 30:
            self.checklist['seq'] = 0
        else:
            self.checklist['seq'] = 1
        for tek in tekens:
            
            if tek[0] in self.seq.GetSeq():
                if tek[1] in self.seq.GetSeq().split(tek[0])[1]:
                    if tek[0] == '[' or tek[0] == '{':
                        self.PrimerRegio(tek)
                    self.checklist[tek[0]] = 1
                else:
                    self.checklist[tek[0]] = 0
        self.SwitchDoorgaan()

    def PrimerRegio(self, tekenl):
        seq1 = self.seq.GetSeq().split(tekenl[0])[1]
        
        seq2 = seq1.split(tekenl[1])[0]
        if len(seq2) < 15:
            self.checklist['len' + tekenl[0]] = 0
        else:
            self.checklist['len' + tekenl[0]] = 1
    def SwitchDoorgaan(self):
        """
        Input: 0
        De functie zet de uit bool op false en loopt daarna door
        de dictionary self.checklist heen. Vervolgens wordt er in de
        loop gekeken of een checklist key ongelijk is aan 1. Als zo is,
        dan is er door de gebruiker nog geen volledige informatie
        ingevoerd. Uit wordt daarom dan ook op True gezet. Als
        laatste wordt de functie van self.Knoppen SetDoorgaanAanUit
        aangeroepen en wordt de bool uit meegegeven.
        Output: 0
        """
        uit = False
        for keys in self.checklist:
            if self.checklist[keys] != 1:
                uit = True
        self.Knoppen.SetDoorgaanAanUit(uit)
