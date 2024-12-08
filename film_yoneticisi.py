from film import Film  

class FilmYoneticisi:
    def __init__(self):
        self.filmler = []  #film nesnelerini saklayan bir listedir.

    def film_ekle(self, ad, yonetmen, yil, tur):  #film ekleme işlemi için kullanılır.
        yeni_film = Film(ad, yonetmen, yil, tur)
        self.filmler.append(yeni_film)
        print(f"Film eklendi: {yeni_film}")

    def film_sil(self, film_adi):
        for film in self.filmler:
            if film.ad.lower() == film_adi.lower():
                self.filmler.remove(film)
                print(f"Film silindi: {film}")
                return
        print("Film bulunamadı.")

    def filmleri_listele(self, filtre_tur=None, filtre_yil=None):
        if not self.filmler:
            print("Henüz eklenmiş bir film yok.")
            return

        print("=== Film Listesi ===")
        for film in self.filmler:
            if (filtre_tur and film.tur.lower() != filtre_tur.lower()) or \
               (filtre_yil and film.yil != filtre_yil):
                continue
            print(film)
