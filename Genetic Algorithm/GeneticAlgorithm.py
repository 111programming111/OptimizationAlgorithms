import random
import matplotlib.pyplot as plt

class GeneticAlgorithm():
    
    def __init__(self, IterationsNumber = 10, populationLength = 6,CrossoverRatio= 0.7 ,MutateRatio = 0.001, minValue = 1, maxValue = 31):
        
        self.iterationsNumber = IterationsNumber
        self.populationLength = populationLength
        self.CrossoverRatio = CrossoverRatio
        self.MutateRatio = MutateRatio
        self.minValue = minValue
        self.maxValue = maxValue
        self.BinaryNumberLength = 0
        self.BinaryNumberLength = len(self.ConvertIntegerNumberToBinary(maxValue))

        self.Data = []
        self.Data2= []

    def RunAlgorithim(self):
        populasyon = self.CreatePopulasyon(self.populationLength)
        print(populasyon)

        from tqdm import tqdm


        for i in tqdm(range(self.iterationsNumber)):
            
            fitness = self.FitnessCalculate(populasyon)
            # print(fitness)
            fitness = sorted(fitness , key=lambda x:x[1])


            sum_Fitness = self.SumFitness(fitness)
            # print(sum_Fitness)


            fitness_Ratio = self.FitnessRatio(fitness, sum_Fitness)
            # print(fitness_Ratio)
            fitness_Ratio = sorted(fitness_Ratio, key=lambda x: x[1])


            cumulative_Ratio = self.CumulativeRatio(fitness_Ratio)
            # print(cumulative_Ratio)

            # Select Process
            newpopulasyon = self.SelectFromPopulasyon(cumulative_Ratio)
            # print(newpopulasyon)

            caprazlama_populasyon = self.PopulasyonCaprazla(newpopulasyon)

            # print(caprazlama_populasyon)

            mutasyonPopulasyon = self.PopulasyonMutasyon(caprazlama_populasyon)

            # print(mutasyonPopulasyon)

            getTheBest = self.CheckToPoulasyon(mutasyonPopulasyon ,fitness)


            populasyon = self.GetPopulasyon(getTheBest)

            maxt =self.Getmax(fitness)
            self.Data.append(maxt[0])
            self.Data2.append(self.Binary2Int(maxt[1]))


    def RandNumber(self):
        # Generate a random integer between 0 and 31
        random_int = random.randint(self.minValue, self.maxValue)
        return random_int


    def ConvertIntegerNumberToBinary(self,int_Number: int):
            binary_Number = ""
            while(int_Number > 0):
                kalan = int_Number % 2
                bol = int(int_Number / 2)

                binary_Number = str(kalan) + binary_Number

                int_Number = bol
            if(self.BinaryNumberLength != 0):
                fark  = self.BinaryNumberLength - len(binary_Number)
                if(fark > 0):
                    for i in range(fark):
                        binary_Number = "0" +binary_Number

            return binary_Number


    def UgunlukHesaplama(self,number : int):
        result = (15 * number) - number**2
        return result


    def SumFitness(self,fitness : list):
        sum_fitness = 0
        for item in fitness:
            sum_fitness += item[1]
        return sum_fitness


    def CreatePopulasyon(self,length: int):
        populasyon = []
        for item in range(length):
            
            intNumber = self.RandNumber()

            binary_Format = self.ConvertIntegerNumberToBinary(intNumber)

            populasyon.append([binary_Format,intNumber])

        return populasyon


    def FitnessCalculate(self,populasyon : list):
        fitness = []
        for item in populasyon:
            uygunluk_Degeri = self.UgunlukHesaplama(item[1])
            if uygunluk_Degeri < 0:
                uygunluk_Degeri = item[1] * 0.001
            fitness.append([item[0],uygunluk_Degeri])

        return fitness


    def FitnessRatio(self,fitness : list,sum_Fitness: int):
        fitness_Ratio = []
        for item in fitness:
            ratio = round(item[1] * (100 / sum_Fitness), 2) 
            fitness_Ratio.append([item[0],ratio])

        return fitness_Ratio


    def CumulativeRatio(self,fitness_Ratio: list):
        cumulative_Ratio = []
        for i in range(len(fitness_Ratio)):
            if(i == 0):
                cumulative_Ratio.append([fitness_Ratio[i][0],round(fitness_Ratio[i][1],2) ])
            else:
                cumulative_Ratio.append([fitness_Ratio[i][0],round(fitness_Ratio[i][1] + cumulative_Ratio[i-1][1],2)])

        return cumulative_Ratio


    def SelectFromPopulasyon(self, cumulative_Ratio: list):
            newpopulasyon = []
            for i in range(self.populationLength):        
                rand = random.randint(0, 99)
                for item in cumulative_Ratio:
                    if(item[1] >= rand):
                        newpopulasyon.append(item[0])
                        break
                    
            return newpopulasyon


    def KromozomCaprazlama(self,item1: int, item2: int,olasilik: float):
        newItem1 = item1
        newItem2 = item2
        rand = random.random()
        if(rand < olasilik):
            index = random.randint(0,4)
            newItem1 = item1[:index] + item2[index:]
            newItem2 = item2[:index] + item1[index:]

        return [newItem1, newItem2]


    def PopulasyonCaprazla(self, newpopulasyon: list):
        for i in range(0,self.populationLength,2):
            newItmes = self.KromozomCaprazlama(newpopulasyon[i],newpopulasyon[i+1],self.CrossoverRatio)
            newpopulasyon[i] = newItmes[0]
            newpopulasyon[i+1] =newItmes[1]
        
        return newpopulasyon


    def PopulasyonMutasyon(self,caprazlama_populasyon: list):

        mutasyonPopulasyon = []

        for item in caprazlama_populasyon:
            
            rand = random.random()
            if(rand < self.MutateRatio):
                index = random.randint(0,self.BinaryNumberLength -1)
                if(item[index] == '0'):
                    item = item[:index] + '1' + item[index + 1:]
                else:
                    item = item[:index] + '0' + item[index + 1:]
                print("Mutasyon oldu")    
            mutasyonPopulasyon.append(item)

        return mutasyonPopulasyon


    def Binary2Int(self,binary_number):
        integer = 0
        for i in range(len(binary_number) - 1, -1, -1):
            integer += int(binary_number[i]) * 2**(len(binary_number)- 1 - i) 
        return integer


    def GetPopulasyon(self,mutasyonPopulasyon):
        populasyon=[]
        for item in mutasyonPopulasyon:
            integer  = self.Binary2Int(item)
            populasyon.append([item,integer])

        return populasyon


    def Getmax(self,populasuon: list):
        max = populasuon[0][1]
        value = populasuon[0][0]
        for item in populasuon:
            if((item[1]) > max):
                max=  (item[1])
                value = item[0]
            
        return [max , value]


    def CheckToPoulasyon(self,mutasyonPopulasyon: list , fitness:list):
        fitnessTest = []
        for i in range(len(mutasyonPopulasyon)):
            fitnessTest.append([mutasyonPopulasyon[i],self.Binary2Int(mutasyonPopulasyon[i])])
        fitnessTest =self.FitnessCalculate(fitnessTest)
        fitnessTest = sorted(fitnessTest,key= lambda x:x[1])
        fitnessTest[0] = fitness[len(fitness)-1]
        rtFitness = []
        for item in fitnessTest:
            rtFitness.append(item[0])
        return rtFitness


    def ShowBarChart(self):
        plt.bar(range(len(self.Data)), self.Data)
        plt.title("Genetik Alogritma . Max value  = "+ str(max(self.Data)))
        plt.xlabel("iterasyon sayisi")
        plt.ylabel("tahmin degeri")
        plt.show()


    def ShowChart(self):
        x = range(0, self.iterationsNumber)
        y = self.Data
        y2 = self.Data2

        # Create two new figures.
        fig1 = plt.figure()
        fig2 = plt.figure()

        # # Add a subplot to each figure.
        ax1 = fig1.add_subplot(111)
        ax2 = fig2.add_subplot(111)

        # # Plot the data in each subplot.
        ax1.plot(x, y, 'b-')
        ax2.plot(x, y2, 'r-')
        # Set the labels and titles for each chart.
        ax1.set_xlabel('itirasyon')
        ax1.set_ylabel('uygunluk değeri')
        ax1.set_title('Uygunluk Fonksiyonu')
        plt.legend(loc='upper right')
        ax2.set_xlabel('x')
        ax2.set_ylabel('x değeri')
        ax2.set_title('Max x değeri')

        # # Save the figures.
        fig1.savefig('uygunlik_Fonksiyonu3.png')
        fig2.savefig('x_degeri3.png')


        plt.figure(figsize=(8, 8))
        plt.subplot(2, 1, 1)
        plt.plot(self.Data, label='Uygunluk')

        plt.legend(loc='lower right')
        plt.ylabel('uygunluk değeri')
        plt.ylim([0, 70])
        plt.title('Uygunluk Fonkisyon')

        plt.subplot(2, 1, 2)
        plt.plot(self.Data2, label='x değeri')
        plt.legend(loc='upper right')
        plt.ylabel('X değeri')
        plt.ylim([0,31])
        plt.title('X Max değeri')
        plt.xlabel('Itirasyon')
        plt.savefig('general.png')
        plt.show()




#====================================================================================================
#====================================================================================================
#====================================================================================================
#====================================================================================================
#====================================================================================================
#====================================================================================================

GA = GeneticAlgorithm(IterationsNumber = 10000)
GA.RunAlgorithim()
GA.ShowChart()