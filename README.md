Not Defteri uygulaması, kullanıcıların not ekleyip silebilmesine ve notlarını tarih sırasına göre görüntüleyebilmesine imkan tanır. 
Tüm notlar bir .txt dosyasında saklanır ve uygulama her açıldığında bu dosyadan veriler yüklenir.
Python programlama dili kullanılarak ve Nesne Yönelimli Programlama (OOP) prensiplerine uygun olarak geliştirilmiştir.

Kullanılan Sınıflar:
-Not Sınıfı: Tek bir notun içeriğini ve tarih bilgisini saklar.
-NotDefteri Sınıfı: Notların eklenmesi, silinmesi, listelenmesi ve dosya işlemlerini yönetir.
Özellikler:
notes: Uygulamada kayıtlı olan notların listesidir.
filename: Notların saklandığı dosyanın adıdır (notes.txt).
Yöntemler:
add_note(content: str): Yeni bir not ekler ve not listesini tarih sırasına göre sıralar.
delete_note(content: str): İçeriği verilen notu siler.
list_notes(): Tüm notları ekrana yazdırır.
save_notes(): Not listesini dosyaya kaydeder.
load_notes(): Dosyada kayıtlı notları yükler.
