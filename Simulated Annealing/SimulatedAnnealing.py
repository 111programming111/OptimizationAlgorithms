
import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt  # to plot
import numpy.random as rn
import seaborn as sns
import matplotlib as mpl

sns.set(context="talk", style="darkgrid", palette="hls",
        font="sans-serif", font_scale=1.05)

FIGSIZE = (19, 8)  #: Figure size, in inches!
mpl.rcParams['figure.figsize'] = FIGSIZE


class SimulatedAnnealing:
    def __init__(self):
        self.interval = (-10, 10)
        self.states = []
        self.costs = []
        self.T = 100
        self.itirasyon = 100
        self.state = 10  # baslangic noktasi

    def Run(self):
        while self.T > 1:
            for item in range(self.itirasyon):
                fraction = item / float(self.itirasyon)
                # self.T = self.Temperature(temp=self.T)
                new_state = self.Random_neighbour(
                    x=self.state, fraction=fraction)
                self.state = self.Acceptance_probability(
                    state=self.state, new_state=new_state, temperature=self.T)
                self.states.append(self.state)
            self.T = self.Temperature(temp=self.T)
            self.costs.append(self.T)

        self.Show_Chart(costs=self.costs, states=self.states)

    #  Random başlangıç değeri almak için
    def random_start(self):
        a, b = self.interval
        return a + (b - a) * rn.random_sample()

    # Sıcaklık değeri azaltmak için
    def Temperature(self, temp):
        return temp * rn.random_sample()

    # Komşu çözümü bulmak için 2.metot
    def Random_neighbour2(self, i: int):
        return 4 * rn.random() - 2 + i

    # Komşu çözümü bulmak için 2. metot
    def Random_neighbour(self, x, fraction=1):
        """Move a little bit x, from the left or the right."""
        amplitude = (max(self.interval) - min(self.interval)) * fraction / 10
        delta = (-amplitude/2.) + amplitude * rn.random_sample()
        return self.Clip(x + delta)

    # Komşu çözümü bulurken değerleri sınırlandırması
    def Clip(self, x):
        """ Force x to be in the interval."""
        a, b = self.interval
        return max(min(x, b), a)

    # Kabul Olasılığı
    def Acceptance_probability(self, state, new_state, temperature):
        cost = self.Cost_function(state)
        new_cost = self.Cost_function(new_state)
        dalta = new_cost - cost
        if (dalta <= 0):  # 1
            state = new_state
        else:
            r = rn.random()
            accpet = np.exp(dalta / temperature)
            if (r < 1/accpet):  # 2
                state = new_state
            else:
                if self.Cost_function(new_state) < self.Cost_function(state):  # 3
                    state = new_state
        return state

    # Uygunluk fonksiyonu
    def Cost_function(self, x):
        if (x <= 5):
            return self.F1(x)
        else:
            return self.F2(x)

    def F2(self, x):  # x <= 1
        return (x-3)**2

    def F1(self, x):  # x > 1
        return x**2

    #  Graf çizme
    def Show_Chart(self, states, costs):
        plt.figure()
        plt.suptitle("Simüle edilmiş tavlamanın durumları ve maliyetleri")
        plt.subplot(121)
        plt.plot(states, 'r')
        plt.title("States " + str(states[-1]))
        plt.subplot(122)
        plt.plot(costs, 'b')
        plt.title("Costs " + str(costs[-1]))
        plt.show()

# ====================================================================================================
# ====================================================================================================
# ====================================================================================================
# ====================================================================================================
# ====================================================================================================
# ====================================================================================================

sA = SimulatedAnnealing().Run()
