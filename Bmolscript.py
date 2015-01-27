'''
Bmol primerprogramma
Jesse Kerkvliet
Bin2a
'''
from collections import Counter

def positie_pakker(pp_sequentie,pp_richting):
  '''
  Deze functie krijgt de volledige sequentie mee, en de richting waarin
  de primers gezocht moeten worden.
  Er worden twee waarden vastgesteld; de begin- en eind-positie.
  De functie geeft vervolgens een op de juist plaatsen geknipte
  sequentie terug
  '''
  if pp_richting == "f":
    beginpos = pp_sequentie.find('[')
    eindpos = pp_sequentie.find(']')
    if beginpos == -1:
      beginpos = 1
    if eindpos == -1:
      eindpos = pp_sequentie.find('<')
  elif pp_richting == "r":
    beginpos = pp_sequentie.find('{')
    eindpos = pp_sequentie.find('}')
    if beginpos == -1:
      beginpos = 1
    if eindpos == -1:
      eindpos = pp_sequentie.find('<')
  return pp_sequentie[beginpos:eindpos]
      
def tm_check(tm_preprimerlist, tm_list):
    '''
    Deze functie krijgt de lijst met gemaakte stukjes primers (preprimers)
    mee. De lijst wordt gekopieerd en voor ieder element in de lijst
    worden de individuele letters geteld door Counter, en in een
    dictionary geplaatst. De smelttemperatuur wordt berekend door
    de frequentie van T's en A's met twee te vermenigvuldigen,
    en de frequentie C's en G's met vier te vermenigvuldigen. De som hiervan
    is de smelttemperatuur. Er wordt gekeken of de smelttemperatuur tussen
    de vooraf aangegeven waarden ligt. Is dit niet zo, wordt de preprimer
    uit de lijst verwijderd. De gekopieerde lijst (zonder de foute preprimers)
    worden teruggegeven.
    '''
    primerlist = tm_preprimerlist[:]
    for y in tm_preprimerlist:
        
        teldict = Counter(y)
        tm = 2*teldict["T"] + 2*teldict["A"] + 4*teldict["G"] + 4*teldict["C"]
        if tm < tm_list[0] or tm > tm_list[1]:
            primerlist.remove(y)         
    return primerlist
def cg_check(cg_primerlist, cg_list):
    '''
    Deze functie krijgt de primerlijst mee die meegegeven is door de tm_check
    functie. Er wordt een kopie gemaakt van de lijst. Voor elk element
    in deze lijst wordt de sequentie geteld op de hoeveelheid nucleotiden
    dit wordt opgeslagen in een dictionary. Er wordt gekeken hoe veel
    C's en G's er in de sequentie zitten. Dit wordt gedeeld door het totaal
    en er wordt een indexcijfer van gemaakt. Er wordt gekeken of dit getal
    tussen de vooraf aangegeven waarden ligt. Is dit niet het geval,
    wordt de mogelijkheid uit de lijst verwijderd. De lijst wordt
    teruggegeven
    '''
    primers = cg_primerlist[:]
    for i in primers:
        teldict = Counter(i)
        cg_content = (teldict["G"] + teldict["C"])/ float(len(i)) * 100
        if cg_content < cg_list[0] or cg_content > cg_list[1]:
            primers.remove(i)          
    return primers

def primerpakken(pp_sequentie, pp_primerlength):
    '''
    De ingelezen sequentie wordt meegegeven.
    Er wordt in de sequentie gezocht naar de tekens die aangeven dat het
    gewenste product daar zit (< en >) en de posities worden opgeslagen
    Voor ieder element in de sequentie wordt een preprimer gemaakt door
    elke sequentie van de juiste lengte te pakken. Als de lengte 15 is,
    en de < en > tags zitten niet in de preprimer wordt deze toegevoegd
    aan een lijst. Er wordt gekeken of de primer op de posities binnen de
    < en > tags zitten, als dit zo is worden ze uit de lijst verwijderd.
    De lijst met preprimers wordt teruggegeven.
    '''
    preprimerlist = []
    for x in range(len(pp_sequentie)):
        preprimer = pp_sequentie[x:x+pp_primerlength]
        if len(preprimer) == pp_primerlength:
            preprimerlist.append(preprimer)
        if "{" in preprimer or "}" in preprimer or "[" in preprimer or "]" in preprimer:
          preprimerlist.remove(preprimer)
    return preprimerlist

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
  
def returncheck(rc_primers):
    '''
    De gemaakte primers worden meegegeven. Er wordt gekeken naar de lengte van
    de lijst. Als deze groter is dan vijf wordt er net zo lang van het einde
    van de lijst primers verwijderd, totdat de lijst nog vijf primers lang is.
    Er wordt een melding gemaakt van het verwijderen van primers.
    De lijst met vijf elementen wordt teruggegeven.
    '''
    if len(rc_primers) > 5:
      print "Er zijn meer dan vijf primers gevonden."
      print "Alleen de eerste vijf worden weergegeven."
      print "Kies voor een beter resultaat een kleinere range."
      while len(rc_primers) > 5:
        rc_primers.remove(rc_primers[-1])
    
    return rc_primers                

def main(tm_list, cg_list, primerlength, seq):
    '''
    Een bestand wordt geopend met een sequentie erin. Deze sequentie wordt
    in een string omgezet en de sequentie wordt op de juiste posities geknipt
    er worden zo veel sequenties gemaakt als de lengte toelaat, en er wordt
    gecheckt of deze sequentie de juiste lengte heeft. Als dit het geval is,
    wordt de sequentie toegevoegd aan een lijst. De lijst wordt meegegeven
    aan de tm_checker.
    '''

    f_pcrdeel = positie_pakker(seq,'f')
    f_preprimerlist = primerpakken(f_pcrdeel,primerlength)
    f_primerlist = tm_check(f_preprimerlist, tm_list)
    f_primers = cg_check(f_primerlist, cg_list)
    f_primers = returncheck(f_primers)
    print f_primers, "na gc_check"
    
    r_reversed = reverser(seq)
    r_pcrdeel = positie_pakker(r_reversed, 'r')
    r_preprimerlist = primerpakken(r_pcrdeel, primerlength)
    r_primerlist = tm_check(r_preprimerlist, tm_list)
    r_primers = cg_check(r_preprimerlist, cg_list)
    r_primers = returncheck(r_primers)
    print r_primers, "r, na gc_check"

    returnlijst = []
    returnlijst.append(f_primers)
    returnlijst.append(r_primers)
    print returnlijst
    return returnlijst
  
sequentie = open("seq.fa","r")
seq =  ''.join(sequentie.readlines())

main([10,60],[10.0,60.0], 15, seq)

