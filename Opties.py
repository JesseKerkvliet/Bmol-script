"""
Sebastiaan de Vriend 26-01-2015 Script schrijven om de kleuren te fixen.
Sebastiaan de Vriend 27-01-2015 Afronding en pep8.
"""

import wx

from SubPaneel import SubPaneel


class Opties(wx.Panel):
    """De classe maakt de extra opties aan."""
    def __init__(self, parent, seq, id=wx.ID_ANY, size=wx.DefaultSize):
        """
        De functie maakt als eerste de standaard paneel aan
        gevolgt voor een vertical boxsizer. Daarna wordt de sequentie
        textbox aangemaakt waarmee alleen uitgelezen kan worden.
        Daarna worden de sliders aangemaakt, gevolgt door de
        Primerlengte slider. Als dit gedaan is, dan wordt de functie
        maak balk aangeroepen en wordt er elke keer een slider set
        meegegeven. Als laatste wordt de self.SetSizer goedgezet.
        """
        self.OptiePan = wx.Panel.__init__(self, parent, id, size=size)
        self.Vbox = wx.BoxSizer(wx.VERTICAL)
        self.seq = wx.TextCtrl(self, style=(wx.TE_MULTILINE | wx.TE_READONLY |
                                            wx.TE_NO_VSCROLL),
                               id=-1, value=seq)
        self.Vbox.Add(self.seq, 2, wx.ALL | wx.EXPAND)
        self.seq.Enable(False)
        sliderlijst = self.MaakSliders()
        self.seq = seq
        self.MaakPL()
        self.MaakBalk(sliderlijst[0], 'GC waardes:')
        self.MaakBalk(sliderlijst[1], 'TM waardes:')
        self.SetSizer(self.Vbox)

    def MaakSliders(self):
        """
        De functie maakt de 4 sliders aan voor minimale en maximale
        gc en tm waardes en geeft de elementen terug in een lijst.
        """
        self.MinGC = wx.Slider(self, value=55, minValue=10, maxValue=55,
                               style=wx.SL_LABELS)
        self.MaxGC = wx.Slider(self, value=60, minValue=60, maxValue=75,
                               style=wx.SL_LABELS)
        self.MinTM = wx.Slider(self, value=55, minValue=10, maxValue=55,
                               style=wx.SL_LABELS)
        self.MaxTM = wx.Slider(self, value=60, minValue=60, maxValue=75,
                               style=wx.SL_LABELS)
        return [[self.MinGC, self.MaxGC], [self.MinTM, self.MaxTM]]

    def MaakBalk(self, ls, naam):
        """
        Input: 2
            ls: lijstm met elementen.
            naam: str met naam voor balk.
        De functie zet een rij alligned neer. Dit wordt gedaan
        met een horizontal boxsizer met als eerste een spatie.
        Daarna wordt de tekst functie aangeroepen en
        de tekst daarvan wordt rechts in het midden geplaatst.
        Daarna wordt de functie MaakStukje twee keer aangeroepen en
        daaraan wordt de tekst en een slider meegegeven. Als laatste
        wordt er nog een ruimte toegevoegd om de slider van de rand van
        het scherm af te houden en wordt de hbox toegevoegd aan Vbox.
        """
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddSpacer(10)
        hbox.Add(self.MaakTekst(naam, 'l'), 0, wx.ALL |
                 wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED)
        self.MaakStukje(hbox, 'min', ls[0])
        self.MaakStukje(hbox, 'max', ls[1])
        hbox.AddSpacer(10)
        self.Vbox.Add(hbox, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL)

    def MaakStukje(self, hbox, naam, el):
        """
        Input: 3
            hbox: horizontal boxsizer.
            naam: naam voor de tekst.
            el: element, slider.
        De functie zet een tussenpaneel in de box en daarna de tekst.
        Vervolgens wordt er een spatie toegevoegd en daarna de slider.
        """
        hbox.Add(self.TP(), 1, wx.ALL)
        hbox.Add(self.MaakTekst(naam, 'l'), 0, wx.ALL |
                 wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.SHAPED)
        hbox.AddSpacer(40)
        hbox.Add(el, 1, wx.ALL)

    def TP(self):
        """Functie geeft een SubPaneel(tussenpaneel) terug."""
        return SubPaneel(self)

    def MaakTekst(self, tekst, optie):
        """
        Input: 2
            tekst: tekst voor de label.
            optie: allign optie.
        De funtctie kijkt welke optie meegegeven is en maakt
        een statictext aan met de allignment optie. l voor LEFT.
        Als laatste wordt de wx element terug gegeven.
        """
        if optie == 'l':
            allign = wx.StaticText(self, id=-1, label=tekst,
                                   style=wx.ALIGN_LEFT)
        return allign               

    def MaakPL(self):
        """
        Input: 0
        De functie maakt een horizontale boxsizer aan en maakt daarna
        een static text aan en een Slider. Vervolgens wordt de text in
        de habox gezet en rechts in het midden gealligned.
        Daarna wordt er een spacer toegevoegd voor extra ruimte en
        wordt de slider toegevoegd met weer een spacer. Als laatste
        wordt de hbox toegevoegd aan de vertical boxsizer.
        """
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        text = wx.StaticText(self, id=-1, label='Primer Lengte:',
                             style=wx.ALIGN_LEFT)

        self.PrimerLen = wx.Slider(self, value=20, minValue=10,
                                   maxValue=30,
                                   style=wx.SL_LABELS, name='Primer lengte:')
        hbox.AddSpacer(10)
        hbox.Add(text, 0, wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL |
                 wx.SHAPED)
        hbox.AddSpacer(5)
        hbox.Add(self.PrimerLen, 6, wx.ALL)
        hbox.AddSpacer(5)
        self.Vbox.Add(hbox, 0, wx.ALL | wx.EXPAND)

    def GetWaardes(self):
        """
        De functies pakt de waardes van alle sliders en stopt deze in
        de volgende lijst [primerlengte, [gc], [tm]]. Deze wordt
        terug gegven.
        """
        pl = self.PrimerLen.GetValue()
        gn = float(self.MinGC.GetValue())
        gx = float(self.MaxGC.GetValue())
        tn = self.MinTM.GetValue()
        tx = self.MaxTM.GetValue()
        lijst = [pl, [gn, gx], [tn, tx]]
        return lijst
