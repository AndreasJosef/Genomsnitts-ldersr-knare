# Huvudfunktion
def main():
    
    # Välkomstmeddelande
    print("Detta program beräknar genomsnittsåldern för två kategorier: kvinnor och män.\n")

    # Läser in och verifierar data från användaren
    k_åldrar_list, m_åldrar_list = mata_in_personer()
            
    # Beräkna genomsnittsåldrar
    f_ages_average = calc_average(k_åldrar_list)
    m_ages_average = calc_average(m_åldrar_list)

    # Visa resultaten
    print(f"Genomsnittsåldern för kvinnor: {f_ages_average} år")
    print(f"Genomsnittsåldern för män: {m_ages_average} år")

# Funktioner
def calc_average(age_list):

    # Förhindrar division med 0
    if len(age_list) == 0: 
        return 0
    
    # Ränka ut genomsnittet och runda till två decimaler 
    avg = round(float(sum(age_list) / len(age_list)), 2)

    return avg

def mata_in_personer():
    # Listor för åldrar
    k_åldrar = []
    m_åldrar = []

    while True:
        # Inmatning
        kön = get_kön()
        ålder = get_ålder()

        if kön == 'M':
            m_åldrar.append(ålder)
        elif kön == 'K':
            k_åldrar.append(ålder)

        # Fråga om användaren vill fortsätta
        fortsätta = input("Tryck enter för nästa eller skriv 's' för att avsluta... ").lower()

        if fortsätta == 's':
            break
    
    return k_åldrar, m_åldrar

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

# Starta programmet
if __name__ == "__main__":
    main()