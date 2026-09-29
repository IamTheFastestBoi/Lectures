# Phyton

# print("Selam")
# input("What is your name")
# name = input("What is your name")
# print(name)
# # Ask user for their name (benim terminali etkilemeyecek notum)
# print("hello," + name)
# print("hello,", name)

# 1) print("Merhaba", end="") => Çıktı: MerhabaDünya
# 2) print("Dünya")

# 1) print("Merhaba", end=" ") => Çıktı: Merhaba Dünya
# 2) print("Dünya")

# print("Merhaba\nDünya") => Çıktı: 1) Merhaba
#                                    2) Dünya
# print("Merhaba", "mehmet") => Çıktı: 1) Merhaba mehmet

# print("Merhaba", "mehmet", sep=", ") => Çıktı: 1) merhaba, mehmet
# print("Merhaba\nDünya") => Çıktı: 1) Merhaba
#                                    2) Dünya

# print("Mehmet bana \"mal\" dedi.") => Çıktı: 1) Mehmet bana "mal" dedi.

# print("hello, {name}") => Çıktı: 1) hello, {name}  yanlış oldu doğrusu;
# print(f"hello, {name}") => Çıktı: 1) hello, mehmet
# ! [name = mehmet] !

# name = name.strip()
# name = name.capitalize()
# name = name.title()

# name = input("Senin adın ne?").strip().title()

print("Windows ve VS Code hazır!")
name=input("senin adin ne?").strip().title()
name= name.strip()
name=name.capitalize()
name=name.strip().title()
print("naber lo , "+name)
print("kardes sen malmisin " , "essek seni" , sep=",")
print("Elma", "Armut", "Çilek")
print("ne sacmaliyon")
print("ben bir essegim" , end="-")
print("hepimiz essegiz")

first, last = name.split(" ")
print(f"hello, {first}")
# buda bir secenek dir : first, second, third = name.split(" ")
# print(f"hello, {second}")

x = 3
y = 7
z = int (x) + int(y)

print(z)

a= input(" what is a ? ")
b= input("what is b ? ")
c= int(a) + int(b)
print(c)
# baska bir yontem de bu : 
# x = int(input("what is x ? ")
# y = int(input("what is y ? ")
# print(x + y)
# bir diger yontem de bu ;
# x = int(input("what is x ? ") + # y = int(input("what is y ? ")   

d = float(input(" what is d ? "))
k = float(input(" what is k ? "))

print(d + k)

g=float(input(" what is g ? "))
t=float(input(" what is t ? "))

h = round(g+t)

print(h)

# cesitli baska kullanimlar da vardir .
# z = 1000000
# Normal yazdırma:
# print(f"{z}")
# Çıktı: 1000000
# Binlik basamak ayırıcılı yazdırma:
# print(f"{z:,}")
# Çıktı: 1,000,000    

# z = 1250000.758
# Hem binlik ayırıcı (,) hem de virgülden sonra 2 basamak (.2f):
# print(f"{z:,.2f}")
# Çıktı: 1,250,000.76

p = x / y 
p = round(x/y, 3)
print(p)

print(f"{p: .2f}")

def merhaba():
    print("merhaba")
merhaba()

def esenlikler(size):
    print("esenlikler," + " dilerim ", size)
yourname = input("what is your name ? ")
esenlikler(yourname)

# baska bir kullanim :
# def hello(to="world"):
#     print("hello, " + to)
# cikti : hello, world


# main() fonksiyonunun kullanimi : 
#print(karesini_al(5))  # Python buraya geldiğinde "karesini_al ne demek bilmiyorum!" der ve çöker.
#def karesini_al(x):
#    return x * x
# YANLIŞ KULLANIM (ÇÖKER)

# DOĞRU KULLANIM (ÇALIŞIR)

# def main():
# Python bu satıra geldiğinde karesini_al fonksiyonunu henüz çalıştırmıyor,
# sadece "main çağrıldığında karesini_al'ı çalıştıracağım" diye not alıyor.
#    print(karesini_al(5)) 

# def karesini_al(x):
#    return x * x

# EN ALTTTAKİ DÜĞME:
# main()  # İşte şimdi çalıştır! Bu satıra gelindiğinde Python karesini_al'ı zaten öğrenmiştir.

def main():
    m = int(input("bir sayi giriniz : "))
    print("m squared is" , square(m))

def square(n):
    return n * n

main()

#def karesi(n):
#    return n * n  # Hesapla ve sonucu çağıran yere teslim et!
# sonuc = karesi(5)  # karesi(5) çalışır, dışarı 25 fırlatır, sonuc = 25 olur.
# print(sonuc)

# def test():
#    x = 10  # x sadece test() fonksiyonunun içinde yaşar!
# test()
# print(x)  # HATA! Python "x ne bilmiyorum" der. (Scope dışı)

# pi = 3.14159265
#print(f"{pi:.3f}")
# Çıktı: 3.142 (Virgülden sonra 3 basamak bıraktı ve yuvarladı)

#para = 5.5
#print(f"{para:.2f}")
# Çıktı: 5.50 (Eksik basamağı sıfırla tamamladı)