from unittest import case


x = int(input("what is x ? "))
y = int(input("what is y ? "))
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

# buradaki mantik basit sistemde hemen anlasilmayabilir . fakat mantik su . ilk durumda , bir sonuc icin 3 soru sorduk . fakat burada artik sistem su sekilde calisiyor . artik bir sorunun cevabina ulastiginda artik sana daha fazla soru sormuyor . dolayisi ile buyuk kodlarda zaman kazaniyorsun .
# x = int(input("what is x ? "))
# y = int(input("what is y ? "))
# if x < y:
    # print("x is less than y")
# elif x > y:
    # print("x is greater than y")
# elif x == y:
    # print("x is equal to y")

# buradaki mantikda su . eger x ve y birbirinden buyuk yada kucuk degilse o zaman esittir . dolayisi ile if ile tekrardan soru sormaktansa artik else ile sunu diyoruz . kardes eger bu ikisi olmuyora else ile sen bunu cevap olarak olustur .
# x = int(input("what is x ? "))
# y = int(input("what is y ? "))
# if x < y:
    # print("x is less than y")
# elif x > y:
    # print("x is greater than y")
# else:
    # print("x is equal to y")

a = int(input("what is a ? "))
b = int(input("what is b ? "))
if a < b or a > b:
    print("a is not equal to b")
else:
    print("a is equal to b")

n = int(input("what is n ? "))
m = int(input("what is m ? "))
if n != m:
    print("n is not equal to m")
else:
    print("n is equal to m")

# burada da aslinda ustteki kodun tam tersi durumunu deneyimledik . 
# n = int(input("what is n ? "))
# m = int(input("what is m ? "))
# if n == m:
    # print("n is  equal to m")
# else:
    # print("n is not equal to m")

score = int(input("what is your score ? "))
if score >= 90 and score <= 100:
    print("your grade is A")
elif score >= 80 and score < 90:
    print("your grade is B")
elif score >= 70 and score < 80:
    print("your grade is C")
elif score >= 60 and score < 70:
    print("your grade is D")
else:
    print("your grade is F")

# buda bir baska mantik :
# if 90 <= score <= 100:
    # print("your grade is A")
# elif 80 <= score < 90:
    # print("your grade is B")
# elif 70 <= score < 80:
    # print("your grade is C")
# elif 60 <= score < 70:
    # print("your grade is D")
# else:
    # print("your grade is F")

# if score >= 90: 
    # print("your grade is A")
# elif score >= 80:
    # print("your grade is B")
# elif score >= 70:
    # print("your grade is C")
# elif score >= 60:
    # print("your grade is D")
# else:
    # print("your grade is F")

p = int(input("what is p ? "))
if p % 2 == 0:
    print("p is even")
else:
    print("p is odd")

# bool 
# False , True 
# kullanim :  return False , return True

def main():
    k = int(input("what is k ? "))
    if is_even(k):
        print("k is even")
    else:
        print("k is odd")

def is_even(L):
    if L % 2 == 0:
        return True
    else:
        return False

main()

# buda alttaki kodun daha kisa hali .
# def is_even(L):
    # if L % 2 == 0:
        # return True if n % 2 == 0 else False

# daha da sadeleştirirsek :
# def is_even(L):
    # n % 2 == 0

name = input("what is your name ? ")
match name:
    case "Alice":
        print("A takimi")
    case "Bob":
        print("B takimi")
    case _:
        print("Baska bir takim")

    
# name = input("what is your name ? ")
# match name:
    # case "andrew" | "bob" | "charlie":
        # print("A takimi")
    # case "david" | "edward" | "frank":
        # print("B takimi")
    # case _:
        # print("Baska bir takim")

