# tuple nedir
def main():
    student = get_student()
    print(f"Name: {student[0]} , from {student[1]}")

def get_student():
    name = input("Enter your name: ")
    country = input("Enter your country: ")
    return (name, country)  # eger parantez yerine koseli parantez olsa idi , bu bir list olurdu .

if __name__ == "__main__":
    main()

# =====================================================================
# TUPLE (DEMET) NOTLARI
# =====================================================================
# 1. TEMEL MANTIK:
# - Tuple, birden fazla veriyi bir arada tutan kilitli bir veri tipidir.
# - En önemli özelliği 'IMMUTABLE' yani DEĞİŞTİRİLEMEZ olmasıdır.
# - Bir kez oluşturulduktan sonra eleman eklenemez, silinemez veya güncellenemez.
#
# 2. TANIMLAMA VE SİHİRLİ VİRGÜL:
# - Tuple oluşturan ana unsur PARANTEZ Değil, VİRGÜL (,) işaretidir.
# - Örnek: nokta = 10, 20  --> Bu ifade otomatik olarak bir Tuple olur.
# - Örnek: nokta = (10, 20) --> Okunabilirliği artırmak için genelde parantezli yazılır.
# - Tek elemanlı Tuple yapmak için virgül şarttır: tekil = (5,) veya tekil = 5,
#
# 3. VERİYE ERİŞİM (INDEX & UNPACKING):
# - İndeks ile erişim:
#   koordinat = (10, 20)
#   x = koordinat[0]  # 10
#   y = koordinat[1]  # 20
#
# - Paket Açma (Unpacking) yöntemi:
#   x, y = koordinat  # x=10, y=20 olur.
#
# 4. NEDEN TUPLE KULLANILIR?:
# - Güvenlik: Kaza sonucu verinin (örn: sabit koordinat, RGB renk kodu) değişmesini engeller.
# - Hız: Listelere (list) göre bellek (RAM) dostudur ve Python tarafında daha hızlı işlenir.
# - Fonksiyon Çıktıları: 'return a, b' yapıldığında veriler başka fonksiyona kilitli paket olarak gider.
# =====================================================================

# class 

class Student:
    ...

def main():
    student = get_student()
    print(f"Name: {student.name} , from {student.country}")

def get_student():
    student = Student()
    student.name = input("Enter your name: ")
    student.country = input("Enter your country: ")
    return student

if __name__ == "__main__":
    main()






class Student:
    def __init__(self, name, country):
        self.name = name
        self.country = country

def main():
    student = get_student()
    print(f"Name: {student.name} , from {student.country}")

def get_student():
    name = input("Enter your name: ")
    country = input("Enter your country: ")
    return Student(name, country)

if __name__ == "__main__":
    main()

# ==============================================================================
# 📌 __init__() Metodu (Constructor / Yapıcı Metod)
# ==============================================================================
#
# 1. Ne İşe Yarar?
#    * Bir sınıftan YENİ BİR NESNE türetildiği an otomatik olarak çalışan ilk fonksiyondur.
#    * Nesnenin kimlik bilgilerini (özelliklerini/değişkenlerini) tanımlamaya ve
#      başlangıç değerlerini atamaya yarar.
#
# 2. self Parametresi Nedir?
#    * O an oluşturulmakta olan "canlı nesnenin kendisini" temsil eder.
#    * 'self.name = name' demek: "Dışarıdan gelen 'name' verisini al, o anki nesnenin
#      içindeki 'name' kutusuna kaydet" demektir.
#
# 3. Örnek Kullanım:
#    class Student:
#        def __init__(self, name, country):
#            self.name = name         # Nesnenin adı
#            self.country = country   # Nesnenin ülkesi
#
#    student1 = Student("Semih", "Türkiye") # Otomatik __init__ çalışır!
#
# ==============================================================================







# hata algilama ve duzeltme

class Student:
    def __init__(self, name, country):
       if not name:
           raise ValueError("Name is required")
       if country not in ["USA", "Canada", "UK"]:
           raise ValueError("Country is required")
       self.name = name
       self.country = country






