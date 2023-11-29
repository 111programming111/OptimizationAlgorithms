import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pprint import pprint
from numpy.random import uniform
import datetime
from tqdm import tqdm
'''
1  Create Population
2  Calculate Affinity for all population items
3  Sorted population items by affinity result
4  Select the best affinity
5  Select from population for train according to selection_size parametre
6  Make Clone for all items(kromozom) in the selection population 
7  Make mutation for new population_clones
8  Select the best affinty from population and mutation pooulation and set these to population
'''


class YBS():

    def __init__(self, min=-5, max=5, population_length=40, selection_size=5,
                 kromozom_length=3, clone_rate=20, mutation_rate=0.3, itirations=50):
        # Inputs parameters
        self.min, self.max = (min, max)
        self.population_length = population_length
        self.selection_size = selection_size
        self.kromozom_length = kromozom_length
        self.clone_rate = clone_rate
        self.mutation_rate = mutation_rate
        self.itirations = itirations
        self.population = []
        self.best_affinity_it = []

        with open('YBS_Log.txt', 'w') as f:
            f.write('\n')

    def writeToFile(self, data, title):
        with open('YBS_Log.txt', 'a') as f:
            f.write(title)
            f.write('\n')
            f.write(str(datetime.datetime.now())+"  ")
            f.write(str(data))
            f.write('\n \n')

    def CreatePopulation(self):
        population = []
        for item in range(self.population_length):
            num = uniform(low=self.min, high=self.max,
                          size=self.kromozom_length)
            population.append(num)
        return population

    def GetAffinity(self, population: list):
        populationAffinity = []
        for kromozom in population:
            affinity = self.Affinity(kromozom=kromozom)
            populationAffinity.append([kromozom, affinity])
        #  print(populationAffinity)

        return populationAffinity

    def Affinity(self, kromozom):
        # print('kromozom  === ', kromozom)
        if len(kromozom) == 2:
            return np.sum(np.power(kromozom[0], 2))
        return np.sum(np.power(kromozom, 2))

    def SetTheBestAffinity(self, population: list):
        self.best_affinity_it.append(population[:5])

    def Clone(self, krmozom):
        clones = []
        clone_num = int(self.clone_rate / krmozom[1])
        # print(clone_num)
        for item in range(clone_num):
            clones.append([krmozom[0], krmozom[1]])
        return clones

    def MakeClone(self, population_select: list):
        popualtion_clones = []
        for item in population_select:
            getClone = self.Clone(krmozom=item)
            # print(getClone)
            popualtion_clones.extend(getClone)
        #  print(popualtion_clones)
        return popualtion_clones

    def Hypermutate(self, krmozom):
        if uniform() <= krmozom[1] / (self.mutation_rate * 100):
            ind_tmp = []
            for gen in krmozom[0]:
                if uniform() <= krmozom[1] / (self.mutation_rate * 100):
                    ind_tmp.append(uniform(low=self.min, high=self.max))
                else:
                    ind_tmp.append(gen)

            return (ind_tmp, self.Affinity(ind_tmp))
        else:
            return (krmozom)

    def MakeMutation(self, popualtion_clones: list):
        self.writeToFile(popualtion_clones, "popualtion_clones")
        hypermutate_popullation = []
        for krmozom in popualtion_clones:
            ind_tmp = self.Hypermutate(krmozom=krmozom)
            hypermutate_popullation.append(ind_tmp)
        # print(hypermutate_popullation)
        return hypermutate_popullation

    def select(self, population: list, hypermutate_population: list):
        # Ex:  population length  = 50 , population_clones length = 20 ==> new populatin length = 70
        population = population + hypermutate_population
        # print(population)
        population = sorted(population, key=lambda x: x[1])[
            :self.population_length]
        # print(population)
        return population

    def Run(self):
        self.population = ybs.CreatePopulation()
        self.writeToFile(self.population, 'population')

        for item in tqdm(range(self.itirations)):

            populationAffinity = self.GetAffinity(population=self.population)

            # Sorted population by affinity results
            populationAffinity = sorted(populationAffinity, key=lambda x: x[1])
            # print(populationAffinity)

            # Get the besst affinity
            self.SetTheBestAffinity(populationAffinity)

            # Select kromozom for training
            population_select = populationAffinity[:self.selection_size]
            # print(population_select)

            # Make Clone
            popualtion_clones = self.MakeClone(
                population_select=population_select)

            # Make mutation
            hypermutate_population = self.MakeMutation(
                popualtion_clones=popualtion_clones)

            # Select the best from poulation and
            self.population = self.select(
                population=self.population, hypermutate_population=hypermutate_population)

            pop = []
            for item in self.population:
                if len(item) == 2:
                    pop.append(item[0])
                else:
                    pop.append(item)

            self.population = pop
            # self.population = [p_i for p_i in ]
            self.writeToFile(self.population, 'population')
            # print(len(self.population))

    def ShowChart(self):
        bests_mean = []
        iterations = [i for i in range(self.itirations)]

        for pop_it in self.best_affinity_it:
            bests_mean.append(np.mean([p_i[1] for p_i in pop_it]))

        x = iterations
        y = bests_mean
        # Create two new figures.
        fig1 = plt.figure()
        # # Add a subplot to each figure.
        ax1 = fig1.add_subplot(111)
        # # Plot the data in each subplot.
        ax1.plot(x, y, 'b-')
        # Set the labels and titles for each chart.
        ax1.set_xlabel('itirasyon')
        ax1.set_ylabel('Affinity Ortalaması')
        ax1.set_title('En İyi 5 kromozomlarin Ortalaması')
        plt.legend(loc='upper right')
        # # Save the figures.
        fig1.savefig('Affinity.png')
        plt.show()

# ====================================================================================================
# ====================================================================================================
# ====================================================================================================
# ====================================================================================================
# ====================================================================================================
# ====================================================================================================


ybs = YBS(itirations=100)
ybs.Run()
ybs.ShowChart()
