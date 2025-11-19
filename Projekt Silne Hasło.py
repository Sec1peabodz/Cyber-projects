import math
import getpass 
import string

MIN_LENGTH = 8 

def entropia_hasla(haslo):
    #Obliczanie Entropii hasła (poziom złożoności)
    charset_size = 0
   
    if any(c in string.ascii_lowercase for c in haslo):
       
        charset_size += 26
    
    if any(c in string.ascii_uppercase for c in haslo):
      
        charset_size += 26
    
    if any(c in string.digits for c in haslo):
        
        charset_size += 10
    
    if any(c in string.punctuation for c in haslo):

        charset_size += len(string.punctuation)
    
    if any(c.isspace() for c in haslo):
    
        charset_size += 1

    return len(haslo) * math.log2(charset_size) if charset_size else 0
    
def sprawdz_sile_hasla():
    #funkcja sprawdzająca siłe hasła
    haslo = getpass.getpass('Wprowadz haslo')

    if len(haslo) < MIN_LENGTH:
        print(f"!!Twoje haslo jest za krótkie! Musi mieć przynajmniej {MIN_LENGTH} znaków.")
            
        return
    
    ilosc_malych_liter = sum(1 for c in haslo if c in string.ascii_lowercase)

    ilosc_duzych_liter = sum(1 for c in haslo if c in string.ascii_uppercase)

    ilosc_cyfr = sum(1 for c in haslo if c in string.digits)

    ilosc_znakow_specjalnych = sum(1 for c in haslo if c in string.punctuation)

    ilosc_znakow_bialych = sum(1 for c in haslo if c.isspace())

    entropia = entropia_hasla(haslo)

    #Klasyfikacja siły hasła
    if entropia < 28:
        uwagi = "! Bardzo słabe hasło, bardzo łatwe do zgadnięcia! Należy zmienić."
    elif entropia < 36:
        uwagi = "! Słabe hasło , wybierz coś bardziej złożonego."
    elif entropia < 60:
        uwagi = "Średniej jakości hasło, akceptowalne ale warto ulepszyć."
    elif entropia < 80:
        uwagi = "Silne hasło, bardzo trudne do złamania, można je zawsze ulepszyć." 
    else:
        uwagi = "Bardzo silne, super hasło."

    #Wyświetlanie Analizy hasła
    print("\n Analiza hasła:")
    print(f"{ilosc_malych_liter} małe litery")
    print(f"{ilosc_duzych_liter} wielkie litery")
    print(f"{ilosc_cyfr} cyfry")
    print(f"{ilosc_znakow_specjalnych} znaki specjalne")
    print(f"{ilosc_znakow_bialych} białe znaki")
    print(f"Entropia wynik: {entropia:.2f} bity")
    print(f" {uwagi}\n")

def sprawdz_kolejne_haslo():
    #Zapytanie o sprawdzenie kolejnego hasła
    while True:
        wybór = input("Czy chcesz sprawzić kolejne hasło? (tak/nie): ").strip().lower()
        if wybór == 'tak':
            return True
        elif wybór == 'nie':
            print("Wyjście... Dowidzenia!")
            return False
        else:
            print("Zła wartość wpisz 'tak' lub 'nie' .")
if __name__ == '__main__':
    print("===== Witaj w Testerze Mocy Haseł =====")
    sprawdz_sile_hasla()
    while sprawdz_kolejne_haslo():
        sprawdz_sile_hasla()
