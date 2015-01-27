"""
Sebastiaan de Vriend 27-01-2015 Shcrijven primer paneel.

"""

import wx

from SubPaneel import SubPaneel

class PrimerPaneel(wx.Panel):

    def __init__(self, parent, primers, seq, id=wx.ID_ANY,
                 size=wx.DefaultSize):
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
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        tekst = wx.StaticText(self, id=-1, label=naam)
        vbox1.Add(tekst, 0, wx.ALL | wx.ALIGN_CENTRE)
        hbox.Add(radio, 1, wx.ALL | wx.ALIGN_CENTRE)
        for x in prim:
            prbox = wx.TextCtrl(self, style=wx.TE_READONLY, size=(250, 24),
                                id=-1, value=x)
            vbox2.Add(prbox, 3, wx.ALL )
            vbox2.AddSpacer(1)
        hbox.Add(vbox2, 2, wx.ALL | wx.ALIGN_CENTRE)
        vbox1.Add(hbox, 1, wx.ALL )
        return vbox1

    def PCRLengte(self, event):
        fwd = self.primers[0][self.radio1.GetSelection()]
        rev = self.primers[1][self.radio2.GetSelection()]
        nr = self.lengtepakker(fwd, rev)
        self.LenText.SetLabel('PCR product lengte:    ' + str(nr))

    def lengtepakker(self, lp_f, lp_r):
        '''
        Er worden drie dingen meegegeven:
        de forward primer, de reverse primer en de gehele sequentie.
        Ik geef nu een lijst door als test, die wordt gejoined tot een string.
        Dit zal uitgecommentarieerd zijn.
        De positie van de forward primer wordt gezocht in de sequentie.
        De reverse primer wordt opgezocht in de reverse-complement sequentie
        Die functie zal ik er ook bij zetten.
        De reverse-positie wordt van het totaal afgetrokken en het verschil
        tussen de forward en de reverse is dan de totale pcr lengte.
        '''
        forwardpos = self.seq.find(lp_f)
        reverseseq = self.reverser(self.seq)
        reversepos = reverseseq.find(lp_r) # staat anders?
        reverse = len(self.seq) - reversepos
##        print forwardpos
##        print reversepos
##        print reverse - forwardpos
##        print len(self.seq)
        return reverse
        
        
    def reverser(self, r_seq):
        """
        De sequentie wordt meegegeven.
        Er wordt gekeken voor ieder teken in de sequentie (in omgekeerde volgorde)
        naar het bijbehorende teken in de complement dictionary.
        Er wordt dan een lijst gemaakt waarin het omgekeerde complement wordt
        opgeslagen. Dit wordt omgezet naar een string en teruggegeven.
        """
        complement_dict = {'A':'T','T':'A','G':'C','C':'G',}
        complement_list = []
        for teken in r_seq[::-1]:
            complement_list += complement_dict[teken]
    
        return  ''.join(complement_list)


    def MaakRadio(self):
        keuze1 = ['Primer'+str(x) for x in range(1, len(self.primers[0])+1)]
        self.radio1 = wx.RadioBox(self, id=1, label='',
                                  style=wx.RA_SPECIFY_ROWS, choices=keuze1)
        keuze2 = ['Primer'+str(x) for x in range(1, len(self.primers[1])+1)]
        self.radio2 = wx.RadioBox(self, id=1, label='',
                                  style=wx.RA_SPECIFY_ROWS, choices=keuze2)
        self.radio1.Bind(wx.EVT_RADIOBOX, self.PCRLengte)
        self.radio2.Bind(wx.EVT_RADIOBOX, self.PCRLengte)
        return [self.radio1, self.radio2]
        
        
            
                              
