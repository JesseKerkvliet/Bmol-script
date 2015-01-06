'''
Bmol primerprogramma
Jesse Kerkvliet
Bin2a
'''
from collections import Counter

def positie_pakker(pp_sequentie):
  '''
  Deze functie krijgt de volledige sequentie mee.
  Er worden twee waarden vastgesteld; de begin- en eind-positie.
  De functie geeft vervolgens een op de juist plaatsen geknipte
  sequentie terug
  '''
  beginpos = 5
  eindpos = 50
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
       #print y,tm
        if tm < 55 or tm > 60:
            primerlist.remove(y)

            #print len(primerlist)
            
        else:
            pass #print "PIEMEL", tm, len(primerlist)
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
        #print teldict
        
       
        cg_content = (teldict["G"] + teldict["C"])/ float(len(i)) * 100
        if cg_content < 50.0 or cg_content > 60.0:
            primers.remove(i)
            #print len(primers)
          
    return primers
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
    preprimerlist = []
    print len(seq)
    pcrdeel = positie_pakker(seq)
    print pcrdeel
    for x in range(len(pcrdeel)):
        
        preprimer = pcrdeel[x:x+15]
        if len(preprimer) == 15:
            preprimerlist.append(preprimer)
    print preprimerlist
    primerlist = tm_check(preprimerlist)
    print len(primerlist)
    
    primers = cg_check(primerlist)
    print len(primers)
    print primers
main()
