Tavlama Benzetimi Algoritması (Simulated Annealing) Kodu

Açıklama:

Bu kod, Tavlama Benzetimi algoritmasının Python uygulamasıdır. Algoritma, metallerin tavlama sürecinden esinlenerek, bir problemin en iyi veya en yakın çözümünü bulmak için kullanılır.

Kodun Yapısı:
    •	SimulatedAnnealing sınıfı: Algoritmanın ana yapısını oluşturur.
    •	Önemli yöntemler:
    •	Run(): Algoritmayı çalıştırır.
    •	random_start(): Rastgele bir başlangıç değeri üretir.
    •	Temperature(): Sıcaklık değerini günceller.
    •	Random_neighbour() ve Random_neighbour2(): Komşu çözümleri üretir.
    •	Clip(): Çözümleri aralık içinde sınırlandırır.
    •	Acceptance_probability(): Yeni çözümleri kabul etme olasılığını hesaplar.
    •	Cost_function(): Çözümlerin uygunluk değerini hesaplar.
        Show_Chart(): Algoritmanın ilerleyişini grafik olarak gösterir.

        
Kodun Kullanımı:
1.	Kodu Python ortamında çalıştırın.
2.	SimulatedAnnealing().Run() komutuyla algoritmayı başlatın.
3.	Algoritma, en iyi çözümü ve maliyetini ekrana yazdıracaktır.
4.	Grafikler de otomatik olarak oluşturulacaktır.


Önemli Notlar:
•	Kodda kullanılan parametreler (aralık, iterasyon sayısı, başlangıç sıcaklığı) ihtiyaca göre değiştirilebilir.
•	Algoritmanın performansı, problemin yapısına ve parametrelerin ayarlanmasına bağlıdır.
