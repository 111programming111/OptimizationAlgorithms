##### ==========================================================EN===================================================================
Introduction
This document provides a detailed explanation of the PSO algorithm implementation and its usage.

PSO Algorithm
The Particle Swarm Optimization (PSO) algorithm is a metaheuristic approach inspired by the social behavior of bird flocks and fish schools. It utilizes a population of particles, each representing a potential solution to an optimization problem, and iteratively updates their positions based on their own best-known positions and the best-known position of the entire population.

Implementation Details
The PSO implementation in this code includes the following key features:

Particle Representation: Each particle is represented as a two-dimensional vector, corresponding to the two optimization variables (X1 and X2) in the problem.

Fitness Function: The fitness function evaluates the quality of each particle's solution. In this case, the fitness function is defined as:

Python
```
def fun(self,x1, x2):
    z= (4*x1**2) - (2.1*x1**4)+ ((1/3)*x1**6) + x1*x2 - (4*x2**2) + (4*x2**4)
    return z
```

Kodu kullanırken dikkatli olun. Daha fazla bilgi
Parameter Settings: The PSO algorithm parameters are set as follows:

    1-parca_sayisi: Number of particles (10 in this case)

    2-itirasyon: Number of iterations (50 in this case)

    3-c1: Social parameter (2 in this case)

    4-c2: Cognitive parameter (2 in this case)

    5-w: Inertia weight (0.729 in this case)

Algorithm Execution
The Run() method initiates the PSO algorithm's execution. It performs the following steps:

    1-Initializes the particle positions and velocities randomly.

    2-Calculates the fitness of each particle.

    3-Updates the best positions of each particle and the global best position.

    4-Updates the velocities of each particle based on their own best positions, the global best position, and the inertia weight.

    5-Repeats steps 2 to 4 for the specified number of iterations.

Output and Visualization
The algorithm generates a log file (PSO_Log.txt) containing detailed information about the particle positions, velocities, fitness values, and best positions at each iteration.

Additionally, the algorithm generates three visualization plots:

    1-X1_degeri.png: Plots the X1 values over the iterations.

    2-X2_degeri.png: Plots the X2 values over the iterations.

    3-Fonksiyon_uygunluk_.png: Plots the fitness values over the iterations.

Usage Example
To run the PSO algorithm, create an instance of the PSO class and call the Run() method. For instance:

Python
```
pso = PSO(parca_sayisi=10, itirasyon=50)
pso.Run()
```
This will execute the PSO algorithm with 10 particles and 50 iterations, generating the corresponding log file and visualization plots.



##### ==========================================================TR===================================================================

Giriş

Bu belge, PSO algoritması uygulamasının ayrıntılı bir açıklamasını ve kullanımını sunmaktadır.

PSO Algoritması

Parçacık Sürü Optimizasyonu (PSO) algoritması, kuş sürülerinin ve balık okullarının sosyal davranışından esinlenen bir metaheuristic yaklaşımdır. Bir optimizasyon problemine potansiyel bir çözümü temsil eden bir nüfusun parçacıklarını kullanır ve kendi en iyi bilinen konumlarına ve nüfusun tamamının en iyi bilinen konumuna göre konumlarını yinelemeli olarak günceller.

Uygulama Detayları

Bu koddaki PSO uygulaması aşağıdaki temel özellikleri içerir:

Parçacık Temsili: Her parçacık, problemdeki iki optimizasyon değişkenine (X1 ve X2) karşılık gelen iki boyutlu bir vektör olarak temsil edilir.

Uygunluk Fonksiyonu: Uygunluk fonksiyonu, her parçacığın çözümünün kalitesini değerlendirir. Bu durumda, uygunluk fonksiyonu şu şekilde tanımlanmıştır:

```
def fun(self,x1, x2):
      z= (4*x1**2) - (2.1*x1**4)+ ((1/3)*x1**6) + x1*x2 - (4*x2**2) + (4*x2**4)
      return z
```

Parametre Ayarları: PSO algoritması parametreleri şu şekilde ayarlanmıştır:

    1-parca_sayisi: Parçacık sayısı (bu durumda 10)

    2-itirasyon: İterasyon sayısı (bu durumda 50)

    3-c1: Sosyal parametre (bu durumda 2)

    4-c2: Bilişsel parametre (bu durumda 2)

    5-w: İnertia ağırlığı (bu durumda 0.729)

Algoritma Çalıştırılması

Run() yöntemi PSO algoritmasının yürütülmesini başlatır. Aşağıdaki adımları gerçekleştirir:

    1-Parçacık konumlarını ve hızlarını rastgele olarak başlatır.

    2-Her parçacığın uygunluğunu hesaplar.

    3-Her parçacığın en iyi konumlarını ve küresel en iyi konumu günceller.

    4-Her parçacığın hızlarını kendi en iyi konumlarına, küresel en iyi konuma ve inertia ağırlığına göre günceller.

    5-Belirtilen iterasyon sayısı için 2. ila 4. adımları tekrar eder.

Çıktı ve Görselleştirme

Algoritma, her iterasyonda parçacık konumları, hızları, uygunluk değerleri ve en iyi konumları hakkında ayrıntılı bilgi içeren bir günlük dosyası (PSO_Log.txt) oluşturur.

Ek olarak, algoritma üç görselleştirme grafiği oluşturur:

    1-X1_degeri.png: X1 değerlerini iterasyonlar boyunca çizer.

    2-X2_degeri.png: X2 değerlerini iterasyonlar boyunca çizer.

    3-Fonksiyon_uygunluk_.png: Uygunluk değerlerini iterasyonlar boyunca çizer.

Kullanım Örneği

PSO algoritmasını çalıştırmak için, PSO sınıfının bir örneğini oluşturun ve Run() yöntemini çağırın. Örneğin:
```
pso = PSO(parca_sayisi=10, itirasyon=50)
pso.Run()
```

Bu, 10 parçacık ve 50 yineleme ile PSO algoritmasını çalıştıracak ve ilgili günlük dosyasını ve görselleştirme grafiklerini oluşturacaktır.
