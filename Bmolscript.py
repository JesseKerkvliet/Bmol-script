def inputs():
  sequentie = str(raw_input("Voer hier de sequentie in: ")
  begin = int(raw_input("Voer hier het beginpunt in waar de primers mogen annealen: ")
  eind = int(raw_input("Voer hier het beginpunt in waar de primers mogen annealen: ")
  max_grootte = int(raw_input("Hoe groot mag het PCR product maximaal zijn? ")


def positie_pakker(pp_sequentie):
  beginpos = 4
  eindpos = 10
  return pp_sequentie[(beginpos-1):eindpos]
  
  
def main():
    sequentie ="AAGCTCGTGATGTACTAGTACGTACTAT"
    print len(sequentie)
    print positie_pakker(seqlijst)
main()
