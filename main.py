from film_yoneticisi import FilmYoneticisi

def main():
    yonetici = FilmYoneticisi()

    while True:
        print("\n=== Film Yönetim Sistemi ===")
        print("1. Film Ekle")
        print("2. Film Sil")
        print("3. Filmleri Listele")
        print("4. Çıkış")

        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            ad = input("Film adı: ")
            yonetmen = input("Yönetmen: ")
            yil = int(input("Yıl: "))
            tur = input("Tür: ")
            yonetici.film_ekle(ad, yonetmen, yil, tur)

        elif secim == "2":
            film_adi = input("Silinecek film adı: ")
            yonetici.film_sil(film_adi)

        elif secim == "3":
            print("Filtre seçenekleri (boş bırakabilirsiniz):")
            filtre_tur = input("Tür: ")
            filtre_yil = input("Yıl: ")
            filtre_yil = int(filtre_yil) if filtre_yil else None
            yonetici.filmleri_listele(filtre_tur, filtre_yil)

        elif secim == "4":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
