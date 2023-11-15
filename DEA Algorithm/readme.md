##### ==========================================================EN===================================================================

Differential Evolution (DEA) Algorithm
This repository contains the implementation of a Differential Evolution (DEA) algorithm for optimization problems.

Algorithm Description

DEA is a population-based optimization algorithm inspired by the natural selection process. It works by iteratively evolving a population of potential solutions, using operators such as crossover and mutation.

In the DEA algorithm, each individual in the population represents a potential solution to the problem. The algorithm starts by creating a random initial population of individuals. Then, at each iteration, the algorithm performs the following steps:

    1-Selection: Select a target individual from the population.

    2-Weighting: Create two weighting vectors by randomly selecting two individuals from the population and subtracting their corresponding components.

    3-Mutation: Apply the weighting vectors to the target individual to generate a trial individual.

    4-Crossover: Combine the target individual and the trial individual to generate a new individual.

    5-Evaluation: Compare the new individual to the target individual and update the population if the new individual is better.

The algorithm continues to iterate until a stopping criterion is met, such as a maximum number of iterations or a satisfactory solution is found.

Usage

To use the DEA algorithm, you can create an instance of the DEA class and call the Run() method. This will run the DEA algorithm for the specified number of iterations.

##### Python Code
dea = DEA(IterationsNumber=100, populationLength=10, CR=0.5, getMax=False)
dea.Run()


Output

The DEA algorithm will print the best solution found at each iteration to the console. You can also use the ShowChart() method to visualize the fitness values over the iterations.

##### Python Code
dea.ShowChart()

Parameters

The DEA algorithm has several parameters that can be adjusted to control its behavior. These parameters are:

IterationsNumber: The number of iterations to run the DEA algorithm.
populationLength: The size of the population.
CR: The crossover rate.
getMax: Whether to find the maximum or minimum value.
Example

##### Python Code
dea = DEA(IterationsNumber=10000, populationLength=100, CR=0.5, getMax=False)
dea.Run()
dea.ShowChart()




##### ==========================================================TR===================================================================


Differential Evolution (DEA) Algoritması
Bu depo, optimizasyon problemleri için bir Differential Evolution (DEA) algoritmasının uygulamasını içerir.

Algoritma Açıklaması

DEA, doğal seleksiyon sürecinden esinlenen popülasyon tabanlı bir optimizasyon algoritmasıdır. Çaprazlama ve mutasyon gibi işlemler kullanarak, potansiyel çözümlerin bir popülasyonunu yinelemeli olarak geliştirerek çalışır.

DEA algoritmasında, popülasyondaki her birey, soruna potansiyel bir çözümü temsil eder. Algoritma, rastgele bir başlangıç ​​popülasyonu bireyi oluşturarak başlar. Ardından, her yinelemede algoritma aşağıdaki adımları gerçekleştirir:

    1-Seçim: Popülasyondan hedef bir birey seçin.

    2-Ağırlıklandırma: Popülasyondan rastgele iki birey seçerek ve karşılık gelen bileşenlerini çıkararak iki ağırlık vektörü oluşturun.

    3-Mutasyon: Bir deneme bireyi oluşturmak için ağırlık vektörlerini hedef bireye uygulayın.

    4-Çaprazlama: Yeni bir birey oluşturmak için hedef bireyi ve deneme bireyini birleştirin.

    5-Değerlendirme: Yeni bireyi hedef bireyle karşılaştırın ve yeni birey daha iyiyse popülasyonu güncelleyin.

Algoritma, durdurma kriteri karşılanana kadar yinelemeye devam eder, örneğin maksimum sayıda yineleme veya tatmin edici bir çözüm bulunur.

Kullanım

DEA algoritmasını kullanmak için, DEA sınıfının bir örneğini oluşturun ve Run() yöntemini çağırın. Bu, DEA algoritmasını belirtilen sayıda yineleme için çalıştıracaktır.

##### Python Code
dea = DEA(IterationsNumber=100, populationLength=10, CR=0.5, getMax=False)
dea.Run()

Çıktı

DEA algoritması, her yinelemede bulunan en iyi çözümü konsola yazdıracaktır. Ayrıca, ShowChart() yöntemini yinelemeler boyunca uygunluk değerlerini görselleştirmek için