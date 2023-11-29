##### ==========================================================EN===================================================================

Code Usage

The code is written in Python and uses the NumPy and Matplotlib libraries. To run the code, follow these steps:


``` 
Change the min, max, population_length, selection_size, kromozom_length, clone_rate, mutation_rate, and itirations variables to your own settings.

``` 
Run the code in a Python interpreter.
The code will produce the following outputs:

The average affinity value of the best 5 chromosomes for each iteration.
The affinity value of the best chromosome over iterations.
Code Explanation

The code uses the following basic concepts:

Population: A set of candidate solutions.
Affinity: A value representing the quality of a solution.
Selection: The selection of solutions with the best affinity values.
Cloning: The replication of selected solutions.
Mutation: The addition of new genetic material to cloned solutions.
The code uses these concepts in the following order:

The CreatePopulation() function creates a random population.
The GetAffinity() function calculates the affinity value of each chromosome.
The SetTheBestAffinity() function records the best affinity value for each iteration.
The Clone() function creates clones of the selected chromosomes.
The MakeClone() function combines the cloned chromosomes.
The Hypermutate() function applies mutation to the cloned chromosomes.
The select() function selects solutions with the best affinity values.
Example Application

The code is illustrated in the following example application:

Python
# Set up the code
min = -5
max = 5
population_length = 20
selection_size = 5
kromozom_length = 3
clone_rate = 20
mutation_rate = 0.3
itirations = 500

# Run the code
``` 
ybs = YBS(min=min, max=max, population_length=population_length,
            selection_size=selection_size, kromozom_length=kromozom_length,
            clone_rate=clone_rate, mutation_rate=mutation_rate,
            itirations=itirations)
ybs.Run()
ybs.ShowChart()
``` 

This code uses the CSA algorithm to optimize the f(x) = x^2 function. After running the code, we get the following output:
``` 
Iteration: 0, Best 5 Chromosomes Average: 25
Iteration: 1, Best 5 Chromosomes Average: 40
Iteration: 2, Best 5 Chromosomes Average: 56.25
...
Iteration: 499, Best 5 Chromosomes Average: 82.5
Iteration: 500, Best 5 Chromosomes Average: 82.5
``` 
Examining the graph, we can see that the best affinity value increases over time. This suggests that the CSA algorithm has been able to find a good solution for the optimized function.

Additional Notes

The min and max variables define the range of possible values for a chromosome.

The population_length variable defines the number of chromosomes in the population.

The selection_size variable defines the number of chromosomes selected for cloning.

The kromozom_length variable defines the length of each chromosome.

The clone_rate variable defines the number of clones created for each selected chromosome.

The mutation_rate variable defines the probability of a mutation occurring for each chromosome.

The itirations variable defines the number of iterations the algorithm will run.

The CreatePopulation() function creates a random population of chromosomes. Each chromosome is a list of numbers.

The GetAffinity() function calculates the affinity value of a chromosome. The affinity value is a measure of the quality of a solution.

The SetTheBestAffinity() function records the best affinity value for each iteration.

The Clone() function creates clones of a chromosome. The clones are exact copies of the original chromosome.

The MakeClone() function combines the cloned chromosomes. The combined chromosomes are a single population of chromosomes.

The Hypermutate() function applies mutation to a chromosome. Mutation can change the values of one or more genes in a chromosome.

The select() function selects solutions with the best affinity values. The selected solutions are used to create the next population of chromosomes.


##### ==========================================================TR===================================================================

Kod Kullanımı

Kod, Python dilinde yazılmıştır ve NumPy ve Matplotlib kütüphanelerini kullanır. Kodu çalıştırmak için aşağıdaki adımları izleyin:


```
min, max, population_length, selection_size, kromozom_length, clone_rate, mutation_rate ve itirations
değişkenlerini kendi ayarlarınıza göre değiştirin.
``` 

Kodu bir Python yorumlayıcısında çalıştırın.
Kod, aşağıdaki çıktıları üretecektir:

Her iterasyon için en iyi 5 kromozomun ortalama uyumluluk değeri.
İterasyonlar boyunca en iyi kromozomun uyumluluk değeri.
Kod Açıklaması

Kod, aşağıdaki temel kavramları kullanır:

Popülasyon: Bir dizi aday çözüm.
Uyumluluk: Bir çözümün kalitesini temsil eden bir değer.
Seçim: En iyi uyumluluk değerlerine sahip çözümlerin seçilmesi.
Klonlama: Seçilen çözümlerin çoğaltılması.
Mutasyon: Klonlanmış çözümlere yeni genetik materyalin eklenmesi.
Kod, bu kavramları aşağıdaki sırayla kullanır:

CreatePopulation() işlevi, rastgele bir popülasyon oluşturur.
GetAffinity() işlevi, her kromozomun uyumluluk değerini hesaplar.
SetTheBestAffinity() işlevi, her iterasyon için en iyi uyumluluk değerini kaydeder.
Clone() işlevi, seçilen kromozomların klonlarını oluşturur.
MakeClone() işlevi, klonlanmış kromozomları bir araya getirir.
Hypermutate() işlevi, klonlanmış kromozomlara mutasyon uygular.
select() işlevi, en iyi uyumluluk değerlerine sahip çözümleri seçer.

Örnek Uygulama

Kod, aşağıdaki örnek uygulamada gösterilmiştir:

Python
# Kodu ayarlayın
min = -5
max = 5
population_length = 20
selection_size = 5
kromozom_length = 3
clone_rate = 20
mutation_rate = 0.3
itirations = 500

# Kodu çalıştırın
```
ybs = YBS(min=min, max=max, population_length=population_length,
            selection_size=selection_size, kromozom_length=kromozom_length,
            clone_rate=clone_rate, mutation_rate=mutation_rate,
            itirations=itirations)
ybs.Run()
ybs.ShowChart()
```

Bu kod, f(x) = x^2 fonksiyonunu optimize etmek için CSA algoritmasını kullanır. Kodu çalıştırdıktan sonra aşağıdaki çıktıyı elde ederiz:
```
Iterasyon: 0, En İyi 5 Kromozom Ortalaması: 25
Iterasyon: 1, En İyi 5 Kromozom Ortalaması: 40
Iterasyon: 2, En İyi 5 Kromozom Ortalaması: 56.25
...
Iterasyon: 499, En İyi 5 Kromozom Ortalaması: 82.5
Iterasyon: 500, En İyi 5 Kromozom Ortalaması: 82.5
```
Grafiği incelediğimizde, en iyi uyumluluk değerinin zamanla arttığını görebiliriz. Bu, CSA algoritmasının optimize edilen fonksiyon için iyi bir çözüm bulmayı başardığını gösterir.


#   Değişkenler

min ve max değişkenleri, bir kromozom için olası değer aralığını belirler.
population_length değişkeni, popülasyondaki kromozom sayısını belirtir.
selection_size değişkeni, klonlama için seçilen kromozom sayısını belirtir.
kromozom_length değişkeni, her kromozomun uzunluğunu belirtir.
clone_rate değişkeni, seçilen her kromozom için oluşturulan klon sayısını belirtir.
mutation_rate değişkeni, her kromozom için mutasyon meydana gelme olasılığını belirtir.
itirations değişkeni, algoritmanın çalıştıracağı yineleme sayısını belirtir.

#   Fonksiyonlar

CreatePopulation() fonksiyonu, rastgele kromozom popülasyonu oluşturur. Her kromozom bir sayılar listesidir.
GetAffinity() fonksiyonu, bir kromozomun uyumluluk değerini hesaplar. Uyumluluk değeri, bir çözümün kalitesinin bir ölçüsüdür.
SetTheBestAffinity() fonksiyonu, her yineleme için en iyi uyumluluk değerini kaydeder.
Clone() fonksiyonu, bir kromozomun klonlarını oluşturur. Klonlar, orijinal kromozomun tam kopyalarıdır.
MakeClone() fonksiyonu, klonlanmış kromozomları birleştirir. Birleştirilmiş kromozomlar, tek bir kromozom popülasyonudur.
Hypermutate() fonksiyonu, bir kromozomda mutasyon uygular. Mutasyon, bir kromozomdaki bir veya daha fazla genin değerlerini değiştirebilir.
select() fonksiyonu, en iyi uyumluluk değerlerine sahip çözümleri seçer. Seçilen çözümler, bir sonraki kromozom popülasyonunu oluşturmak için kullanılır.