class Student:
    def __init__(self, name, country):
        if not name:
            raise ValueError("Name is required")
        if country not in ["USA", "Canada", "UK"]:
            raise ValueError("Country is required")
        self.name = name
        self.country = country
    def __str__(self):
        return f"Student(name={self.name} , country={self.country})"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Enter your name: ")
    country = input("Enter your country: ")
    return Student(name, country)

if __name__ == "__main__":
    main()

# 📌 __str__() : print(nesne) yazıldığında anlamsız bellek adresi yerine
# nesnenin kendini insan dilinde anlatan temiz metin çıktısını döndürür.






class Student:
    def __init__(self, name, country):
        if not name:
            raise ValueError("Name is required")
        if country not in ["USA", "Canada", "UK"]:
            raise ValueError("Country is required")
        self.name = name
        self.country = country
    def __str__(self):
        return f"Student(name={self.name} , country={self.country})"
    def charm(self):
        match self.country:
            case "USA":
                return "Howdy!"
            case "Canada":
                return "Eh?"
            case "UK":
                return "Cheerio!"
            case _:
                return "Hello!"

def main():
    student = get_student()
    print(student)
    print(student.charm())
def get_student():
    name = input("Enter your name: ")
    country = input("Enter your country: ")
    return Student(name, country)

if __name__ == "__main__":
    main()








class Student:
    def __init__(self, name, country):
        # if not name:  # buradaki kontrole  setter daki kontrol ile artik ihtiyac kalmadi .
            # raise ValueError("Name is required")
        # if country not in ["USA", "Canada", "UK"]:  # buradaki kontrole  setter daki kontrol ile artik ihtiyac kalmadi .
            # raise ValueError("Country is required")
        self.name = name
        self.country = country
    def __str__(self):
        return f"Student(name={self.name} , country={self.country})"
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name is required")
        self._name = name
    @property
    def country(self):
        return self._country
    @country.setter
    def country(self, country):
        if country not in ["USA", "Canada", "UK"]:
            raise ValueError(" Invalid Country ")
        self._country = country

def main():
    student = get_student()
    print(student)
def get_student():
    name = input("Enter your name: ")
    country = input("Enter your country: ")
    return Student(name, country)

if __name__ == "__main__":
    main()

# ==============================================================================
# 📌 @property (Getter) ve Setter İçin Altın Notlar
# ==============================================================================
#
# 1. Amaç Nedir?
#    * Getter (@property): Veriyi dışarıya okuturken araya giren bekçidir.
#    * Setter (@isim.setter): Değişkene dışarıdan yeni bir değer atanırken
#      veriyi denetleyen güvenlik kalkanıdır.
#
# 2. Alt Tire (_) Kuralı (Hayat Kurtaran Detay):
#    * Sınıfın içinde asıl veriyi tutan gizli değişkenin başına tek alt tire
#      konulur (self._country).
#    * Eğer Setter veya Getter içinde alt tire koymayıp self.country yazarsan,
#      Python kendi kuyruğunu kovalayan kedi gibi sonsuz döngüye girer
#      (RecursionError).
#
# 3. Nasıl Çalışır?
#    * student.country yazıp okumak istediğinde arka planda Getter çalışır
#      ve sana self._country değerini döndürür.
#    * student.country = "USA" deyip veri atadığında arka planda Setter çalışır;
#      "USA" değerini kontrolden geçirip onaylarsa self._country içine yazar.
#    * Dışarıdan bakan biri arkadaki bu denetim mekanizmasını hiç görmez,
#      sanki normal bir değişkene erişiyormuş gibi temiz bir kullanım sunar.
#
# ==============================================================================

# ONEMLI BIR MESELE !!! 
# 1. Sağ Taraf (country - Parametre):
# Bu, kullanıcının dışarıdan fonksiyona verdiği ham değerdir (örneğin "USA").
# 2. Sol Taraf (self._country - Nesnenin Kendi Hafızası):
# Bu ise sınıfın içindeki gizli hafıza kutusudur.
# Eşittir işareti (=) Python'da her zaman "Sağdakini al, soldakinin içine at" demektir.
# Yani o satır Türkçe olarak tam olarak şunu söyler:
# "Kullanıcının gönderdiği o "USA" kelimesini al (country), benim nesnemin arkasındaki o gizli hafıza kutusuna (self._country) kaydet!"

