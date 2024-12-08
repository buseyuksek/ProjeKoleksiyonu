__Not Defteri uygulaması__, kullanıcıların not ekleyip silebilmesine ve notlarını tarih sırasına göre görüntüleyebilmesine imkan tanır. 
Tüm notlar bir .txt dosyasında saklanır ve uygulama her açıldığında bu dosyadan veriler yüklenir.
Python programlama dili kullanılarak ve Nesne Yönelimli Programlama (OOP) prensiplerine uygun olarak geliştirilmiştir.

__Kullanılan Sınıflar__:
__Not Sınıfı__: Tek bir notun içeriğini ve tarih bilgisini saklar.
init Metodu:
content parametresi: Kullanıcının girdiği not içeriğini tutar.
date parametres: Notun tarihi ve saati. Eğer kullanıcı tarih vermezse, o anki tarih ve saat otomatik olarak atanır.
datetime.now().strftime("%Y-%m-%d %H:%M:%S") ifadesi, geçerli tarih ve saati YYYY-MM-DD HH:MM:SS formatında alır.

str Metodu: Bu metod, bir Not nesnesinin string (yazı) formatında temsilini döndürür.
Kullanıcı bir Not nesnesini yazdırdığında, bu metod çağrılır ve Not nesnesinin tarih ve içeriği birleştirilerek okunabilir bir şekilde ekrana yazdırılır.

__NotDefteri Sınıfı__: Notların eklenmesi, silinmesi, listelenmesi ve dosya işlemlerini yönetir.
__Özellikler__:
notes: Uygulamada kayıtlı olan notların listesidir.
filename: Notların saklandığı dosyanın adıdır (notes.txt).
__Yöntemler:__
add_note(content: str): Yeni bir not ekler ve not listesini tarih sırasına göre sıralar.
delete_note(content: str): İçeriği verilen notu siler.
list_notes(): Tüm notları ekrana yazdırır.
save_notes(): Not listesini dosyaya kaydeder.
load_notes(): Dosyada kayıtlı notları yükler.
