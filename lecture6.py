names = []

for _ in range(3):
    name = input("What is your name?")
    names.append(name)

# yada su sekildede yazilabilir ;
# for _ in range(3):
    # names.append(input("What is your name?"))

# .append(): Dosyaya dokunmaz; sadece RAM'deki listenin sonuna yeni bir eleman ekler.
# Burada kullanıcıdan alınan name değişkenini, 1. satırda oluşturduğumuz names listesinin içine fırlatır.

for name1 in sorted(names):
    print(f"hello, {name1}")

##########################################################################

file = open("names.txt", "w")
file.write(name)
file.close()

# burada sen names.txt ye isim yaziyorsun fakat w(write) fonksiyonu dolayisi ile her yeni data girisinde , bir eski data yi siliyor. ve 2 data yi da \n nin olmamasindan dolayi art arda birlesik yaziyor.
# kardes aklin karismasin , burada for loop unda bile yeni data girisinde siliyor . o yuzden names.txt de tam adini yazdiginda sira ile ; sadece akbas yazisini goruyorsun.

name2 = input("what is your name?")

file1 = open("names1.txt", "a")
file1.write(f"{name2}\n")
file1.close()

# burada "a" fonksiyonu ile artik yeni data girisinde eski data yi silmiyor . ve gorunen \n fonksiyonu ise , data nin art arda eklenmesinin onune gecip , yeni data nin alt satira yazilmasini sagliyor. eger \n olmasa idi .txt dosyamizda data yi mehmetahmethuseyin olarak gorurduk . fakat \n ile bud data lar alt alta yazilarak daha okunabilir hale getiriliyor.

with open("names1.txt", "a") as file1:
    file1.write(f"{name2}\n")

with open("names1.txt", "r") as file1:
    lines = file1.readlines()

for line in lines:
    print("hello,", line.rstrip())

# with open() KULLANIMI ÖZETİ
# NE İŞE YARAR?
# Dosyayı güvenli bir şekilde açar ve işlem bittiğinde otomatik KAPATIR.
# file.close() yazma zorunluluğunu ortadan kaldırır, veri kaybını önler.

# readlines() Ne İşe Yarar?
# Dosyadaki bütün satırları tek bir hamlede okur ve her satırı ayrı bir metin (string) elemanı yaparak sana bir liste (list) halinde teslim eder.

# read(): Dosyanın tamamını tek bir uzun metin (string) olarak okur.

# readline(): Dosyadan sadece 1 satır okur. Her çağırışında bir sonraki satıra geçer.

# readlines(): Dosyadaki bütün satırları okuyup bir liste (list) olarak döndürür.

names1 = []

with open("names1.txt") as file3:
    for line in file3:
        names1.append(line.rstrip())

for name4 in sorted(names1):
    print(f"hello, {name4}")

# names = ["mehmet", "akbas", "semih"]
# Normal sıralama (A'dan Z'ye): ['akbas', 'mehmet', 'semih']
# reverse=True ile tersten sıralama (Z'den A'ya):
# for name in sorted(names, reverse=True):
    # print(name)

##########################################

with open("mehmethayat.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

# bir baska yontemde;

# with open("students.csv") as file
     # for line in file:
          # isim, okul = line.rstrip().split(",")
          # print(f"{isim} is in {okul}")
          
# ==============================================================================
# .split() FONKSİYONU ÖZETİ
# ==============================================================================

# NE İŞE YARAR?
# Tek parça halinde duran uzun bir metni (string) belirlediğin bir ayraçtan
# (virgül, boşluk, tire vb.) keser ve sana elemanlarına ayrılmış bir LİSTE teslim eder.

# 1. TEMEL KULLANIM (Metni Virgülden Bölme)
# text = "mehmet, semih, akbas"
# names = text.split(", ")  # Virgülden ve boşluktan keser
# print(names)              # Çıktı: ['mehmet', 'semih', 'akbas']

# 2. AYRAÇ BELİRTMEZSEN (Boşluklardan Bölme)
# sentence = "Python ogrenmek cok zevkli"
# words = sentence.split()  # Varsayılan olarak boşluklardan böler
# print(words)              # Çıktı: ['Python', 'ogrenmek', 'cok', 'zevkli']

# 3. DOSYA OKURKEN KULLANIMI (CSV / List Unpacking)
# "mehmet,yildiz\n" verisini virgülden bölüp doğrudan değişkenlere dağıtır:
# name, school = "mehmet,yildiz".split(",")
# print(name)               # Output: mehmet
# print(school)             # Output: yildiz

# ALTIN KURAL: 
# .split() SADECE metinlerde (string) çalışır. Zaten liste olan yapıya atılmaz!
# ==============================================================================

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

def get_name(student):
    return student["name"]



for student in sorted(students, key=get_name):
     print(f"{student['name']} is in {student['house']}")


# Yada def ile bir fonksiyon tanimla zahmetine girmeden lambda fonksiyonunu kullanabiliriz;

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")

# LAMBDA (TEK SATIRLIK FONKSİYON) ÖZETİ
# ==============================================================================
#
# NE İŞE YARAR?
# 'def' ile uzun uzun fonksiyon tanımlamak yerine, sadece tek bir yerde 
# kullanılacak geçici ve isim verilmemiş fonksiyonlar oluşturur.
#
# DÖNÜŞÜM:
# def get_name(student):           ===>   lambda student: student["name"]
#     return student["name"]


import csv

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})


