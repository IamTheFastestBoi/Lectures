students = [{"name": "Hermione" , "house": "Gryffindor"}, 
            {"name": "Harry" , "house": "Gryffindor"}, 
            {"name": "Draco" , "house": "Slytherin"}]
houses = set()
for student in students:
    houses.add(student["house"])
for house in sorted(houses):
    print(house)

# ==============================================================================
# 📌 set (Kümeler) Notları
# ==============================================================================
#
# 1. TEMEL MANTIK:
#    * Tekrarsız (unique) ve sırasız (unordered) veri tutan koleksiyon tipidir.
#    * Aynı elemandan 100 tane de eklesen küme içinde SADECE 1 TANE tutulur.
#
# 2. OLUŞTURMA:
#    * kume = {"A", "B", "C"} veya liste_temiz = set(eski_liste)
#    * Boş küme oluştururken 'kume = {}' YAZILMAZ (O Dictionary olur!). 
#      Boş küme için 'kume = set()' yazılır.
#
# 3. KULLANIM ALANLARI:
#    * Listelerdeki mükerrer/tekrarlayan verileri saniyeler içinde temizlemek.
#    * 'x in kume' şeklinde devasa verilerde eleman varlığı sorgulama hızını katlamak.
#    * Kesişim (&), Birleşim (|) ve Fark (-) gibi matematiksel işlemleri yapmak.
#
# 4. KISITLAMA:
#    * Kümelerin sırası olmadığı için 'kume[0]' şeklinde indeks ile eleman çağrılamaz.
#
# ==============================================================================

balance = 0
def main():
    print("Balance: ", balance)
    deposit(100)
    withdraw(50)
    print("Balance: ", balance)
def deposit(n):
    global balance
    balance += n
def withdraw(n):
    global balance
    balance -= n
if __name__ == "__main__":
    main()



# Dışarıda tanımladığın değişken: Fonksiyonun içinden okunabilir.
# Ama o değişkeni bir def fonksiyonunun İÇİNDE güncellemek/değiştirmek istersen: Python'a "Dur, bu yeni bir değişken değil, dışarıdaki asıl değişken!" demek için fonksiyonun içine global komutunu vermek zorundasın.

import mypy

def meow(n: int) -> None:
    for _ in range(n):
        print("meow")
number : int = input("Number: ")
meow(number)

# mypy bizim icin yazdigimiz koddaki bug lari bulmak icin kullanilir.

# ==============================================================================
# 📌 Fonksiyonlarda '-> None' Tanımlaması
# ==============================================================================
#
# 1. 'def fonksiyon() -> None:' yapısı, fonksiyonun 'return' yapmadığını belirtir.
# 2. Sadece ekrana çıktı veren, dosyaya yazan veya veritabanını güncelleyen 
#    ama geriye değer döndürmeyen fonksiyonlarda kullanılır.
# 3. 'mypy' gibi araçların 'None' dönen bir fonksiyonu değişkene atama hatalarını 
#    yakalamasını sağlar.
#
# ==============================================================================
# ==============================================================================
# 📌 Fonksiyonlarda '-> str' Tanımlaması
# ==============================================================================
#
# 1. 'def fonksiyon() -> str:' ifadesi, fonksiyonun geriye 'str' (metin) türünde 
#    bir değer döndüreceğini (return) ifade eder.
# 2. Fonksiyonun içinde mutlaka bir 'return ...' satırı bulunmalıdır.
# 3. 'mypy' bu kurala bakarak, dönen sonucun metin olup olmadığını ve doğru 
#    değişkenlere atanıp atanmadığını denetler.
#
# ==============================================================================

#  Yorum Satırları (#) vs. Dokümantasyon Metinleri (""")
# ------------------------------------------------------------------------------
# * # (Diyez): Kodun içindeki mantığı, karmaşık satırları veya geliştirici notlarını
#   açıklamak için kullanılır.
# * """ (Docstring): Fonksiyon veya sınıfların en üstüne yazılır; editörlerde (IDE)
#   mouse ile üzerine gelindiğinde açılan ipucu pencerelerini oluşturur.
#
# ==============================================================================

import argparse
parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n" , help = "number of times to meow" , type = int , default = 1)
args = parser.parse_args()
for _ in range(args.n):
    print("meow")

