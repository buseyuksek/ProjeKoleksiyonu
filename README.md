__Film Yönetim Sistemi,__ kullanıcıların film koleksiyonlarını kolayca yönetmelerine yardımcı olan bir Python uygulamasıdır. 
Bu sistem sayesinde kullanıcılar filmleri ekleyebilir, silebilir ve listeleyebilir. 
Listeleme işlemi sırasında filmleri tür veya yıla göre filtrelemek de mümkün.

__Özellikler:__
1-Film Ekleme: Film adı, yönetmen, yıl ve tür bilgilerini girerek yeni bir film ekleyebilirsiniz.
2-Film Silme: Koleksiyonunuzdan istediğiniz bir filmi kaldırabilirsiniz.
3-Filmleri Listeleme: Tüm filmleri görüntüleyebilir veya belirli bir türe/yıla göre filtreleme yapabilirsiniz.

__Proje Yapısı:__
film.py: Film sınıfını barındırır ve bir film nesnesinin ad, yönetmen, yıl ve tür bilgilerini saklar.
film_yoneticisi.py: FilmYoneticisi sınıfını içerir ve film ekleme, silme ve listeleme işlemlerini yönetir.
main.py: Kullanıcı arayüzünü (komut satırı üzerinden) kontrol eder ve kullanıcıdan giriş alır.

__Film Sınıfı:__
__init__(self, ad, yonetmen, yil, tur): Bu metot,bir film nesnesi oluşturulurken devreye girer. Filmin adını, yönetmenini, çıkış yılını ve türünü parametre olarak alır ve bu bilgileri sınıfın özelliklerine (self.ad, self.yonetmen, self.yil, self.tur) atar.
__str__(self): Bu metod, filmin adını, yönetmenini, çıkış yılını ve türünü içeren bir string döndürür.


__FilmYoneticisi Sınıfı:__
__init__(self): Bu metod, FilmYoneticisi sınıfının bir örneği oluşturulduğunda çağrılır. self.filmler listesi başlatılır ve filmleri burada tutarız.

film_ekle(self, ad, yonetmen, yil, tur): Bu metod ile yeni bir film eklenebilir. Parametreler olarak filmin adı, yönetmeni, çıkış yılı ve türü alınır.

film_sil(self, film_adi): Bu metod ile adı verilen filmi listeden silinir. Eğer film bulunursa, listeden silinir ve kullanıcıya bildirilir.

filmleri_listele(self, filtre_tur=None, filtre_yil=None): Bu metod, filmleri listeler. Kullanıcı tür veya yıl filtreleme parametreleri verebilir. Filtreler varsa, sadece verilen tür veya yıl ile eşleşen filmler listelenir. Eğer filtre yoksa, tüm filmler gösterilir.
