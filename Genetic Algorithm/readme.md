#### ==========================================================EN===================================================================

Genetic Algorithm
This repository contains the implementation of a genetic algorithm (GA) for solving optimization problems. The GA is a metaheuristic search algorithm inspired by the natural selection process. It works by iteratively evolving a population of potential solutions, using operators such as crossover and mutation to improve the fitness of the solutions.

Usage
To use the GA, you can create an instance of the GeneticAlgorithm class and call the RunAlgorithim() method. This will run the GA for the specified number of iterations.

##### Python Code
```
ga = GeneticAlgorithm(IterationsNumber=100, populationLength=10, CrossoverRatio=0.7, MutateRatio=0.001, minValue=1, maxValue=31)
ga.RunAlgorithim()
```

Output
The GA will print the best solution found at each iteration to the console. You can also use the ShowChart() method to visualize the fitness and x values over the iterations.

##### Python Code
```
ga.ShowChart()
```
Parameters
The GA has several parameters that can be adjusted to control its behavior. These parameters are:

    1-IterationsNumber: The number of iterations to run the GA.
    2-populationLength: The size of the population.
    3-CrossoverRatio: The probability of performing crossover.
    4-MutateRatio: The probability of performing mutation.
    5-minValue: The minimum value of the problem variables.
    6-maxValue: The maximum value of the problem variables.
Example
##### Python Code
```
ga = GeneticAlgorithm(IterationsNumber=10000, populationLength=100, CrossoverRatio=0.7, MutateRatio=0.001, minValue=1, maxValue=31)
ga.RunAlgorithim()
ga.ShowChart()
```

#### ==========================================================TR===================================================================




Genetik Algoritma
Bu depo, optimizasyon problemlerini çözmek için bir genetik algoritma (GA) uygulamasını içerir. GA, doğal seleksiyon sürecinin esinlenmesinden ortaya çıkan bir metaheuristik arama algoritmasıdır. Çözümlerin uygunluğunu iyileştirmek için çaprazlama ve mutasyon gibi işlemler kullanarak, potansiyel çözümlerin bir popülasyonunu yinelemeli olarak geliştirerek çalışır.

Kullanım
GA'yı kullanmak için, GeneticAlgorithm sınıfının bir örneğini oluşturun ve RunAlgorithim() yöntemini çağırın. Bu, GA'yı belirtilen iterasyon sayısı için çalıştıracaktır.

##### Python Code
```
ga = GeneticAlgorithm(IterationsNumber=100, populationLength=10, CrossoverRatio=0.7, MutateRatio=0.001, minValue=1, maxValue=31)
ga.RunAlgorithim()
```

Çıktı
GA, her iterasyonda bulunan en iyi çözümü konsola yazdıracaktır. Ayrıca, yinelemeler boyunca uygunluk ve x değerlerini görselleştirmek için ShowChart() yöntemini de kullanabilirsiniz.

##### Python Code
```
ga.ShowChart()
```

Parametreler
GA, davranışını kontrol etmek için ayarlanabilecek birkaç parametreye sahiptir. Bu parametreler şunlardır:

    1-IterationsNumber: GA'yı çalıştırılacak iterasyon sayısı.
    2-populationLength: Popülasyonun boyutu.
    3-CrossoverRatio: Çaprazlama gerçekleştirme olasılığı.
    4-MutateRatio: Mutasyon gerçekleştirme olasılığı.
    5-minValue: Problem değişkenlerinin minimum değeri.
    6-maxValue: Problem değişkenlerinin maksimum değeri.
Örnek
##### Python Code
```
ga = GeneticAlgorithm(IterationsNumber=10000, populationLength=100, CrossoverRatio=0.7, MutateRatio=0.001, minValue=1, maxValue=31)
ga.RunAlgorithim()
ga.ShowChart()
```

