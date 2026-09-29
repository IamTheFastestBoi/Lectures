i = 3
while i != 0:
    print("meow")
    i = i - 1

# Özetle while Arka Planda Ne Yapar?
# while aslında tek bir şey yapar:
# Koşul True (Doğru) olduğu sürece, altındaki kod bloğunu çalıştırıp sürekli en başa (şartı kontrol etme noktasına) geri fırlatan bir görünmez yaydır.
# Kutudaki sayı eksilip şart False (Yanlış) olduğu an, o yay kırılır ve program aşağı doğru akmaya devam eder.

a = 0
while a <= 3:
    print("meow2")
    a = a + 1

# bir kisa yol : i += 1 de yazabilirsin , bu da ayni mantik oluyor

for b in [0,1,2]:
    print("meow3")

# for döngüsünün mantığı şudur:
# "Listede kaç tane eleman varsa, sırayla hepsini eline al ve bloktaki kodu o kadar kez çalıştır."

for c in range(3):
    print("meow4")

# range() fonksiyonu aslında senin yerine otomatik bir liste üreten bir fabrikadır.
# range(3) yazdığında Python arka planda senin yerine [0, 1, 2] listesini oluşturur. for döngüsü de bu 3 elemanı gezip kodu 3 kere çalıştırır.
# range(10000) yazdığında ise Python arka planda [0, 1, 2, ..., 9999] şeklinde tam 10.000 elemanlı bir liste hazırlar. Döngü de hiç üşenmeden o kodu 10.000 kere çalıştırır.
# Küçük Bir Detay (Sıfırdan Başlar)
# range(3) dediğinde sayılar 1, 2, 3 diye gitmez, 0'dan başlar: 0, 1, 2.
# Ama kaç adet sayı var diye sayarsan tam 3 tane sayı vardır. O yüzden döngünün dönme sayısı verdiğin sayıyla her zaman birebir aynıdır!

for _ in range(3):
    print("meow5")

# burda _ kullanmamizin sebebi aslinda o degiskeni kullanmayacagimiz icin , yani sadece 3 kere donmesini istiyoruz , ama degiskeni kullanmayacagimiz icin _ kullaniyoruz .

print("meow6 "*3)

# yada ;

print("meow7\n"*3, end="")

while True:
    T = int(input("What is T ?"))
    if T < 0:
        continue
    else:
        break

# DÖNGÜLERDE BREAK VE RETURN FARKI

# 1. break
# - SADECE icinde bulundugu donguyu sonlandirir (kirar).
# - Fonksiyondan cikmaz; dongunun altindaki kodlar calismaya devam eder.
# - Dışarıya herhangi bir veri/değer TESLİM ETMEZ.

# 2. return
# - Donguyu ANINDA kirar VE fonksiyonu o saniyede tamamen bitirir.
# - Altindaki hicbir kod satiri calismaz.
# - Elde edilen degeri fonksiyonun cagrildigi yere GERİ VERİR (teslim eder).

# ==============================================================================
# ÖZET
# break  --> "Donguyu durdur, fonksiyon icinde yoluna devam et."
# return --> "Donguyu durdur, fonksiyonu kapat ve degeri teslim et."
# ==============================================================================



for _ in range(T):
    print("meow81")


# isi daha da kisaltarak :

while True:
    R = int(input("What is R ?"))
    if R > 0:
        break

for _ in range(R):
    print("meow8")


def main():
    meow(3)

def meow(k):
    for _ in range(k):
        print("meow9")

main()

# isi biraz daha spesifiklestirelim ;

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        L = int(input("What is L ?"))
        if L > 0:
            return L

def meow(L):
    for _ in range(L):
        print("meow10")

main()

# break: Sadece içinde bulunduğu döngüyü kırar.
# continue: Döngünün o turunu pas geçer, başa döner.
# return: Döngüye bakmaksızın tüm fonksiyonu bitirip dışarıya değer döndürür.

students = ["Alice", "Bob", "Charlie"]

print(students[0])  # Alice
print(students[1])  # Bob
print(students[2])  # Charlie

for student in students:
    print(student)

# Python bunu okurken der ki:
# "Tamam, elimde students adında bir liste var. Bu listenin içindeki elemanları sırayla elime alacağım. Her elime aldığım elemanı geçici olarak student adını verdiğim kutunun içine koyacağım ve alt satıra geçeceğim."

for P in range(len(students)):
    print(students[P])

# ise biraz daha renk katmak istersen ;
# for P in range(len(students)):
    # print(P + 1, students[P])

hogwarts = { "hermoine": "Gryffindor", "harry": "Gryffindor", "ron": "Gryffindor" , "draco": "Slytherin", }
print(hogwarts["hermoine"])
print(hogwarts["harry"])
print(hogwarts["ron"])
print(hogwarts["draco"])

# enayi gibi tek tek print yazmak yerine ;
for student in hogwarts:
    print(student, hogwarts[student] , sep=", ")


ogrenciler = [
    {"isim":"hermoine", "house":"Gryffindor","patronus":"otter"},
    {"isim":"harry", "house":"Gryffindor","patronus":"stag"},
    {"isim":"ron", "house":"Gryffindor","patronus":"jack russell terrier"},
    {"isim":"draco", "house":"Slytherin","patronus":None}
]

for student in ogrenciler:
    print(student["isim"], student["house"], student["patronus"], sep=", ")


def main():
    print_square(3)

def print_square(size):
    for W in range(size):
        for H in range(size):
            print("#", end="")
        print()

# kardes bu loop un daha kolayi var , onu da yazalim ;
# def print_square(size):
#     for W in range(size):
#         print("#" * size)

main()



