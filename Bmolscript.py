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
  return pp_sequentie[(beginpos-1):eindpos]
      
def tm_check(tm_preprimerlist):
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
        if tm < 50 or tm > 60:
            primerlist.remove(y)         
    return primerlist
def cg_check(cg_primerlist):
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
        if cg_content < 50.0 or cg_content > 60.0:
            primers.remove(i)          
    return primers

def primerpakken(pp_sequentie):
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
    exclude_start = pp_sequentie.find("<")
    exclude_stop = pp_sequentie.find(">")
    for x in range(len(pp_sequentie)):
        
        preprimer = pp_sequentie[x:x+15]
        if len(preprimer) == 15 and ">" not in preprimer and "<"not in preprimer:
            preprimerlist.append(preprimer)
        if "{" in preprimer or "}" in preprimer or "[" in preprimer or "]" in preprimer:
          preprimerlist.remove(preprimer)
        if x < exclude_stop and x > exclude_start:
            try:
              preprimerlist.remove(preprimer)
            except ValueError:
              pass
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
def main():
    '''
    Een bestand wordt geopend met een sequentie erin. Deze sequentie wordt
    in een string omgezet en de sequentie wordt op de juiste posities geknipt
    er worden zo veel sequenties gemaakt als de lengte toelaat, en er wordt
    gecheckt of deze sequentie de juiste lengte heeft. Als dit het geval is,
    wordt de sequentie toegevoegd aan een lijst. De lijst wordt meegegeven
    aan de tm_checker.
    '''
    primerlengte = 15
    sequentie = open("seq.fa","r")
    seq =  ''.join(sequentie.readlines())
    f_pcrdeel = positie_pakker(seq,'f')
    f_preprimerlist = primerpakken(f_pcrdeel)
    f_primerlist = tm_check(f_preprimerlist)
    f_primers = cg_check(f_primerlist)
    print f_primers, "na gc_check"
    r_reversed = reverser(seq)
    r_pcrdeel = positie_pakker(r_reversed, 'r')
    r_preprimerlist = primerpakken(r_pcrdeel)
    r_primerlist = tm_check(r_preprimerlist)
    r_primers = cg_check(r_preprimerlist)
    print r_primers, "r, na gc_check"
main()
