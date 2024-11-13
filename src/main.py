from utils.input_helpers import get_kön, get_ålder
from utils.calculations import calc_average

# Huvudfunktion
def main():
    # Välkomstmeddelande som förklarar syftet med programmet
    print("Detta program beräknar genomsnittsåldern för två kategorier: kvinnor och män.\n")

    # Samlar in ålder för kvinnor och män från användaren och verifierar inmatningen
    k_åldrar_list, m_åldrar_list = mata_in_personer()
            
    # Beräknar genomsnittsåldern för kvinnor och män med funktionen calc_average
    f_ages_average = calc_average(k_åldrar_list)
    m_ages_average = calc_average(m_åldrar_list)

    # Visar resultaten för användaren
    print(f"\nGenomsnittsåldern för kvinnor: {f_ages_average} år")
    print(f"Genomsnittsåldern för män: {m_ages_average} år\n")

# Funktion som hämtar och organiserar data från användaren i listor för kvinnor och män
def mata_in_personer():
    # Skapar tomma listor för att lagra åldrar för kvinnor och män separat
    k_åldrar = []
    m_åldrar = []

    while True:
        # Anropar hjälpfunktioner för att få och verifiera inmatningar för kön och ålder
        kön = get_kön()
        ålder = get_ålder()

        # Lägger till åldern i motsvarande lista beroende på kön
        if kön == 'M':
            m_åldrar.append(ålder)
        elif kön == 'K':
            k_åldrar.append(ålder)

        # Frågar användaren om de vill fortsätta mata in fler personer eller avsluta
        fortsätta = input("Tryck enter för nästa eller skriv 's' för att avsluta... ").lower()

        # Avslutar loopen om användaren skriver 's'
        if fortsätta == 's':
            break
    
    # Returnerar listorna med åldrar som en tuple (k_åldrar, m_åldrar)
    return k_åldrar, m_åldrar

# Startar programmet
if __name__ == "__main__":
    main()
