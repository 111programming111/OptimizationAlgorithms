import datetime
import numpy as np
import matplotlib.pyplot  as plt

class PSO():
    def __init__(self,xMin=-10,xMax=+10,parca_sayisi=6,itirasyon=10,c1=2,c2=2):
        self.d = 2
        self.xMin ,self.xMax = xMin , xMax
        self.vMin , self.vMax = 0 , 0.5*(xMax - xMin)
        self.itirasyon = itirasyon
        self.parca_sayisi = parca_sayisi
        self.c1 = c1
        self.c2 = c2
        self.w = 0.729
        self.global_best_X1 = []
        self.global_best_X2 = []
        self.global_fit = []

    def Run(self):
        #parcalarin baslangic noktalar
        self.positions = np.random.uniform(-10, 10, (self.parca_sayisi, self.d)).tolist()
        with open('PSO_Log.txt', 'w') as f:
            f.write("positions")
            f.write('\n')
            f.write(str(self.positions))
            f.write('\n \n')

        # Uygunluk hesaplama
        self.fitness = np.array([self.fun(x1, x2) for x1, x2 in self.positions]).tolist()
        self.writeToFile(self.fitness,"fitness")
        # Hizlar

        self.velocities = np.full((self.parca_sayisi, self.d),0.5).tolist()
        self.writeToFile(self.velocities,"velocities")

        # Parcalarin en iyi pozisyonu 
        self.best_positions = self.positions
        self.writeToFile(self.best_positions,"best_positions")

        # En iyi amac fun degerleri
        self.best_fitness = self.fitness
        self.writeToFile(self.best_fitness,"best_fitness")

        # En iyi amac degeri
        self.global_best_fitnes= min(self.fitness)
        self.writeToFile(self.global_best_fitnes,"global_best_fitness")
        self.global_fit.append(self.global_best_fitnes)

        # En iyi amac degerin pozisyonlarin index i
        index = self.fitness.index(self.global_best_fitnes)
        self.writeToFile(index,"index")

        # En iyi amac degerin pozisyonlari
        self.global_best_posation = self.best_positions[index]
        self.global_best_X1.append(self.global_best_posation[0])
        self.global_best_X2.append(self.global_best_posation[1])
        self.writeToFile(self.global_best_posation,"global_best_posation")

        for item in range(self.itirasyon):
            self.writeToFile("========"+str(item)+"========","itertion")
            self.HizGuncelleme(self.velocities)

        self.writeToFile(self.global_best_fitnes,"global_best_fitnes") 
        self.writeToFile(self.global_best_X1,"global_best_X1")
        self.writeToFile(self.global_best_X2,"global_best_X2")
        self.ShowChart(self.global_best_X1,self.global_best_X2,self.global_fit)

    def writeToFile(self,data,title):
        with open('PSO_Log.txt', 'a') as f:
            f.write(title)
            f.write('\n')
            f.write(str(datetime.datetime.now())+"  ")
            f.write(str(data))
            f.write('\n \n')

    def fun(self,x1, x2):
        z= (4*x1**2) - (2.1*x1**4)+ ((1/3)*x1**6) + x1*x2 - (4*x2**2) + (4*x2**4)
        return z

    def LsimitV(self,V):
        if(V > self.vMax):
            V = self.vMax
        if (V < self.vMin):
            V = self.vMin
        return V
    
    def LsimitX(self,X):
        if(X > self.xMax):
            X = self.xMax
        if (X < self.xMin):
            X = self.xMin
        return X
    
    def HizGuncelleme(self,velocities):
        for i in range(self.parca_sayisi):
            for j in range(self.d):
                velocities[i][j] = (self.w * velocities[i][j]
                                                    + self.c1 * np.random.rand() * (self.best_positions[i][j] - self.positions[i][j])
                                                    + self.c2 * np.random.rand() * (self.global_best_posation[j]- self.positions[i][j])
                                                    )
                velocities[i][j]= self.LsimitV(velocities[i][j])
                self.positions[i][j] = self.positions[i][j] + velocities[i][j]
                self.positions[i][j] = self.LsimitX(self.positions[i][j])
            newF = self.fun(self.positions[i][0],self.positions[i][1])
            if newF < self.best_fitness[i]:
                self.best_fitness[i] = newF
                self.best_positions[i][0] = self.positions[i][0]
                self.best_positions[i][1] = self.positions[i][1]
                if newF < self.global_best_fitnes:
                    self.global_best_fitnes = self.best_fitness[i]
                    self.global_best_posation[0] = self.positions[i][0]   
                    self.global_best_posation[1] = self.positions[i][1]


        self.global_fit.append(self.global_best_fitnes)
        self.global_best_X1.append(self.global_best_posation[0])
        self.global_best_X2.append(self.global_best_posation[1])
        self.writeToFile(self.velocities,"new velocities")
        self.writeToFile(self.positions, "new positions")
        self.writeToFile(self.best_positions, "new best_positions")
        self.writeToFile(self.global_best_posation, "new global_best_posation")   

    def ShowChart(self,X1,X2,global_fit):
        x = range(0, self.itirasyon+1)
        y1 = X1
        y2 = X2
        y3 = global_fit

        fig1 = plt.figure()
        fig2 = plt.figure()
        fig3 = plt.figure()

        ax1 = fig1.add_subplot(111)
        ax2 = fig2.add_subplot(111)
        ax3 = fig3.add_subplot(111)

        ax1.plot(x, y1, 'b-')
        ax2.plot(x, y2, 'r-')
        ax3.plot(x, y3, 'b-')

        ax1.set_xlabel('itirasyon')
        ax1.set_ylabel('X1')
        ax1.set_title('Max X1  değeri')
        plt.legend(loc='upper right')


        ax2.set_xlabel('itirasyon')
        ax2.set_ylabel('X2')
        ax2.set_title('Max X2 değeri')
        plt.legend(loc='upper right')


        ax3.set_xlabel('itirasyon')
        ax3.set_ylabel('uygunluk deger')
        ax3.set_title('Fonksiyon uygunluk değeri')

        fig1.savefig('X1_degeri.png')
        fig2.savefig('X2_degeri.png')
        fig3.savefig('Fonksiyon_uygunlik_.png')

        plt.figure(figsize=(8, 12))
        plt.subplot(3, 1, 1)
        plt.plot(X1, label='X1 değeri')
        plt.legend(loc='lower right')
        plt.ylabel('X1')
        plt.title('X1 değeri')

        plt.subplot(3, 1, 2)
        plt.plot(X2, label='X2 değeri')
        plt.legend(loc='upper right')
        plt.ylabel('X2')
        plt.title('X2 değeri')

        plt.subplot(3, 1, 3)
        plt.plot(global_fit, label='uygunluk')
        plt.legend(loc='upper right')
        plt.ylabel('uygunluk')
        plt.title('Fonksiyon uygunluk değeri')
        plt.xlabel('Itirasyon')

        plt.savefig('general.png')
        plt.show()


#====================================================================================================
#====================================================================================================
#====================================================================================================
#====================================================================================================
#====================================================================================================
#====================================================================================================

pso = PSO(parca_sayisi=10, itirasyon=5)
pso.Run()
