# assert (Birim Doğrulama):
# Mantık: assert <koşul> → Koşul True ise kod akmaya devam eder, False ise program AssertionError verip patlar.
# Kullanım Amacı: Fonksiyonların beklediğimiz çıktıyı üretip üretmediğini elle terminalde test etmek yerine otomatik kontrol etmektir.

# ornek kullanim sekilleri;
# def test_square():
     # try:
        # assert square(2) == 4
     # except AssertionError:
        # print("2 squared was not 4")
     # try:
         # assert square(3) == 9
     # except AssertionError:
         # print("3 squared was not 9")

# Python’a şu emri verirsin: "Bu ifadenin doğru (True) olduğunu varsayıyorum. Eğer yanlışsa (False), programı derhal durdur ve bana bağırma!"
# Normalde kodun hatalı çalışırsa yanlış bir çıktı verir ve sessizce devam eder (bu en tehlikeli durumdur). assert ise bir kural çiğnendiğinde sistemi anında kilitler.

# def karesini_al(x):
    # return x * x

# Kontrol: karesini_al(5) gerçekten 25 mi?
# assert karesini_al(5) == 25

# Eğer sonuç 25 ise: Python hiçbir şey demez, alt satıra geçer (Sessiz onay).
#Eğer sonuç 25 değilse: Python AssertionError fırlatır ve programı orada bitirir.
        
# pytest ile uzun uzun try except yazmaktansa artik bize daha kullanilabilir sistem veriliyo. 
# Artik try except kullanmadan sadece assert ile kontrol kodumuzu yazip , terminale pytest lecture5.py yazdigimizda sistem artik bize hata nin nerede oldugunu soyleyecek eger hata yok ise sistem akicak .
# pytest sayesinde direkt;

#  def test_square():
#      assert square(2) == 4
#      assert square(3) == 9
#      assert square(-2) == 4
#      assert square(-3) == 9
#      assert square(0) == 0

# boylece daha pratik bir kontrol kodu insa ettik.

# TypeError (Veri Tipi Hatası):
# Nedir? Bir işlemin veya fonksiyonun, desteklemediği/uyumsuz bir veri tipiyle çağrılması durumunda Python'ın fırlattığı hatadır.
# Ne Zaman Olur?

# 5 + "10" (Sayı + Metin birleşimi)

# "metin" / 2 (Metin üzerinde geçersiz matematik)

# len(100) (Sayılar üzerinde uzunluk alma gibi uyumsuz fonksiyon kullanımı)

# Nasıl Çözülür/Yakalanır? Tip dönüşümü yapılarak (int(), str()) veya try / except TypeError: bloğu ile yakalanarak.
# Bir cozum seklide ; 

# def test_str():
     # with pytest.raises(TypeError):
         # square("cat")

# pytest.raises (Beklenen Hata Testi):
# Nedir? Fonksiyona hatalı/bozuk veri gönderildiğinde, fonksiyonun doğru hata tipini fırlatıp fırlatmadığını denetleyen pytest yapısıdır.
# Mantık: with pytest.raises(HataTipi): bloğu içindeki kod belirtilen hatayı verirse test geçer, hata vermezse veya farklı bir hata verirse test kalır.
# Ne Zaman Kullanılır? ValueError, TypeError veya ZeroDivisionError gibi beklenen güvenlik/istisna durumlarını otomatik test etmek için.

# Package (Paket):

# Nedir? Birden fazla .py (modül) dosyasını tek bir çatı altında düzenli tutan kod klasörüdür.
# init.py: Bir klasörün içine __init__.py isimli dosya koyduğunda, Python o klasörü sıradan bir klasör değil, içinden kod çekilebilir bir Package olarak kabul eder.
# PyPI (pip): Başkalarının yazdığı paketlerin (örneğin pytest, matplotlib) indirildiği küresel paket deposudur. pip install paket_adi komutuyla bilgisayara kurulur.