# ==============================================================================
# 📌 type() Fonksiyonu Hakkında Kısa Not
# ==============================================================================
#
# 1. Ne İşe Yarar?
#    * type(veri): Bir değişkenin veya değerin CİNSİNİ / TÜRÜNÜ söyler.
#    * Python'da her veri tipi aslında önceden yazılmış bir sınıftır (class).
#
# 2. Temel Veri Tipleri:
#    * type(50)      --> <class 'int'>    (Tam Sayı)
#    * type(3.14)    --> <class 'float'>  (Ondalıklı Sayı)
#    * type("Semih") --> <class 'str'>    (Metin / String)
#    * type(True)    --> <class 'bool'>   (Mantıksal Doğru/Yanlış)
#
# 3. Kendi Sınıflarında (OOP):
#    * student = Student("Semih", "USA")
#    * type(student) --> <class '__main__.Student'>
#      (Senin oluşturduğun özel sınıfa ait bir nesne olduğunu gösterir)
#
# ==============================================================================

import random

class Ogrenci:
    def __init__(self):
        self.countrys = ["USA", "Canada", "UK"]
    def sort(self, isim):
        print(isim, "is from" , random.choice(self.countrys))
ogrenci = Ogrenci()
ogrenci.sort("Mehmet")



class Ogrenci:
    # Bu sınıfın tüm örneklerinde ortak olan verileri burada tanımlıyoruz.
    countrys = ["USA", "Canada", "UK"]
    @classmethod
    def sort(cls, isim):
        print(isim, "is from" , random.choice(cls.countrys))
Ogrenci.sort("Mehmet")

# 📌 @classmethod & cls : Nesne üretmeden (Ogrenci()) doğrudan sınıfa (Ogrenci.sort()) erişim sağlar.
# 'self' tek bir canlı nesneyi temsil ederken, 'cls' doğrudan sınıfın kendisini temsil eder.
# Nesneye özel verilerle işimiz yoksa, gereksiz nesne oluşturmayıp hafızayı (RAM) korumamızı sağlar.

# simdi ise biraz daha isi farklilastirip , o ana kodumuzda bazi sadelestirmeler yapalim.

class Student:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    def __str__(self):
        return f"Student(name={self.name} , country={self.country})"
    @classmethod
    def get(cls):
        name = input("Enter your name: ")
        country = input("Enter your country: ")
        return cls(name, country)  # cls() ile nesne üretimi
def main():
    student = Student.get()  # Nesne üretimi ve veri alma tek satırda
    print(student)
if __name__ == "__main__":
    main()

# ==============================================================================
# 📌 @classmethod İle Alternatif Nesne Üretimi (Factory Method)
# ==============================================================================
#
# 1. 'Student.get()' çağrıldığında ortada henüz hiçbir nesne yokken doğrudan sınıfa ulaşılır.
# 2. 'cls' parametresi doğrudan 'Student' sınıfının kendisini temsil eder.
# 3. 'get(cls)' metodu kullanıcıdan name ve country verilerini input ile alır.
# 4. 'return cls(name, country)' satırı aslında 'return Student(name, country)' demektir.
# 5. Bu işlem kullanıcıdan veriyi alıp tek hamlede yeni bir Student nesnesi üretir ve döndürür.
# 6. Avantajı: Nesne üretme ve veri alma mantığını sınıfın içine gömerek kodu tertemiz tutar.
#
# ==============================================================================

