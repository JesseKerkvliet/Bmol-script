"""
Sebastiaan de Vriend 27-01-2015 Shcrijven primer paneel.

"""

import wx

from SubPaneel import SubPaneel


class PrimerPaneel(wx.Panel):
    """De classe maakt het primer paneel en toont deze."""
    def __init__(self, parent, primers, seq, id=wx.ID_ANY,
                 size=wx.DefaultSize):
        """
        parent
                Ouder van het paneel
            id
                id voor frame. Als er geen id aanwezig is, dan zal
                deze aangemaakt worden met de library van wx python.
            size=wx.DefaultSize
                Size van Paneel. Als er geen waarde is meegegeven zal
                de standaard waarde van wx python gebruikt worden.
            primers: lijst met primers.
            seq: str met sequentie.
        ALs eerste wordt er een standaard paneeltje aangemaakt.
        Vervolgens wordt primers global gemaakt en daarna wordt de
        functie MaakRadio aangeroepen voor de radio boxen.
        Dan wordt de functie MaakPrimers 2x aangeroepen om de 2 lijsten
        op scherm te tonen. Als laatste wordt alles toegevoegd aan de
        sizers.
        """
        self.PrimerPan = wx.Panel.__init__(self, parent, id, size=size)
        self.fvbox = wx.BoxSizer(wx.VERTICAL)
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.primers = primers
        radlist = self.MaakRadio()
        self.hbox.Add(self.MaakPrimers(primers[0], 'Forward', radlist[0]),
                      1, wx.ALL | wx.EXPAND)
        self.hbox.Add(self.MaakPrimers(primers[1], 'Reversed', radlist[1]),
                      1, wx.ALL | wx.EXPAND)
        self.fvbox.Add(self.hbox, 1, wx.ALL | wx.EXPAND)
        self.LenText = wx.StaticText(self, id=-1, label='PCR Lengte: ')
        self.seq = seq
        self.fvbox.Add(self.LenText, 0, wx.ALL | wx.ALIGN_CENTRE)
        self.SetSizer(self.fvbox)
        self.PCRLengte(0)

    def MaakPrimers(self, prim, naam, radio):
        """
        Input: 3
            prim: primerslijst
            naam: string
            radio: radiobox element.
        De functie maakt teksten aan en alligned alles netjes in
        de BoxSizers...
        """
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        tekst = wx.StaticText(self, id=-1, label=naam)
        vbox1.Add(tekst, 0, wx.ALL | wx.ALIGN_CENTRE)
        hbox.Add(radio, 1, wx.ALL | wx.ALIGN_CENTRE)
        for x in prim:
            prbox = wx.TextCtrl(self, style=wx.TE_READONLY, size=(250, 24),
                                id=-1, value=x)
            vbox2.Add(prbox, 3, wx.ALL)
            vbox2.AddSpacer(1)
        hbox.Add(vbox2, 2, wx.ALL | wx.ALIGN_CENTRE)
        vbox1.Add(hbox, 1, wx.ALL)
        return vbox1

    def PCRLengte(self, event):
        """
        input: 1
            event: wx event.
        de fucntie haalt de posities van de radioboxen op en
        daarmee de sequenties uit de primerslijst. Daarna
        worden de sequenties doorgegeven aan lengtepakker.
        Als laatste wordt de tekstbox geupdate met de pcrlengte.
        """
        fwd = self.primers[0][self.radio1.GetSelection()]
        rev = self.primers[1][self.radio2.GetSelection()]
        nr = self.lengtepakker(fwd, rev)
        self.LenText.SetLabel('PCR product lengte:    ' + str(nr))

    def lengtepakker(self, lp_f, lp_r):
        '''
        Input: 2
            lp_f: primer forward.
            lp_r: primer reversed.
        De functie berekent het verschil uit tussend de primer bindingen.
        '''
        forwardpos = self.seq.find(lp_f)
        reverseseq = self.reverser(self.seq)
        reversepos = reverseseq.find(lp_r)
        reverse = len(self.seq) - reversepos
        return reverse

    def reverser(self, r_seq):
        """
        Input: 1
            r_seq: sequentie, str
        De functie maakt de sequentie complementair.
        Output: 1
            str met nieuwe sequentie.
        """
        complement_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        complement_list = []
        for teken in r_seq[::-1]:
            complement_list += complement_dict[teken]
        return ''.join(complement_list)

    def MaakRadio(self):
        """
        Functie maakt radioboxen aan en geeft de elementen terug in
        een lijst.
        """
        keuze1 = ['Primer'+str(x) for x in range(1, len(self.primers[0])+1)]
        self.radio1 = wx.RadioBox(self, id=1, label='',
                                  style=wx.RA_SPECIFY_ROWS, choices=keuze1)
        keuze2 = ['Primer'+str(x) for x in range(1, len(self.primers[1])+1)]
        self.radio2 = wx.RadioBox(self, id=1, label='',
                                  style=wx.RA_SPECIFY_ROWS, choices=keuze2)
        self.radio1.Bind(wx.EVT_RADIOBOX, self.PCRLengte)
        self.radio2.Bind(wx.EVT_RADIOBOX, self.PCRLengte)
        return [self.radio1, self.radio2]
