def get_kön():
    kön = ''
    första_försök = True

    while kön not in ["M", "K"]:

        if första_försök != True:
            print("Felaktig inmatning! Ange ett K eller M.")

        kön = input("Ange kön (M för man, K för kvinna): ").upper()
        
        första_försök = False

    return kön

def get_ålder():
    while True:
        try:
            ålder = int(input("Ange ålder: "))
            if ålder > 0:
                return ålder  
            else:
                print("Åldern måste vara ett positivt tal.")
        except ValueError:
            print("Felaktig inmatning! Ange ett heltal.")