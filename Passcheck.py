import re
from colorama import Fore, Style, init

# Colorama başlat
init(autoreset=True)

def sifre_gucu(sifre):
    puan = 0
    öneriler = []

    if len(sifre) >= 8:
        puan += 1
    else:
        öneriler.append("Şifrenizi en az 8 karakter yapın.")

    if re.search(r"[A-Z]", sifre):
        puan += 1
    else:
        öneriler.append("Şifrenize büyük harf ekleyin.")

    if re.search(r"[a-z]", sifre):
        puan += 1
    else:
        öneriler.append("Şifrenize küçük harf ekleyin.")

    if re.search(r"[0-9]", sifre):
        puan += 1
    else:
        öneriler.append("Şifrenize rakam ekleyin.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", sifre):
        puan += 1
    else:
        öneriler.append("Şifrenize özel karakter ekleyin (!,@,#, vb.).")

    if puan <= 1:
        seviye = Fore.RED + "Çok Zayıf"
    elif puan == 2:
        seviye = Fore.RED + "Zayıf"
    elif puan == 3:
        seviye = Fore.YELLOW + "Orta"
    elif puan == 4:
        seviye = Fore.CYAN + "Güçlü"
    elif puan == 5:
        seviye = Fore.GREEN + Style.BRIGHT + "Çok Güçlü"
    else:
        seviye = Fore.RED + "Geçersiz"

    return seviye, puan, öneriler

if __name__ == "__main__":
    while True:
        sifre = input(Fore.BLUE + "Şifrenizi girin (çıkmak için q): " + Style.RESET_ALL)
        
        if sifre.lower() == "q":
            print(Fore.MAGENTA + "Programdan çıkılıyor...")
            break
        
        if not sifre.strip():
            print(Fore.RED + "Lütfen şifre giriniz!")
            continue
        
        seviye, puan, öneriler = sifre_gucu(sifre)
        print("Şifre Gücü: {} ({}/5)".format(seviye, puan))
        
        if öneriler:
            print(Fore.MAGENTA + "Öneriler:")
            for o in öneriler:
                print("-", o)
        print()  # boş satır