Gezgin Satıcı Problemi
Giriş
Gezgin satıcı problemi, bir satıcının belirli bir bölgedeki şehirleri ziyaret etmesi ve bu şehirler arasındaki en kısa yolu bulmasıdır. Bu problem, bilgisayar bilimi, mühendislik ve ekonomi gibi birçok alanda yaygın olarak kullanılmaktadır.

Karınca Kolonisi Algoritması:
Karınca kolonisi algoritması, gezgin satıcı problemini çözmek için kullanılan bir metasezgisel algoritmadır. Bu algoritma, karıncaların feromon bırakarak yollarını bulmalarına benzer bir şekilde çalışır.

Bu Kod Ne Yapar?
Bu kod, karınca kolonisi algoritmasını kullanarak gezgin satıcı problemini çözer. Kod, aşağıdaki adımları gerçekleştirir:
1.	Şehirler arasındaki uzaklıkları hesaplar.
2.	Başlangıçta tüm şehirler için eşit olan bir feromon matrisi oluşturur.
3.	Belirli bir sayıda iterasyon için aşağıdaki adımları gerçekleştirir:
1.	Her karınca, şehirleri rastgele bir sırayla ziyaret eder.
2.	Her karıncanın ziyaret ettiği her yol için, feromon miktarını artırır.
3.	Sonraki iterasyon için, daha önce daha fazla ziyaret edilen yollar daha olasıdır.
4.	İteratörler bittikten sonra, en kısa yolu bulmak için feromon matrisini kullanır.

```
Kodun Kullanımı
import numpy as np
import random
import matplotlib.pyplot as plt

from karınca_kolonisi_algoritmasi import KARINCA_KOLONI_ALGORITMASI

# Şehirler arasındaki uzaklıkları hesaplayın
uzaklik_matris = np.array([[0, 32, 41, 27, 13, 54],
                           [30, 0, 34, 39, 58, 40],
                           [32, 59, 0, 14, 24, 46],
                           [12, 15, 26, 0, 24, 53],
                           [46, 39, 22, 35, 0, 33],
                           [53, 37, 30, 58, 11, 0]])

# Algoritmayı çalıştırın
KKA = KARINCA_KOLONI_ALGORITMASI(itirasyon=50)
KKA.Run()

# Rotaları ve maliyetleri gösterin
rotalar = KKA.seyhatRotasi
maliyet = KKA.GetRotlarUzunlugu(rotalar, uzaklik_matris)

print("Rotalar:")
print(rotalar)
print("Maliyet:")
print(maliyet)

```
