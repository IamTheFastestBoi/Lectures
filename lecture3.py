try:
    x = int(input("Enter a number: "))
    print(f"You entered: {x}")
except ValueError:
    print("That's not a valid number. Please enter an integer.")

try:
    y = int(input("enter your fav number:"))
except ValueError:
    print("That's not a valid number. Please enter an integer.")
else:
    print(f"you entered: {y}")


while True:
    try:
        z = int(input("Enter a number: "))
    except ValueError:
        print("That's not a valid number. Please enter an integer.")
    else:
        break

print(f"You entered: {z}")

def main():
    a = get_int()
    print(f"You entered: {a}")

def get_int():
    while True:
        try:
            a = int(input("Enter a number: "))
        except ValueError:
            print("That's not a valid number. Please enter an integer.")
        else:
            break
    return a

# yada bir baska sekilde de yazabiliriz ;

def main():
    b = get_integer()
    print(f"You entered: {b}")

def get_integer():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            pass  # Hata durumunda hiçbir şey yapmadan döngüye devam et



main()






#  SyntaxError (Sözdizimi Hatası)
# Python'ın yazım kuralları ihlal edildiğinde oluşur. Kod çalışmadan önce
# okuma (parse) aşamasında fark edilir (try-except ile yakalanamaz).
# Örnek: if x == 5 (sonunda : unutulduğunda)

#  ValueError (Değer Hatası)
# Bir fonksiyona doğru veri tipinde (örn. string) ama içeriği/değeri 
# o işlem için geçersiz bir veri gönderildiğinde oluşur.
# Örnek: int("cat") veya float("on_bes")

#  NameError (İsim Hatası)
# Python'ın hafızasında olmayan, tanımlanmamış bir değişken veya fonksiyon
# çağrıldığında oluşur.
# Örnek: try bloğunda x = int(input()) satırı patlarsa, x hiç oluşmaz. 
# Alt satırda print(x) dersen NameError alırsın.
# print(tanimlanmamis_degisken)


