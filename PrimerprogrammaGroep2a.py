# -*- coding: cp1252 -*-
"""
Sebastiaan de Vriend 06-01-2015 Controller maken.
Sebastiaan de Vriend 28-01-2015 documentatie, pep8.

Programma toont de schermen en roept de overige scripten aan.
Ook koppelt het programma alles aan elkaar.
"""

import wx

from Beginscherm import BeginScherm
from InvoerScherm import InvoerScherm
from OptieScherm import OptieScherm
from ResultaatScherm import ResultaatScherm

import Bmolscript


class PrimerProg(wx.App):
    """Klasse roept alles aan."""
    def OnInit(self):
        """
        Bij de OnInit wordt een functie aangeroepen die gebruikt wordt
        bij de normale init. De functie maakt een schermtellen aan, een
        schermlijst. Start vervolgens scherm beheer op om het eerste
        scherm te tonen. Daarna worden alle button events gebind en
        doorgestuurd naar de functie KnopBeheer. Als laatste wordt
        de gobale variable seq aangemaakt.
        De functie returned een True om het programma te tonen aan
        de apploop buiten de classe.
        """
        self.SC = 0
        self.SchermLijst = [BeginScherm, InvoerScherm, OptieScherm,
                            ResultaatScherm]
        self.SchermBeheer()
        self.Bind(wx.EVT_BUTTON, self.KnopBeheer)
        self.seq = ''
        return True

    def SchermBeheer(self):
        """
        De functie maakt als eerste de variabelen naam en fmt aan. Deze
        worden gebruikt voor scherm formaat en de naam van het scherm.
        Vervoglens wordt er via een if statement gecontroleerd wat de
        nummer is van self.SC ( schermcounter ) en daarop wordt
        de juiste scherm geopend. Bij scherm 3 wordt de sequentie
        veranderd en de speciale tekens worden eruit gehaald.
        """
        naam = 'Primer generator 2.0'
        fmt = (700, 350)
        if self.SC == 2:
            self.frame = self.SchermLijst[self.SC](None, seq=self.seq,
                                                   title=naam, size=fmt)
        elif self.SC == 3:
            tekens = '[]{}<>'
            for teken in tekens:
                self.seq = self.seq.replace(teken, "")
            self.frame = self.SchermLijst[self.SC](None, primers=self.res,
                                                   title=naam, size=fmt,
                                                   seq=self.seq)
        else:
            self.frame = self.SchermLijst[self.SC](None, title=naam, size=fmt)

    def KnopBeheer(self, event):
        """
        input: 1
            event: wx python event/
        De functie haalt de ID op en kijkt via een if statement waar
        de event vandaan komt.
        Als het event van doorgaan komt, dan wordt er een toepasselijke
        taak uitgevoerd. Als de event van Doorgaan komt en scherm 1, dan
        wordt de sequentie opgehaald in hoofdletters.
        Bij scherm 2 worden de settings opgehaald en doorgestuurd naar
        de primer script. Bij het laatste scherm wordt de schermcounter
        terug gezet op 0 om het programma opnieuw op te starten.
        Als de GetHelp ID overeenkomt met event, dan wordt de functie
        ShowMessage aangeroepen voor het helpscherm.
        """
        EventID = event.GetId()

        if EventID == self.frame.GetDoorgaan():
            if self.SC == 1:
                self.seq = self.frame.GetSeq().upper()
            elif self.SC == 2:
                self.info = self.frame.GetSettingVal()

                self.res = Bmolscript.main(self.info[2], self.info[1],
                                           self.info[0], self.seq)
            elif self.SC == 3:
                self.SC = 0

            self.SluitScherm()
        elif EventID == self.frame.GetHelp():
            self.ShowMessage()

    def GetHelpFromReadme(self, tl):
        """
        Input: 1
            tl: tekenlijst.
        Als eerste wordt de README.txt geopend om de readme informatie
        uit te lezen met readlines.
        Daarna wordt de go bool aangeroepen en de tekststring.
        Vervolgens wordt er geloopt door de regels en wordt er gekeken
        naar het tekentje. De tekst van readme tussen [[, ]] en <<, >>
        worden toegevoegd aan title en tekst.
        Output: 2
            title: string
            tekst: string
        """
        with open('README.txt', 'r') as f:
            data = f.readlines()
        go = False
        tekst = ''
        for regel in data:
            if regel[:-1] == tl[0]:
                go = True
            elif regel[:-1] == tl[1]:
                go = False
            if go:
                if regel[0] == '-':
                    title = regel[1:-1]
                elif tl[0] not in regel and tl[1] not in regel:
                    tekst += regel
        return title, tekst

    def ShowMessage(self):
        """
        Functie roept de functie GetHelpFromReadme aan en stuurt het
        resultaat door aan MessageBox.
        """
        if self.SC == 1:
            title, tekst = self.GetHelpFromReadme(['<<', '>>'])
        elif self.SC == 2:
            title, tekst = self.GetHelpFromReadme(['[[', ']]'])

        wx.MessageBox(tekst, title, wx.OK | wx.ICON_INFORMATION)

    def SluitScherm(self):
        """
        De functie sluit self.frame, telt 1 bij de schermteller en
        start de functie SchermBeheer op.
        """
        self.frame.Destroy()
        self.SC += 1
        self.SchermBeheer()


app = PrimerProg(False)
app.MainLoop()
