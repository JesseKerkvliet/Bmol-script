"""
Sebastiaan de Vriend 06-01-2015 Invoer scherm maken.

Script toont invoer scherm met diverse opties en mogelijkheden.              
"""
import os
import wx



from KnoppenPaneel import KnoppenPaneel
from SubPaneel import SubPaneel
from SequentieInvoer import SequentieInvoer

class InvoerScherm(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY,
                 title='Primer programam - Sequentie invoeren',
                 pos=wx.DefaultPosition, size=(600, 450),
                 style=wx.DEFAULT_FRAME_STYLE &~(wx.RESIZE_BORDER |
                                                 wx.CLOSE_BOX |
                                                 wx.SYSTEM_MENU),
                 name='Primer programma'):
        super(InvoerScherm, self).__init__(parent, id, title, pos, size,
                                           style, name)
        self.MainPaneel = SubPaneel(self)
        #self.checklist = {'seq': 0, 'exl':0}
        self.Vbox = wx.BoxSizer(wx.VERTICAL)
        self.Knoppen = KnoppenPaneel(self, vraag=True)
        self.Knoppen.SetDoorgaanAanUit(True)
        self.seq = SequentieInvoer(self)
        self.Bind(wx.EVT_BUTTON, self.Openen, self.seq.GetBladeren())
        #self.seq.Bind(wx.EVT_CHAR_HOOK, self.HandelBox, self.seq.GetInvoer())
        #self.Bind(wx.EVT_KEY_UP, self.HandelBox, self.seq.GetTinvoer())
        self.Bind(wx.EVT_TEXT, self.HandelBox)
        self.Vbox.Add(self.seq, 19, wx.ALL | wx.EXPAND)
        self.Vbox.Add(self.Knoppen, 1, wx.ALL | wx.EXPAND)
        self.SetSizer(self.Vbox)
        self.Show()

    def GetDoorgaan(self):
        """De functie roept self.Knoppen.GetDoorgaan an en retruend."""
        return self.Knoppen.GetDoorgaan()

    def GetSeq(self):
        return self.seq.GetSeq()

    def GetHelp(self):
        return self.Knoppen.GetHelp()

    def HandelBox(self, event):
        
        
        eventid = event.GetId()
        
        self.seq.CheckInvoer(eventid)
        self.ChecklistCheck()
        event.Skip()
    def HandleOptieBox(self, event):
        """
        Mogelijk overbodig als de binds goed gaan.
        """
        print 'yolo'
        eventid = 'swag'
        

    def Openen(self, event):
        print 'bladeren'
        wildcard = """Fasta(*.fa)|*.fa""" 
        self.blad = wx.FileDialog(self, "woop", os.getcwd(), "",
                                  wildcard, wx.OPEN)
        if self.blad.ShowModal() == wx.ID_OK:
            bestandsnaam = self.blad.GetPath()
            
            with open(bestandsnaam, 'r') as f:
                data = f.readlines()
            seqff = [x[:-1] for x in data if ">" not in x]
            self.seq.SetBoxVal("".join(seqff))
            
            
        self.blad.Destroy()

    def ChecklistCheck(self):
        """
        De functie is bedoelt als check functie om te kijken of de
        gebruiker alles juist heeft ingevuld. Als alles van de checklist
        goed is, dan wordt de doorgaan knop weer aangezet.
        """
        self.checklist = {}
        uit = False
        seq = self.seq.GetSeq()
        tekens = [['<','>'],['[',']'],['{','}']]
        if len(seq) != 0:
            self.checklist['seq'] = 1
        else:
            self.checklist['seq'] = 0
        for tek in tekens:
            if tek[0] in seq:
                if tek[1] in seq.split(tek[0])[1]:
                    self.checklist[tek[0]] = 1
                else:
                    self.checklist[tek[0]] = 0
        
        for keys in self.checklist:
            if self.checklist[keys] == 1:
                pass
            else:
                uit = True
        print self.checklist
        self.Knoppen.SetDoorgaanAanUit(uit)
