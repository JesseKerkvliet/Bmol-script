def inputs():
  sequentie = str(raw_input("Voer hier de sequentie in: ")
  begin = int(raw_input("Voer hier het beginpunt in waar de primers mogen annealen: ")
  eind = int(raw_input("Voer hier het beginpunt in waar de primers mogen annealen: ")
  max_grootte = int(raw_input("Hoe groot mag het PCR product maximaal zijn? ")


def positie_pakker(pp_sequentie):
  beginpos = 4
  eindpos = 10
  return pp_sequentie[(beginpos-1):eindpos]
  
def nucleotide_teller(primer):
  A_lijst = []
  T_lijst = []
  C_lijst = []
  G_lijst = []
  for x in sequentie:
    if x == "A":
      x.append(A_lijst)
    elif x == "T":
      x.append(T_lijst)
    elif x == "C":
      x.append(C_lijst)
    elif x == "G":
      x.append(G_lijst)
    return (A_lijst, C_lijst, G_lijst, T_lijst)
    
def tm_berekenen():
  Tm = 2*(len(A_lijst) + len(T_lijst)) + 4*(len(C_lijst) + len(G_lijst))
  return Tm
  
def GC-content():
  
  
def main():
    sequentie ="AAGCTCGTGATGTACTAGTACGTACTAT"
    print len(sequentie)
    print positie_pakker(seqlijst)
main()