# ==============================================================================
# 📌 @staticmethod (Statik Metot) Nedir?
# ==============================================================================
#
# 1. Ne İşe Yarar?
#    * Sınıfın içine (class) yazılan ama sınıfın (cls) veya nesnenin (self) 
#      hiçbir verisini KULLANMAYAN normal bir yardımcı fonksiyondur.
#
# 2. @classmethod'dan Farkı Nedir?
#    * @classmethod -> İlk parametre olarak 'cls' alır (Sınıfın verilerine erişebilir).
#    * @staticmethod -> 'cls' veya 'self' ALMAZ! Sınıftan tamamen bağımsızdır.
#      Parantezinin içine ne self ne de cls yazılmaz.
#
# 3. Neden Sınıfın İçine Koyarız?
#    * Mantıken o sınıfla (örneğin Student veya Drone ile) İLGİLİDİR ama 
#      çalışmak için sınıfın verilerine ihtiyacı yoktur. Kodun düzenli durması 
#      ve ilgili fonksiyonlar bir arada olsun diye sınıfın içine saklanır.
#
# 4. Örnek Kullanım:
#    class Student:
#        @staticmethod
#        def okul_kurallarini_goster(): # İçinde self veya cls YOK!
#            print("1. Sessiz ol, 2. Geç kalma")
#
#    # Nesne üretmeden doğrudan çağrılabilir:
#    Student.okul_kurallari_goster()
# ==============================================================================

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Name is required")
        self.name = name
        ...
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)  # Wizard sınıfının __init__() metodunu çağırır
        self.house = house
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)  # Wizard sınıfının __init__() metodunu çağırır
        self.subject = subject
wizard = Wizard("Albus Dumbledore")
student = Student("Harry Potter", "Gryffindor")
professor = Professor("Severus Snape", "Potions")

# ==============================================================================
# 📌 Kalıtım (Inheritance) & super() Kullanımı Özeti
# ==============================================================================
#
# 1. Kalıtım (Inheritance), alt sınıfların üst sınıftan (Wizard) ortak özellikleri miras almasıdır[cite: 1].
# 2. 'class Student(Wizard):' ifadesi, Student'ın bir Wizard (Ata Sınıf) olduğunu belirtir[cite: 1].
# 3. Ortak değişkenleri (örneğin 'name') her alt sınıfta tekrar tanımlamak yerine ata sınıfta tutarız.
# 4. 'super().__init__(name)' satırı, isim kaydetme işini üstteki Wizard sınıfına devreder[cite: 1].
# 5. Alt sınıflar sadece kendilerine özel verileri (örn: 'house', 'subject') kendi içinde kaydeder[cite: 1].
# 6. Miras alınan verilere erişirken hiçbir şey değişmez: 'student.name' veya 'self.name' ile çağrılır.
#
# ==============================================================================
# ==============================================================================
# 📌 Kalıtım (Inheritance) İle Oluşturulan Nesneleri Çağırma
# ==============================================================================
#
# 1. wizard = Wizard("Albus Dumbledore") -> Doğrudan ata sınıftan temel bir büyücü üretir.
# 2. student = Student("Harry Potter", "Gryffindor") -> Öğrenci nesnesini üretir.
# 3. super().__init__(name) sayesinde "Harry Potter" ismi ata sınıf olan Wizard'a kaydolur[cite: 1].
# 4. self.house = house sayesinde "Gryffindor" bilgisi sadece öğrenciye özel kaydedilir[cite: 1].
# 5. Çağırırken hiçbir karmaşa yoktur: 'student.name' veya 'professor.name' yazarak isimlere erişilir.
# 6. Özetle: Miras almak veri çağırma yöntemini değiştirmez, sadece sınıf yazarken kod tekrarını önler.
#
# ==============================================================================

# ==============================================================================
# 📌 Python Hata Hiyerarşisi (BaseException vs Exception)
# ==============================================================================
#
# 1. BaseException: Python'daki tüm hataların en tepesindeki ata (kök) sınıftır[cite: 2].
# 2. KeyboardInterrupt: Klavyeden Ctrl+C ile programı kapatma olayını temsil eder[cite: 2].
# 3. Exception: Bizim kodlarımızda oluşan tüm mantıksal hataların (ValueError, ZeroDivisionError vb.) ata sınıfıdır[cite: 2].
# 4. Kural: Kod yazarken 'except BaseException' KULLANILMAZ! Çünkü programın Ctrl+C ile kapanmasını engeller[cite: 2].
# 5. Doğru Kullanım: Hata yakalarken 'except Exception' veya 'except ValueError' gibi spesifik sınıflar kullanılır[cite: 2].
#
# ==============================================================================
# 📌 Hata Yakalamada 'except Exception as e' Kullanımı
# ==============================================================================

