# Genomsnittsåldersräknare

Detta program beräknar genomsnittsåldern för två kategorier: kvinnor och män. Användaren matar in ålder och kön för varje person, och programmet beräknar och visar genomsnittsåldern för respektive kön.

## Mappstruktur

- `src/` - Innehåller huvudprogrammet och stödmoduler.
  - `main.py` - Huvudfilen som kör programmet.
  - `utils/` - Innehåller hjälpfunktioner för inmatningsvalidering och åldersberäkningar.
    - `input_helpers.py` - Innehåller funktionerna `get_kön()` och `get_ålder()`.
    - `calculations.py` - Innehåller funktionen `calc_average()`.
  
- `tests/` - Innehåller testfiler.
  - `test_log_file.md` - Detaljerade testfall för manuell testning.

- `README.md` - Översikt av applikationen och mappstrukturen.

## Användning
1. Clone 
  ```
  https://github.com/AndreasJosef/Genomsnitts-ldersr-knare.git
  ```

2. Kör huvudprogrammet:

   ```bash
   python src/main.py
   ```