# ==============================================================================
# 📌 PYTHON 'argparse' MODÜLÜ VE KOMUT SATIRI ARGÜMANLARI
# ==============================================================================
#
# 1. argparse Nedir ve Ne İşe Yarar?
# ------------------------------------------------------------------------------
# * Python'ın yerleşik bir kütüphanesidir; komut satırından (terminal) çalıştırılan
#   script'lere parametre/bayrak (flag) geçmeyi profesyonelleştirir.
# * 'sys.argv' yerine daha güvenli, esnek ve okunaklı bir alternatif sunar.
#
# 2. sys.argv Kullanımına Göre Avantajları
# ------------------------------------------------------------------------------
# * Sıra Bağımsızlığı: Parametre sırası önemli değildir (-n 5 -f dosya.txt ile 
#   -f dosya.txt -n 5 aynı şekilde çalışır).
# * Otomatik Tip Dönüşümü: Verileri otomatik olarak 'int', 'float' vb. türlere 
#   dönüştürür (Manuel int() çevrimi yapmaya ve try-except yazmaya gerek kalmaz).
# * Otomatik Yardım Menüsü: Terminale '--help' veya '-h' yazıldığında 
#   kullanım kılavuzunu ve parametre listesini otomatik olarak basar.
# * Varsayılan Değerler (default): Kullanıcı bir parametre girmediğinde 
#   arka planda otomatik varsayılan değerler atayabilir.

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts
coins = [100, 50, 25]
print(total(*coins))  # unpacking 
# ==============================================================================
# 📌 PYTHON 'UNPACKING' (AMBALAJ / PAKET AÇMA)
# ==============================================================================
#
#  Unpacking Nedir ve Ne İşe Yarar?
# ------------------------------------------------------------------------------
# * Liste, demet (tuple) veya sözlük (dict) içindeki elemanları tek tek 
#   'liste[0]', 'liste[1]' diye çağırmak yerine, doğrudan değişkenlere veya 
#   fonksiyonlara tek hamlede dağıtmaya yarar.
# Liste unpack etmek için * kullanılır. 
# Dict unpack etmek için ** kullanılır.

def f(*args, **kwargs):
    print("Positional arguments:", args)

f(100, 50, 25 , 5)

def g(*args, **kwargs):
    print("Named arguments:", kwargs)

g(galleons=100, sickles=50, knuts=25)

# ==============================================================================
# 📌 PYTHON *args VE **kwargs (ESNEK PARAMETRELER)
# ==============================================================================
#
# 1. *args (Positional Arguments)
# ------------------------------------------------------------------------------
# * Fonksiyona sınırsız sayıda 'isimsiz/konumsel' argüman geçilmesini sağlar.
# * Gelen tüm verileri bir TUPLE (demet) yapısı içinde toplar.
# * Örnek: def topla(*args):  -> args (1, 2, 3) şeklinde okunur.
#
# 2. **kwargs (Keyword Arguments)
# ------------------------------------------------------------------------------
# * Fonksiyona sınırsız sayıda 'isimli' (key=value) argüman geçilmesini sağlar.
# * Gelen tüm verileri bir DICTIONARY (sözlük) yapısı içinde toplar.
# * Örnek: def kayit(**kwargs): -> kwargs {'ad': 'Semih'} şeklinde okunur.
#
# 3. Sıralama Kuralı (Fonksiyon Tanımlarken)
# ------------------------------------------------------------------------------
# 1. Normal Parametreler  (örn: a, b)
# 2. *args               (isimsiz esnek parametreler)
# 3. **kwargs            (isimli esnek parametreler)
#
# Örnek: def fonksiyon(sabit, *args, **kwargs):
#
# ==============================================================================

def main():
    yell("This" , "is" , "CS50")
def yell(*words):
    uppercased = map(str.upper , words)
    print(*uppercased)
if __name__ == "__main__":
    main()

# ==============================================================================
# 📌 PYTHON 'map()' FONKSİYONU
# ==============================================================================
#
# 1. map() Nedir ve Ne İşe Yarar?
# ------------------------------------------------------------------------------
# * Bir fonksiyonu, bir koleksiyondaki (liste, tuple vb.) TÜM elemanlara 
#   tek tek uygulamak için kullanılır.
# * Manuel 'for' döngüsü yazma ihtiyacını ortadan kaldırır.
#
# 2. Önemli Kurallar
# ------------------------------------------------------------------------------
# * İlk parametre fonksiyonun ADIDIR (fonksiyon çağrılmaz, örn: 'int()' değil 'int').
# * Tembel Çalışma (Lazy Evaluation): 'map()' geriye bir map objesi döndürür. 
#   Ekranda basmak veya kullanmak için 'list(map(...))' şeklinde sarmalanmalıdır.

def main():
    yell("This" , "is" , "CS50")
def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)
if __name__ == "__main__":
    main()

# ==============================================================================
# 📌 PYTHON LIST COMPREHENSION (LİSTE KAVRAYIMI)
# ==============================================================================
#
# 1. Nedir ve Ne İşe Yarar?
# ------------------------------------------------------------------------------
# * Boş liste oluşturup 'for' döngüsü ve '.append()' ile eleman eklemek yerine
#   yeni listeyi TEK SATIRDA oluşturmayı sağlar.
# * Kodun daha kısa, temiz ve performanslı çalışmasını sağlar.
#
# 2. Genel Kalıp (Formül)
# ------------------------------------------------------------------------------
# yeni_liste = [ ifade  for eleman in veri_kaynagi  if kosul ]
#
# 3. Karşılaştırmalı Örnekler
# ------------------------------------------------------------------------------
# sayilar = [1, 2, 3, 4, 5, 6]

