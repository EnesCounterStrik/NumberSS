import re
from kisanumaralar import kisa_numara_sorgula
from cografihat import cografi_sorgula
from mobilhat import mobil_sorgula

ASCII_ART = r"""
           ⣿⣿⣿⣿⣿
           ⣿⣿⣿⣿⣿
           ⣿⣿⣿⣿⣿
           ⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣶⣶⣶⣶⣶⣿⡷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠛⠛⠛⠛⠷⣶⣤⣀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⠈⢳⡀⢀⣠⣴⡿⠿⠛⠁
⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⣿⣿⣿
⠀⠀⠀⠀⠀⢀⡾⠀⢀⣠⣤⣄⢸⣿⣿⣿
⠀⠀⠀⠀⠀⣾⠁⠀⣾⠋⠈⠹⣿⣿⣿⣿⡇    .S_sSSs     .S       S.    .S_SsS_S.    .S_SSSs     sSSs   .S_sSSs     sSSs    sSSs
⠀⠀⠀⠀⢸⡏⠀⠀⢻⡆⠀⠀⢹⣿⣿⣿⡇   .SS~YS%%b   .SS       SS.  .SS~S*S~SS.  .SS~SSSSS    d%%SP  .SS~YS%%b    d%%SP   d%%SP
⠀⠀⠀⠀⢸⡇⠀⠀⢸⡇⠀⠀⠈⣿⣿⣿    S%S    `S%b  S%S       S%S  S%S `Y' S%S  S%S    SSSS  d%S'    S%S    `S%b  d%S'    d%S'
⠀⠀⠀⠀⢸⡇⠀⠀⢸⣇⠀⠀⠀⣿⣿⡿    S%S     S%S  S%S       S%S  S%S     S%S  S%S    S%S  S%S     S%S     S%S  S%|     S%|
⠀⠀⠀⠀⢸⡇⠀⠀⢸⣿⠀⠀⢠⣿⣿⡇    S%S     S&S  S&S       S&S  S%S     S%S  S%S SSSS%P  S&S     S%S     d*S  S&S     S&S
⠀⠀⠀⠀⠸⣷⠀⠀⠈⣿⠀⢀⣾⣿⣿     S&S     S&S  S&S       S&S  S&S     S&S  S&S  SSSY   S&S_Ss  S&S    .S*S  Y&Ss    Y&Ss
⠀⠀⠀⠀⠀⣿⡀⠀⠀⠻⢶⣿⣿⣿⡇     S&S     S&S  S&S       S&S  S&S     S&S  S&S    S&S  S&S~SP  S&S_sdSSS    `S&&S   `S&&S
⠀⠀⢀⣤⡾⠃⠀⠀⠀⠈⣿⣿⣿        S&S     S&S  S&S       S&S  S&S     S&S  S&S    S&S  S&S     S&S~YSY%b     `S*S    `S*S
⢠⣶⣯⣤⣤⣤⣤⡴⠶⠶⣼⣿⣿⣷⣤⣀    S*S     S*S  S*b       d*S  S*S     S*S  S*S    S&S  S*b     S*S    `S%b     l*S     l*S
                        S*S     S*S  S*S.     .S*S  S*S     S*S  S*S    S*S  S*S.    S*S    S%S    .S*P    .S*P
                        S*S     S*S   SSSbs_sdSSS   S*S     S*S  S*S SSSSP    SSSbs  S*S    S&S   sSS*S   sSS*S
                        S*S     SSS    YSSP~YSSY    SSS     S*S  S*S  SSY      YSSP  S*S    SSS   YSS'    YSS'
                        SP                                  SP   SP                  SP
                        Y                                   Y    Y                   Y
"""

def numara_sorgula(girdi):
    sadece_rakam = re.sub(r"\D", "", girdi)

    if len(sadece_rakam) == 3:
        kisa_sonuc = kisa_numara_sorgula(sadece_rakam)
        if kisa_sonuc:
            return {"tur": "Kısa Numara", "veri": kisa_sonuc}
        return "Bu numara bizim dosyamızda yok"

    mnc_match = re.search(r"\((.*?)\)", girdi)
    if mnc_match:
        mnc = mnc_match.group(1).strip()
    else:
        if sadece_rakam.startswith("90"):
            mnc = sadece_rakam[2:5]
        elif sadece_rakam.startswith("0"):
            mnc = sadece_rakam[1:4]
        else:
            mnc = sadece_rakam[:3]

    cografi_sonuc = cografi_sorgula(mnc)
    if cografi_sonuc:
        return {"tur": "Coğrafi Hat", "veri": cografi_sonuc}

    mobil_sonuc = mobil_sorgula(mnc)
    if mobil_sonuc:
        return {"tur": "Mobil Hat", "veri": mobil_sonuc}

    return "Bu numara bizim dosyamızda yok"

def menu_goster():
    print(ASCII_ART)
    print("=" * 80)
    print("                    NUMARA SORGULAMA SISTEMI v2.0")
    print("=" * 80)
    print("  [1] Numara Sorgula")
    print("  [2] Çıkış")
    print("=" * 80)

def main():
    while True:
        menu_goster()
        secim = input("\n[+] Seçiminiz (1-2): ").strip()

        if secim == "1":
            numara = input("\n[?] Sorgulanacak numarayı girin: ").strip()
            print("\n" + "-" * 40)
            print("[*] Sorgulanıyor...")
            sonuc = numara_sorgula(numara)

            print("-" * 40)
            if isinstance(sonuc, dict):
                print(f"[+] Hat Türü : {sonuc['tur']}")
                for k, v in sonuc["veri"].items():
                    print(f"[+] {k} : {v}")
            else:
                print(f"[-] {sonuc}")
            print("-" * 40 + "\n")
            input("Devam etmek için ENTER'a basın...")
        elif secim == "2":
            print("\n[-] Çıkış yapılıyor...")
            break
        else:
            print("\n[!] Geçersiz seçim! Tekrar deneyin.\n")

if __name__ == "__main__":
    main()
