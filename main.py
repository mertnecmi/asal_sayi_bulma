# Kullanıcıdan bir sayı alan ve 
# bu sayının asal olup olmadığını kontrol eden bir Python kodu yazın.

sayi = int(input("Bir Sayı Giriniz : "))

if sayi > 1:
    for i in range(2, sayi + 1): 
        if sayi % i == 0:  # Eğer sayi, i'ye tam bölünüyorsa
            print(f"{sayi} asal bir sayı değildir.")
            break
    else:
        print(f"{sayi} asal bir sayıdır.")
else:
    print(f"{sayi} asal bir sayı değildir."