# burada isin key get name ile ozel olarak sorted olmamis halini yazdik;

# for student in students:
    # print(f"{student['name']} is in {student['house']}")

# ==============================================================================
# csv.reader KULLANIMI VE MANTIĞI
# ==============================================================================
#
# NE İŞE YARAR?
# Düz .split(",") yönteminin aksine, CSV dosyasındaki çift tırnaklı koruma
# kalkanlarını ("b, c") tanır. Tırnak içindeki virgülleri bölmez, veriyi korur.
#
# ÇALIŞMA MANTIĞI:
# reader = csv.reader(file)
# Her satırı okunmuş ve doğru sütunlara bölünmüş bir LİSTE olarak verir:
# Örn: 'a, "b, c"' satırını ['a', 'b, c'] şeklinde 2 elemanlı liste yapar.
#
# KULLANIM ÖRNEĞİ:
# import csv
#
# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:  # 2 elemanlı listeyi değişkenlere dağıtır
#         print(f"{name} is in {home}")
# ==============================================================================

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

# ==============================================================================
# csv.DictReader KULLANIMI VE MANTIĞI
# ==============================================================================
#
# NE İŞE YARAR?
# CSV dosyasının İLK SATIRINDAKİ sütun isimlerini (header) otomatik okur ve 
# her satırı etiketli bir Sözlük (dict) olarak bize teslim eder.
#
# İNDEKS (row[0]) İLE DictReader (row["name"]) FARKI:
# csv.reader kullanırken sütun sırasına (row[0], row[1]) bağımlı kalırız.
# DictReader ile doğrudan sütun adı ("name", "home") kullanırız; dosyada 
# sütunların sırası değişse bile kodumuz bozulmaz.
#
# KULLANIM ÖRNEĞİ:
# import csv
#
# with open("students.csv") as file:
#     reader = csv.DictReader(file)  # İlk satırı anahtar (key) yapar
#     for row in reader:
#         # row artık bir dict'tir: {"name": "Itachi", "home": "Konoha"}
#         print(f"{row['name']} is from {row['home']}")
# ==============================================================================
# ==============================================================================
# SÖZLÜK (DICTIONARY - dict) ÖZETİ
# ==============================================================================
#
# NE İŞE YARAR?
# Verileri indeks numarasıyla ([0], [1]) değil, etiket ismiyle ("name", "age")
# saklamamızı sağlar. { "anahtar": "değer" } yapısıyla çalışır.
#
# TEMEL KULLANIM:
# student = {"name": "Mehmet", "house": "Yildiz"}
# print(student["name"])   # Çıktı: Mehmet
# print(student["house"])  # Çıktı: Yildiz
# ==============================================================================
# ==============================================================================
# F-STRING VE SÖZLÜK (dict) TIRNAK ÇAKIŞMASI KURALI
# ==============================================================================
#
# NEDEN TEK TIRNAK (') KULLANILIR?
# Python ilk gördüğü tırnak türüyle metni başlatır ve aynı türden ikinci tırnağı
# gördüğü anda metni BİTİRİR. İçeride de aynı tırnağı açarsan metin erken kapanır.
#
# DOĞRU (Çakışma yok):
# print(f"{student['name']}")  # Dışarıda çift ", içeride tek '
#
# YANLIŞ (Metin 'name' öncesinde erken kapanır ve hata verir):
# print(f"{student["name"]}")  # SyntaxError!
# ==============================================================================

import csv

name = input("what is your name?")
home = input("where is your home")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name,home])

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})

# ==============================================================================
# 1. csv.writer (LİSTE İLE YAZMA)
# ==============================================================================
# - Verileri bir LİSTE [...] olarak alır ve sırayla sütunlara yazar.
# - Sütun sırası tamamen senin listenin içine yazdığın eleman sırasına bağlıdır.
# - writer.writerow([name, home])
# ==============================================================================

# ==============================================================================
# 2. csv.DictWriter (SÖZLÜK İLE YAZMA)
# ==============================================================================
# - Verileri SÖZLÜK {...} olarak alır ve etiketlerine (key) göre ilgili sütuna yazar.
# - 'fieldnames' parametresi ile başlık sırasını en başta tanımlamak ZORUNLUDUR.
# - writer.writerow({"name": name, "home": home}) . Fieldnames bir nevi patronlugunu 
# ilan eder ve sen writerow() icine ters sirayla bile yazsan , sistem fieldnames deki 
# siraya gore hareket eder.
# ==============================================================================





