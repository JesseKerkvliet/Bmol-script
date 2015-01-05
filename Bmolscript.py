def positie_pakker(pp_sequentie):
  beginpos = 4
  eindpos = 10
  return pp_sequentie[(beginpos-1):eindpos]
  
  
def main():
    sequentie ="AAGCTCGTGATGTACTAGTACGTACTAT"
    print len(sequentie)
    print positie_pakker(seqlijst)
main()
