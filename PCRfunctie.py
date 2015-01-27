def lengtepakker(lp_f, lp_r, seq):
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
    #lp_f = ''.join(lp_f)
    #lp_r = ''.join(lp_r)
    forwardpos = seq.find(lp_f)
    
    reverseseq = reverser(seq)
    reversepos = seq.find(lp_r)
    reverse = len(seq) - reversepos
    print forwardpos
    print reversepos
    print reverse - forwardpos

def reverser(r_seq):
    '''
    De sequentie wordt meegegeven.
    Er wordt gekeken voor ieder teken in de sequentie (in omgekeerde volgorde)
    naar het bijbehorende teken in de complement dictionary.
    Er wordt dan een lijst gemaakt waarin het omgekeerde complement wordt
    opgeslagen. Dit wordt omgezet naar een string en teruggegeven.
    '''
    complement_dict = {'A':'T','T':'A','G':'C','C':'G', '{':'}',
                       '}':'{', '[':']', ']':'[', '<':'>', '>':'<'}
    complement_list = []
    for teken in r_seq[::-1]:
      complement_list += complement_dict[teken]
    
    return  ''.join(complement_list)
