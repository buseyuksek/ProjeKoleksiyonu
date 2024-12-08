class Film:  #film nesnesi oluşturulur
    def __init__(self, ad, yonetmen, yil,tur):  #film nesnesine özellikler atanır
        self.ad = ad
        self.yonetmen = yonetmen
        self.yil = yil
        self.tur = tur

    def __str__(self):  #film nesnesini okunabilir döndürmek için __str__ metodu kullanılır.
        return f"{self.ad} ({self.yil}) - Yönetmen: {self.yonetmen}, Tür: {self.tur}"