import random 

coin = random.choice(['Heads', 'Tails'])

print(coin)

from random import choice

coin1 = choice(['Heads', 'Tails'])

print(coin1)

# --- YÖNTEM 1: Bütün Çantayı Getirmek (import random) ---
# import random

# Çantayı komple getirdiğin için aletin adının başına "random." yazmak zorundasın.
# para1 = random.choice(["yazı", "tura"])
# print(para1)


# --- YÖNTEM 2: Çantadan Sadece İstediğin Aleti Almak (from random import choice) ---
# from random import choice

# Aleti doğrudan masaya koyduğun için başına "random." yazmadan direkt kullanırsın.
# para2 = choice(["yazı", "tura"])
# print(para2)

import random

number = random.randint(1, 10)

print(number)

import random

cards = ["jack", "queen", "king"]

random.shuffle(cards)

for card in cards:
    print(card)

import statistics

print(statistics.mean([100, 90]))

import sys

print("hello, my name is", sys.argv[1])

# eger kisi bir prompt girmezse IndexError vericek

import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for argument in sys.argv:
    print("hello, my name is", argument)

# burada bir sikinti var , oda su . lecture4.py ,  sys.argv[0] in kendisi oldugu icin , terminalde girdigin promptlar ile birlikte ayni zamanda hello, my name is lecture4.py adinda sacma bir sey daha yazicak.
# bunu duzeltmek icin;

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for argument1 in sys.argv[1:]:
    print("hello, my name is", argument1)

# [1:] ile yaptigimiz sey ; sisteme 0 dan degil 1 den basla ve son neresi ise oraya kadar devam et diyoruz.

############################################################################

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])

#############################################################################

import requests
import sys


if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(response.json())

import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(json.dumps(response.json() , indent=2))

import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

a = response.json()
for result in a["results"]:
    print(result["trackName"])

# burada itunes dan aldigimiz bilgiyi , incelenebilir ve kullanici tarafindan okunabilir bir liste haline getirdik.


import sys

from sayings import hello 

if len(sys.argv) == 2:
    hello(sys.argv[1])

# burada kendi yazdigimiz sayings.py dan hello fonksiyonunu import ettik .

# sayings.py dosyamiz;

# def main()
    # hello("world")
    # goodbye("world")

# def hello(name):
    # print(f"hello, {name}")

# def goodbye(name):
    # print(f"goodbye, {name}")

# if __name__ == "__main__":
    # main()

# if __name__ == "__main__": satırı; "Bu dosya doğrudan çalıştırılırsa bu kodları çalıştır, ama başka bir dosyaya import edilirse bu kodları çalıştırma, gizle" demektir.

# --- __name__ VE __main__ MANTIĞI (EMNİYET KİLİDİ) ---

# 1. DOSYA BİZZAT ÇALIŞTIRILIRSA (python dosya.py):
# Python arka planda __name__ değişkenine OTOMATİK OLARAK "__main__" değerini atar.
# Şart sağlandığı için ( "__main__ == "__main__" ) kilit kalkar ve kod çalışır.

# 2. DOSYA BAŞKA YERDE İTHAL EDİLİRSE (import dosya):
# Python arka planda __name__ değişkenine DOSYANIN KENDİ ADINI atar (örneğin "araba").
# Şart bozulduğu için ( "araba" == "__main__" -> Yanlış) kilit KALKMADAN kalır.
# İçerideki kodlar otomatik çalışıp ortalığı karıştırmaz.

# if __name__ == "__main__":
    # Buraya sadece dosya direkt çalıştırıldığında tetiklenmesini istediğin 
    # fonksiyonu/kodları yazarsın:
    # main()
    





      



    







