"""
Sebastiaan de Vriend 05-01-2015 SubPaneel class maken.

Script maakt een paneel aan.
"""
import wx

class SubPaneel(wx.Panel):
    """Klasse maakt een SubPaneel aan. Zie init voor documentatie."""
    def __init__(self, parent, id=wx.ID_ANY, size=wx.DefaultSize,
                 style=wx.BORDER_DEFAULT):
        """
        Maakt een paneel. Heeft de volgende parameters.
            parent
                Ouder van het paneel
            id
                id voor frame. Als er geen id aanwezig is, dan zal
                deze aangemaakt worden met de library van wx python.
            size=wx.DefaultSize
                Size van Paneel. Als er geen waarde is meegegeven zal
                de standaard waarde van wx python gebruikt worden.
            style=wx.BORDER_DEFAULT
                Style voor de paneel. Als er geen waarde is meegegeven
                dan zal de standaard style van wx gebruikt worden.
        """
        super(SubPaneel, self).__init__(parent, id, size=size, style=style)