# Örnek A: Tüm sayıların 2 katını alma
# iki_kati = [x * 2 for x in sayilar]  # [2, 4, 6, 8, 10, 12]

# Örnek B: Sadece 3'ten büyük olanları filtreleyip alma
# buyukler = [x for x in sayilar if x > 3]  # [4, 5, 6]
#
# ==============================================================================

# bir ornek daha:
students = [{"name": "Hermione" , "house": "Gryffindor"}, 
            {"name": "Harry" , "house": "Gryffindor"},
            {"name": "Draco" , "house": "Slytherin"}]
gryffindors = [student["name"] for student in students if student["house"] == "Gryffindor"]
for gryffindor in sorted(gryffindors):
    print(gryffindor)
# ==============================================================================

students = [{"name": "Hermione" , "house": "Gryffindor"}, 
            {"name": "Harry" , "house": "Gryffindor"},
            {"name": "Draco" , "house": "Slytherin"}]
def is_gryffindor(student):
    return student["house"] == "Gryffindor"
gryffindors = filter(is_gryffindor, students)
for gryffindor in sorted(gryffindors , key=lambda student: student["name"]):
    print(gryffindor["name"])

# ==============================================================================
# 📌 PYTHON 'filter()' FONKSİYONU
# ==============================================================================
#
# 1. filter() Nedir ve Ne İşe Yarar?
# ------------------------------------------------------------------------------
# * Bir koleksiyondaki (liste, tuple vb.) elemanları belirli bir koşula göre 
#   süzmek/ayıklamak için kullanılır.
# * Fonksiyon her bir eleman için 'True' dönüyorsa o eleman tutulur, 
#   'False' dönüyorsa listeden elenir.
#
# 2. Önemli Kurallar
# ------------------------------------------------------------------------------
# * 'map()' gibi 'filter()' da geriye bir filter objesi döndürür. 
#   Sonucu liste olarak almak için 'list(filter(...))' yazılır.
# * İlk parametre olarak 'None' geçilirse, listedeki boş/geçersiz (Falsy) 
#   değerleri (0, "", None, False) otomatik temizler.
#
# ==============================================================================
# 📌 PYTHON 'lambda' (İSİMSİZ TEK SATIRLIK FONKSİYONLAR)
# ==============================================================================
#
# 1. Nedir?
# ------------------------------------------------------------------------------
# * 'def' yazmadan tek satırda "kullan-at" fonksiyon oluşturmayı sağlar.
# * Otomatik değer döndürür ('return' kelimesi yazılmaz).
# * Sözdizimi: lambda parametreler : ifade
#
# 2. Doğrudan Kullanım
# ------------------------------------------------------------------------------
# kare_al = lambda x: x * x
# print(kare_al(5))  # Çıktı: 25
#
# topla = lambda a, b: a + b
# print(topla(3, 7))  # Çıktı: 10
#
# 3. Ortak Kullanım Alanları (map, filter, sorted)
# ------------------------------------------------------------------------------
# * map() ile    : list(map(lambda x: x * 2, [1, 2, 3]))      -> [2, 4, 6]
# * filter() ile : list(filter(lambda x: x % 2 == 0, [1, 2])) -> [2]
# * sorted() ile : sorted(liste, key=lambda x: x["isim"])     -> Isme gore siralar
#
# 4. Kural
# ------------------------------------------------------------------------------
# * Sadece tek satırlık işlemler içindir; döngü veya çok satırlı bloklar yazılmaz.
#
# ==============================================================================

students = ["Hermione" , "Harry" , "Ron"]
gryffindors = {student: "Gryffindor" for student in students}
print(gryffindors)

# ==============================================================================
# 📌 PYTHON DICT COMPREHENSION (SÖZLÜK KAVRAYIMI)
# ==============================================================================
#
# 1. Nedir?
# ------------------------------------------------------------------------------
# * 'for' döngüsü yazmadan, tek satırda hızlıca Sözlük (Dictionary) oluşturmayı sağlar.
# * Sözdizimi: { anahtar: deger  for eleman in kaynak  if kosul }
#
# 2. Temel Örnekler
# ------------------------------------------------------------------------------
# A) Sayıların karelerinden sözlük oluşturma:
# kareler = {x: x * x for x in range(1, 4)}
# print(kareler)  # Çıktı: {1: 1, 2: 4, 3: 9}
#
# B) İki listeyi birleştirip sözlük yapma (zip ile):
# ogrenciler = ["Semih", "Ahmet"]
# notlar = [90, 80]
# sonuc = {ogrenciler[i]: notlar[i] for i in range(len(ogrenciler))}
# print(sonuc)  # Çıktı: {'Semih': 90, 'Ahmet': 80}
#
# C) Koşul (if) ekleyerek filtreleme:
# puanlar = {"Semih": 90, "Ahmet": 45, "Can": 75}
# gecenler = {k: v for k, v in puanlar.items() if v >= 50}
# print(gecenler)  # Çıktı: {'Semih': 90, 'Can': 75}
#
# 3. List Comprehension'dan Farkı
# ------------------------------------------------------------------------------
# * Listede köşeli parantez '[ ]' kullanılırken, Sözlükte süslü parantez '{ }' 
#   kullanılır ve araya iki nokta üst üste 'key: value' konur.
#
# ==============================================================================

