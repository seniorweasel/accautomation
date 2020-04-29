# -*- coding: cp1254 -*-
import json
import time
import uinames
import string
import random
i=0
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def tarik():
    if __name__ == "__main__":
        people = uinames.generate_random_identities(500, "female", "turkey", ext=True)
        for p in people.data:
            print("db.insert(#'ad':'{}', 'soyad':'{}', 'ulke':'{}' , 'sifre':'123abc234' *)").format(p.name, p.surname,p.region,)
            
tarik()
tarik()
tarik()
tarik()
tarik()

time.sleep(60.0)
tarik()
tarik()
tarik()
tarik()
tarik()

time.sleep(60.0)
tarik()
tarik()
tarik()
tarik()
tarik()

print("Kod 429 Sınırı Aşılıyor...--10 saniye delay")
time.sleep(60.0)
tarik()
tarik()
tarik()
tarik()
tarik()

print("Kod 429 Sınırı Aşılıyor...--10 saniye delay")
time.sleep(60.0)
tarik()
tarik()
tarik()
tarik()
tarik()

print("Kod 429 Sınırı Aşılıyor...--10 saniye delay")
time.sleep(60.0)
tarik()
tarik()
tarik()
tarik()
tarik()

print("Kod 429 Sınırı Aşılıyor...--10 saniye delay")
time.sleep(60.0)
tarik()
tarik()
tarik()
tarik()
tarik()

print("12000 kullanıcı basıldı! --60 saniye içinde bu pencere kendini kapatacak.")
time.sleep(60000)



