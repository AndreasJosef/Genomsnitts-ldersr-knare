# Funktion för att hämta in och verifiera åldern
def get_kön():
    # Initialiserar kön som en tom sträng och anger första_försök till True
    kön = ''
    första_försök = True # Kommer sättas till False efter felaktig inmatning

    # Loopar tills användaren anger ett giltigt kön ('M' för man eller 'K' för kvinna)
    while kön not in ["M", "K"]:
        # Om det inte är första försöket var inmatningen ogiltig: skriv ut ett felmeddelande
        if not första_försök:
            print("Felaktig inmatning! Ange ett K eller M.")

        # Ber användaren att ange kön och konverterar inmatningen till versaler
        kön = input("Ange kön (M för man, K för kvinna): ").upper()
        
        # Markerar att första försöket är gjort för att eventuellt visa felmeddelande vid nästa försök
        första_försök = False

    # Returnerar giltig könsinmatning ('M' eller 'K')
    return kön

def get_ålder():
    # Loopar tills användaren anger en giltig ålder som ett positivt heltal
    while True:
        try:
            # Försöker konvertera användarens inmatning till ett heltal (int)
            ålder = int(input("Ange ålder: "))
            
            # Kontrollera att åldern är ett positivt tal
            if ålder > 0:
                return ålder  # Returnerar åldern om den är giltig
            else:
                print("Åldern måste vara ett positivt tal.")  # Felmeddelande om åldern är <= 0
        
        # Hanterar ValueError om inmatningen inte är ett heltal
        except ValueError:
            print("Felaktig inmatning! Ange ett heltal.")
