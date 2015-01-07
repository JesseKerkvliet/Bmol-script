"""
Sebastiaan de Vriend 06-01-2015 Invoer scherm maken.

Script toont invoer scherm met diverse opties en mogelijkheden.
"""

import wx
import os

from KnoppenPaneel import KnoppenPaneel
from SubPaneel import SubPaneel
from SequentieInvoer import SequentieInvoer

class InvoerScherm(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY,
                 title='Primer programam - Sequentie invoeren',
                 pos=wx.DefaultPosition, size=(800, 450),
                 style=wx.DEFAULT_FRAME_STYLE &~(wx.RESIZE_BORDER |
                                                 wx.CLOSE_BOX |
                                                 wx.SYSTEM_MENU),
                 name='Primer programma'):
        super(InvoerScherm, self).__init__(parent, id, title, pos, size,
                                           style, name)
        self.MainPaneel = SubPaneel(self)
        self.checklist = {'seq': 0, 'exl':0}
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
        return self.Knoppen.GetDoorgaan()

    def GetSeq(self):
        return self.seq.GetSeq()

    def GetHelp(self):
        return self.Knoppen.GetHelp()

    def HandelBox(self, event):
        eventid = event.GetId()
        self.seq.CheckInvoer(eventid)
        self.ChecklistCheck()
            
        

    def Openen(self, event):
        print 'bladeren'
        wildcard = """Fasta(*.fa)|*.fa|
Alle bestanden (*.*)|*.*""" 
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
        uit = False
        
        if len(self.seq.GetSeq()) != 0:
            self.checklist['seq'] = 1
        else:
            self.checklist['seq'] = 0
        # check voor excl
        self.checklist['exl'] = 1
        for keys in self.checklist:
            if self.checklist[keys] == 1:
                pass
            else:
                uit = True
        
        self.Knoppen.SetDoorgaanAanUit(uit)
