import random
import datetime
import matplotlib.pyplot as plt


class DEA():
    def __init__(self, IterationsNumber=100, populationLength=6, CR=0.5, getMax=True):
        self.IterationsNumber = IterationsNumber
        self.populasyon = []
        self.degiskeSayisi = 5
        self.populasyonLength = populationLength
        self.vectorIndexList = []     # length = 2
        self.mutasyonIndex = []       # length = 1
        self.CR = CR
        self.newPopulasyon = []
        self.betterValues = []
        self.getMax = getMax

        with open('DEA_Log.txt', 'w') as f:
            f.write('\n')

    def writeToFile(self, data, title):
        with open('DEA_Log.txt', 'a') as f:
            f.write(title)
            f.write('\n')
            f.write(str(datetime.datetime.now())+"  ")
            f.write(str(data))
            f.write('\n \n')

    def RandNumber(self):
        # Generate a random integer between 0 and 1
        random_int = random.random()
        return random_int

    def CreatePopulasyon(self):
        populasyon = []
        for i in range(self.populasyonLength):
            kromozom = []
            for j in range(self.degiskeSayisi):
                kromozom.append(self.RandNumber())
            populasyon.append(kromozom)
        return populasyon

    # Get Vector index

    def GetVectorIndexList(self):
        index = random.randint(0, 5)
        if (len(self.vectorIndexList) == 2):
            return
        if index not in self.vectorIndexList and index != self.targetIndex:
            self.vectorIndexList.append(index)
        self.GetVectorIndexList()     # Recursive function

    # Get mutasyon index

    def GetMutasyonIndex(self):
        index = random.randint(0, 5)
        if index not in self.vectorIndexList and index != self.targetIndex:
            self.mutasyonIndex.append(index)
            return
        self.GetMutasyonIndex()       # Recursive function

    def MakeWeightingForVector(self):
        result = [a - b for a, b in zip(self.populasyon[self.vectorIndexList[0]],
                                        self.populasyon[self.vectorIndexList[1]])]
        rand = 0 + random.random()*(2-0)
        result = [item * rand for item in result]
        # self.writeToFile(result,"Caprazlama")
        return result

    def MakeMutasyon(self, caprazlamaResult: list):
        result = [
            a + b for a, b in zip(self.populasyon[self.mutasyonIndex[0]], caprazlamaResult)]
        return result

    def SelectGenFromKromozom(self, targetKromozom: list, mutsyonResultKromozom: list):
        kromozom = []
        for i in range(self.degiskeSayisi):
            rand = random.random()
            if rand < self.CR:
                kromozom.append(targetKromozom[i])
            else:
                kromozom.append(mutsyonResultKromozom[i])
        return kromozom

    def fun(self, kromozom: list):
        result = sum(kromozom)
        return result

    def GetTheBetterResult(self, theSelectedNewKromozom: list, tagetKromozom: list):
        r1 = self.fun(theSelectedNewKromozom)
        r2 = self.fun(tagetKromozom)
        if self.getMax:
            if r1 > r2:
                return theSelectedNewKromozom
            else:
                return tagetKromozom
        else:
            if r1 < r2:
                return theSelectedNewKromozom
            else:
                return tagetKromozom

    def Run(self):
        self.populasyon = self.CreatePopulasyon()
        self.writeToFile(self.populasyon, "populasyon")
        for i in range(self.IterationsNumber):
            for j in range(self.populasyonLength):
                self.targetIndex = j
                self.targetKromozom = self.populasyon[self.targetIndex]
                self.GetVectorIndexList()
                self.GetMutasyonIndex()
                vectorResult = self.MakeWeightingForVector()
                mutsyonResultKromozom = self.MakeMutasyon(vectorResult)
                theSelectedNewKromozom = self.SelectGenFromKromozom(
                    self.targetKromozom, mutsyonResultKromozom)
                theSelectedNewKromozom = self.GetTheBetterResult(
                    theSelectedNewKromozom, self.targetKromozom)
                self.newPopulasyon.append(theSelectedNewKromozom)
            self.populasyon = self.newPopulasyon
            self.SetValue(self.populasyon)
            self.writeToFile(self.populasyon, "populasyon")
            self.ResetVariables()

        self.writeToFile(self.betterValues, "betterValues")

    def ResetVariables(self):
        self.vectorIndexList = []
        self.mutasyonIndex = []
        self.newPopulasyon = []

    def SetValue(self, populasyon: list):
        maxOrMin = sum(populasyon[0])
        for item in populasyon:
            val = sum(item)
            if self.getMax:
                if val > maxOrMin:
                    maxOrMin = val
            else:
                if val < maxOrMin:
                    maxOrMin = val
        self.betterValues.append(maxOrMin)

    def ShowChart(self):
        x = range(0, self.IterationsNumber)
        y = self.betterValues
        # Create two new figures.
        fig1 = plt.figure()
        # # Add a subplot to each figure.
        ax1 = fig1.add_subplot(111)
        # # Plot the data in each subplot.
        ax1.plot(x, y, 'b-')
        # Set the labels and titles for each chart.
        ax1.set_xlabel('itirasyon')
        ax1.set_ylabel('uygunluk değeri')
        ax1.set_title('Uygunluk Fonksiyonu')
        plt.legend(loc='upper right')
        # # Save the figures.
        fig1.savefig('uygunlik_Fonksiyonu max.png')
        plt.show()


dea = DEA(getMax=True, IterationsNumber=100)
dea.Run()
dea.ShowChart()
