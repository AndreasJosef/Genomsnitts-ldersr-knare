from utils.input_helpers import get_kön, get_ålder
from utils.calculations import calc_average

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
    print(f"\nGenomsnittsåldern för kvinnor: {f_ages_average} år")
    print(f"Genomsnittsåldern för män: {m_ages_average} år\n")

# Funktioner
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

# Starta programmet
if __name__ == "__main__":
    main()