students = ["Hermione" , "Harry" , "Ron"]
for i, student in enumerate(students):
    print(i+1 , student)

# ==============================================================================
# 📌 PYTHON 'enumerate()' FONKSİYONU
# ==============================================================================
#
# 1. Nedir?
# ------------------------------------------------------------------------------
# * Bir listede döngü (for) ile gezerken elemanların 'indeks sırasını' da otomatik verir.
# * Manuel sayaç (i = 0, i += 1) yazma kalabalığını ortadan kaldırır.
# * Döngünün her adımında geriye (indeks, eleman) şeklinde ikili (tuple) döndürür.
#
# 2. Örnek Kullanım
# ------------------------------------------------------------------------------
# meyveler = ["Elma", "Muz", "Çilek"]
#
# for sira, meyve in enumerate(meyveler):
#     print(f"{sira}. indeks: {meyve}")
#
# Çıktı:
# 0. indeks: Elma
# 1. indeks: Muz
# 2. indeks: Çilek
#
# 3. İndeksi İstediğin Sayıdan Başlatma (start=1)
# ------------------------------------------------------------------------------
# for sira, meyve in enumerate(meyveler, start=1):
#     print(f"{sira}. Meyve: {meyve}")
#
# Çıktı:
# 1. Meyve: Elma
# 2. Meyve: Muz
# 3. Meyve: Çilek
#
# ==============================================================================
# ==============================================================================
# 📌 FARKLARI: range() VS enumerate()
# ==============================================================================
#
# * range(len(liste)) : Sadece sayı üretir (0, 1, 2...). 
#                       Elemana erişmek için 'liste[i]' yazmak şarttır.
#
# * enumerate(liste)   : Hem sırayı (i) hem de ELEMANIN KENDİSİNİ verir.
#                       'liste[i]' yazma kalabalığını bitirir.
#
# ==============================================================================

def main():
    n = int(input("What's n? "))
    for s in range(n):
        print("s")
def sheep(n):
    for i in range(n):
        yield "🐑" * i
if __name__ == "__main__":
    main()

# ==============================================================================
# 📌 PYTHON 'yield' VE GENERATORS (ÜRETEÇLER)
# ==============================================================================
#
# 1. Nedir ve Ne İşe Yarar?
# ------------------------------------------------------------------------------
# * Milyonlarca veriyi aynı anda RAM'e yükleyip bilgisayarı kilitlemek yerine,
#   ihtiyaç duyuldukça ADIM ADIM (tek tek) veri üretmeyi sağlar.
# * Bellek (RAM) tasarrufu için hayati önem taşır.
#
# 2. 'return' ve 'yield' Farkı
# ------------------------------------------------------------------------------
# * return : Fonksiyonu tamamen kapatır ve sonucu tek hamlede döndürür.
# * yield  : Değeri üretir, fonksiyonu duraklatır (pause) ve kaldığı yeri hatırlar.
#
# 3. Örnek Kullanım
# ------------------------------------------------------------------------------
# def kare_uretec(sinir):
#     for i in range(sinir):
#         yield i * i  # Hepsini listede toplamaz, çağırdıkça 1 tane verir.
#
# # Kullanım A: for döngüsü ile (Otomatik tüketim)
# for kare in kare_uretec(5):
#     print(kare)  # 0, 1, 4, 9, 16 (Tek tek basar)
#
# # Kullanım B: next() fonksiyonu ile (Manuel adım adım)
# g = kare_uretec(3)
# print(next(g))  # 0 üretir ve durur
# print(next(g))  # 1 üretir ve durur
#
# 4. Generator Expression (Tek Satırda Yazımı)
# ------------------------------------------------------------------------------
# * List comprehension gibi yazılır ama '[]' yerine '()' parantez kullanılır:
#
# liste_hali   = [x * 2 for x in range(1000000)]  # Tüm liste RAM'de (Yüksek Bellek)
# generator_hali = (x * 2 for x in range(1000000)) # Üreteç objesi (Sıfır Bellek yükü)
#
# ==============================================================================

