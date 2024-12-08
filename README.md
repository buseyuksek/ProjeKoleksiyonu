Film Yönetim Sistemi, kullanıcıların film koleksiyonlarını kolayca yönetmelerine yardımcı olan bir Python uygulamasıdır. 
Bu sistem sayesinde kullanıcılar filmleri ekleyebilir, silebilir ve listeleyebilir. 
Listeleme işlemi sırasında filmleri tür veya yıla göre filtrelemek de mümkün.

Özellikler
Film Ekleme: Film adı, yönetmen, yıl ve tür bilgilerini girerek yeni bir film ekleyebilirsiniz.
Film Silme: Koleksiyonunuzdan istediğiniz bir filmi kaldırabilirsiniz.
Filmleri Listeleme: Tüm filmleri görüntüleyebilir veya belirli bir türe/yıla göre filtreleme yapabilirsiniz.

Proje Yapısı:
film.py: Film sınıfını barındırır ve bir film nesnesinin ad, yönetmen, yıl ve tür bilgilerini saklar.
film_yoneticisi.py: FilmYoneticisi sınıfını içerir ve film ekleme, silme ve listeleme işlemlerini yönetir.
main.py: Kullanıcı arayüzünü (komut satırı üzerinden) kontrol eder ve kullanıcıdan giriş alır.