# try:
  # sayi = int(input("Bir sayı girin: "))
  # sonuc = 10 / sayi
  # print(f"Sonuç: {sonuc}")

# except Exception as e:
  # print(f"Bir hata oluştu: {e}")

# ------------------------------------------------------------------------------
# 💡 NOT: 
# 1. 'except Exception as e' kalıbı, kodda ne hatası çıkarsa çıksın programı 
#    patlatmadan hatayı 'e' adındaki değişkene paketler ve yakalar[cite: 2].
# 2. 'BaseException' yerine 'Exception' seçilmesinin sebebi; kullanıcının 
#    terminalde Ctrl+C yapıp programı kapatma isteğini (KeyboardInterrupt) engellememektir[cite: 2].
# ==============================================================================

class Vault:
    def __init__(self, galleons=0 , sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        def __str__(self):
            return f"Vault(galleons={self.galleons} , sickles={self.sickles} , knuts={self.knuts})"
potter = Vault(100 , 50 , 25)
print(potter)
weasley = Vault(25 , 50 , 100)
print(weasley)

galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

total = Vault(galleons, sickles, knuts)
print(total)

# opeator overloading ile simdi isi daha guzel ve temiz bir hale getirelim.

class Vault:

  def __init__(self, galleons=0, sickles=0, knuts=0):
    self.galleons = galleons
    self.sickles = sickles
    self.knuts = knuts

  def __str__(self):
    return f"Vault(galleons={self.galleons}, sickles={self.sickles}, knuts={self.knuts})"

  def __add__(self, other):
    galleons = self.galleons + other.galleons
    sickles = self.sickles + other.sickles
    knuts = self.knuts + other.knuts
    return Vault(galleons, sickles, knuts)
potter = Vault(100 , 50 , 25)
print(potter)
weasley = Vault(25 , 50 , 100)
print(weasley)
total = potter + weasley
print(total)

# ==============================================================================
# 📌 Operator Overloading (Operatör Aşırı Yüklemesi)
# ==============================================================================
#
# 1. ' + ', ' - ', ' == ', ' > ' gibi operatörlerin kendi sınıflarımızda nasıl davranacağını belirler.
# 2. Her operatör arka planda gizli bir dunder metoda bağlıdır (Örn: '+' -> __add__, '==' -> __eq__).
# 3. 'def __add__(self, other):' yazarak iki nesne '+' ile toplandığında ne olacağını biz tanımlarız.
# 4. Amacı: Kodu 'drone1 + drone2' şeklinde çok daha okunabilir ve doğal hale getirmektir.
#
# ==============================================================================
# ==============================================================================
# 📌 Operatörlerde 3 veya Daha Fazla Nesneyi Toplama Mantığı
# ==============================================================================
#
# 1. Python '+' operatörünü çalıştırırken d1 + d2 + d3 ifadesini adım adım ikili çözer.
# 2. 'def __add__(self, other):' metoduna 3. bir parametre (other2) EKLENMEZ.
# 3. Metodun 'return Vault(...)' gibi YENİ BİR NESNE döndürmesi sağlanır.
# 4. Böylece (v1 + v2) birleşip yeni bir nesne olur, ardından o da v3 ile toplanır.
# 5. Zincirleme toplama sayesinde sınırsız sayıda nesne '+' ile yan yana toplanabilir.
#
# ==============================================================================

# 3. Static Methods (@staticmethod)
# ------------------------------------------------------------------------------
# * Bir sınıf (Class) içinde tanımlanan ama ne 'self' ne de 'cls' parametresi alan 
#   bağımsız fonksiyonlardır.
# * Sınıftan canlı nesne üretmeye (Ogrenci()) gerek kalmadan doğrudan 
#   'SinifAdi.fonksiyon()' şeklinde çağrılabilir.
