import numpy as np
import random
import matplotlib.pyplot as plt  # to plot
import seaborn as sns
import matplotlib as mpl

sns.set(context="talk", style="darkgrid", palette="hls", font="sans-serif", font_scale=1.05)

FIGSIZE = (32, 24)  #: Figure size, in inches!
mpl.rcParams['figure.figsize'] = FIGSIZE


class KARINCA_KOLONI_ALGORITMASI:
    def __init__(self, itirasyon=20):
        self.itirasyon = itirasyon
        self.SEHIR_SAYISI = 6
        self.KARINCA_SAYISI = 6
        self.ALPHA = 1
        self.BETA = 1
        self.p = 0.1
        self.uzaklik_matris = [  
                [0, 32, 41, 27, 13, 54],
                [30, 0, 34, 39, 58, 40],
                [32, 59, 0, 14, 24, 46],
                [12, 15, 26, 0, 24,53],
                [46, 39, 22, 35, 0, 33],
                [53, 37, 30, 58, 11, 0]
            ]
        
    def Run(self):
        n_i_j = self.build_n_i_j(self.uzaklik_matris,self.SEHIR_SAYISI)
 
        fermons = self.GetFermonMatris(self.SEHIR_SAYISI)
        karinca_1 = []
        karinca_2 = []
        karinca_3 = []
        karinca_4 = []
        karinca_5 = []
        karinca_6 = []
        seyhatRotasi = self.SeyhatRotalarOlustur(uzaklik_matris=self.uzaklik_matris, KARINCA_SAYISI=self.KARINCA_SAYISI)
        print(seyhatRotasi)
        test = self.GetRotlarUzunlugu(seyhatRotasi,self.uzaklik_matris)
        karinca_1.append(test[0])
        karinca_2.append(test[1])
        karinca_3.append(test[2])
        karinca_4.append(test[3])
        karinca_5.append(test[4])
        karinca_6.append(test[5])
        print(self.GetRotlarUzunlugu(seyhatRotasi,self.uzaklik_matris))
        for item in range(self.itirasyon):
            
            rotalar_lk = self.GetRotlarUzunlugu(seyhatRotasi,self.uzaklik_matris)
            # print(rotalar_lk)
            herKarincaIcinLokalFeromon = self.HerKarincaIcinLokalFermonDegerleriHesapla(seyhatRotasi,rotalar_lk,self.SEHIR_SAYISI)

            # birinci itirasyon fermon degleri t_i_j
            sehirFermonDegerleri = self.HerSehirIcinlokalFermonHesapla(herKarincaIcinLokalFeromon,self.SEHIR_SAYISI)

            p_i_j = n_i_j * sehirFermonDegerleri
            # print(p_i_j)
            olasilik_deger_matris = self.Get_olasilik_deger_matris(p_i_j,self.SEHIR_SAYISI)

            kumletif_olasilik_deger_matris = self.Get_kumletif_olasilik_deger_matris(olasilik_deger_matris,self.SEHIR_SAYISI)

            # karinica rotalari hesaplmak icin
            reasal_sayi_matrisi = self.Get_reasal_sayi_matrisi(self.SEHIR_SAYISI,self.KARINCA_SAYISI)


            new_seyhatRotasi = self.Get_yeni_karinca_rotalari(seyhatRotasi,kumletif_olasilik_deger_matris,self.SEHIR_SAYISI,self.KARINCA_SAYISI)
            test = self.GetRotlarUzunlugu(new_seyhatRotasi,self.uzaklik_matris)
            if test[0] < rotalar_lk[0]:
                seyhatRotasi[0] = new_seyhatRotasi[0]
            if test[1] < rotalar_lk[1]:
                seyhatRotasi[1] = new_seyhatRotasi[1]
            if test[2] < rotalar_lk[2]:
                seyhatRotasi[2] = new_seyhatRotasi[2]
            if test[3] < rotalar_lk[3]:
                seyhatRotasi[3] = new_seyhatRotasi[3]
            if test[4] < rotalar_lk[4]:
                seyhatRotasi[4] = new_seyhatRotasi[4]
            if test[5] < rotalar_lk[5]:
                seyhatRotasi[5] = new_seyhatRotasi[5]
            test = self.GetRotlarUzunlugu(seyhatRotasi,self.uzaklik_matris)
            karinca_1.append(test[0])
            karinca_2.append(test[1])
            karinca_3.append(test[2])
            karinca_4.append(test[3])
            karinca_5.append(test[4])
            karinca_6.append(test[5])

        self.Show_Chart(karinca_1,karinca_2,karinca_3,karinca_4,karinca_5,karinca_6)
        print(seyhatRotasi)
        print(self.GetRotlarUzunlugu(seyhatRotasi,self.uzaklik_matris))
                
    def GetFermonMatris(self,boyut):
        fermons = np.ones((boyut,boyut))
        for i in range(boyut):
            for j in range(boyut):
                if i == j:
                    fermons[i][j] = 0      
        # print(fermons)
        return fermons
    
    def BaslangicUzaklikMatris(self,boyut):
        matris = np.zeros((boyut,boyut))
        for i in range(boyut):
            for j in range(boyut):
                if i == j:
                    continue
                matris[i][j] = random.randint(10, 100)
        # print(matris)
        return matris


    def build_n_i_j(self,matris, boyut: int):
        n_i_j_Matris = np.zeros((boyut,boyut))
        for i in range(boyut):
            for j in range(boyut):
                if i == j:
                    continue
                n_i_j_Matris[i][j] = round(1 /matris[i][j], 3)
            
        # print(matris)
        return n_i_j_Matris
    
    #  Rekursif metodu
    def GetRandomSehir(self,karincaRotasi):
        randomSehir = random.randint(1,6)
        if randomSehir in karincaRotasi:
            # print("Bu sehir rotada mevcut")
            return self.GetRandomSehir(karincaRotasi)
        else:
            # print("Bu sehir rotada mevcut degil")
            return randomSehir
        
    #  Rekursif metodu
    def GetBaslangicNokta(self,baslangicNoktalar: list):
        randomSehir = random.randint(1,6)
        if randomSehir in baslangicNoktalar:
            # print("Bu sehir başka bir rotada başlangıç noktası olarak mevcut")
            return self.GetBaslangicNokta(baslangicNoktalar)
        else:
            # print("u sehir başka bir rotada başlangıç noktası olarak mevcut degil")
            return randomSehir
        
    def SeyhatRotalarOlustur(self,uzaklik_matris, KARINCA_SAYISI):
        seyhatRota = np.zeros((KARINCA_SAYISI, len(uzaklik_matris)))
        # print(seyhatRota)
        for i in range(len(seyhatRota)):
            for j in range(len(seyhatRota[i])):
                if j == 0:
                    seyhatRota[i][j] = self.GetBaslangicNokta(seyhatRota[:,0])
                else:
                    seyhatRota[i][j] = self.GetRandomSehir(seyhatRota[i])
        # print(seyhatRota)
        return seyhatRota
    
    def GetRotlarUzunlugu(self,seyhatRotasi, uzaklik_matris):
        rotlar_uzunluklari = []
        uz = 0
        for i in range(len(seyhatRotasi)):
            for j in range(len(seyhatRotasi[i])-1):
                satir = int(seyhatRotasi[i][j]-1)
                sutun = int(seyhatRotasi[i][j+1]-1)
                # print(satir)
                # print(sutun)
                uz = uz + uzaklik_matris[satir][sutun]
            rotlar_uzunluklari.append(uz)
            uz = 0

        # print(rotlar_uzunluklari)
        return rotlar_uzunluklari
    
    def HerKarincaIcinLokalFermonDegerleriHesapla(self,seyhatRotasi,rotalar_lk,SEHIR_SAYISI):
        tumSehirleriLokalFeromon = []
        for i in range(len(seyhatRotasi)):
            feromon = np.round(1 / rotalar_lk[i],4) 
            matris = np.zeros((SEHIR_SAYISI,SEHIR_SAYISI))
            for j in range(len(seyhatRotasi[i])-1):
                satir = int(seyhatRotasi[i][j]-1)
                sutun = int(seyhatRotasi[i][j+1]-1)
                matris[satir][sutun] = feromon

            # print(matris)
            tumSehirleriLokalFeromon.append(matris)
        
        return tumSehirleriLokalFeromon
    
    def HerSehirIcinlokalFermonHesapla(self,herKarincaIcinLokalFeromon,SEHIR_SAYISI):
        matris = np.zeros((SEHIR_SAYISI,SEHIR_SAYISI))
        formul = 1 - self.p

        for i in range(len(herKarincaIcinLokalFeromon)):
            matris = matris + herKarincaIcinLokalFeromon[i]
        
        matris = matris + formul
        # print(matris)
        return matris
    
    def Get_olasilik_deger_matris(self,p_i_j,SEHIR_SAYISI):
        matris = np.zeros((SEHIR_SAYISI,SEHIR_SAYISI))
        for i in range(len(p_i_j)):
            satir_toplami = sum(p_i_j[i])
            # print(satir_toplami)
            for j in range(len(p_i_j[i])):
                matris[i][j] = np.round(p_i_j[i][j] / satir_toplami,5) 
        # print(matris)
        return matris
    
    def Get_kumletif_olasilik_deger_matris(self,olasilik_deger_matris,SEHIR_SAYISI):
        matris = np.zeros((SEHIR_SAYISI,SEHIR_SAYISI))
        for i in range(len(olasilik_deger_matris)):
            matris[i][0] = olasilik_deger_matris[i][0]
            for j in range(len(olasilik_deger_matris[i])-1):
                prevalue = matris[i][j]
                matris[i][j+1] = olasilik_deger_matris[i][j+1] + prevalue

        # print(matris)
        return matris
    
    def Get_reasal_sayi_matrisi(self,SEHIR_SAYISI,KARINCA_SAYISI):
        matris = np.zeros((KARINCA_SAYISI,10))
        for i in range(len(matris)):
            for j in range(10):
                matris[i][j] = random.random()
        # print(matris)
        return matris
    
    def Get_yeni_karinca_rotalari(self,eski_seyhatRotasi,kumletif_olasilik_deger_matris,SEHIR_SAYISI,KARINCA_SAYISI):
        rotalar = np.zeros((KARINCA_SAYISI,SEHIR_SAYISI))
        for i in range(len(eski_seyhatRotasi)):
            rotalar[i][0] = eski_seyhatRotasi[i][0]

        for i in range(len(rotalar)):
            for j in range(len(rotalar[i])-1):
                sehir = int(rotalar[i][j])
                nextSehir = self.GetSonrakiSehir(sehir,kumletif_olasilik_deger_matris,rotalar[i],j+1)
                rotalar[i][j+1]  = nextSehir
                # print(rotalar)
        
        return rotalar
    
    def getMissingCity(self,rota):
        for item in range(6):
            if item+1 in rota:
                continue
            else:
                return item+1 
            
    def GetSonrakiSehir(self,sehir,kumletif_olasilik_deger_matris,sehir_rotasi,currentIndex):
        if currentIndex  == 5 or currentIndex == 4:
            return self.getMissingCity(sehir_rotasi)
        index = sehir
        while index in sehir_rotasi or index == None:
            rasal_sayi = random.random()
            index = self.Get_index_from_kumletif_list(rasal_sayi,kumletif_olasilik_deger_matris[sehir-1])

        return index
    
    def Get_index_from_kumletif_list(self,rasal_sayi, kumletif_olasilik_deger_liste):
        for i in range(len(kumletif_olasilik_deger_liste)-1):
            if rasal_sayi >= kumletif_olasilik_deger_liste[i] and rasal_sayi < kumletif_olasilik_deger_liste[i+1]:
                return i+1
            
    
    def Show_Chart(self,karinca1, karinca2,karinca3,karinca4,karinca5,karinca6):
    
        fig, axes = plt.subplots(3, 2, figsize=(25, 16))  # 2x2 alt grafik alanı oluşturur
        fig.suptitle("Simüle edilmiş")  # Ana başlık

        # Alt grafiklere çizim
        axes[0, 0].plot(karinca1, 'r')
        axes[0, 0].set_title("karinca 1")
        axes[0, 1].plot(karinca2, 'b')
        axes[0, 1].set_title("karinca 2")
        axes[1, 0].plot(karinca3, 'g')
        axes[1, 0].set_title("karinca 3")
        axes[1, 1].plot(karinca4, 'y')
        axes[1, 1].set_title("karinca 4")
        axes[2, 0].plot(karinca5, 'b')
        axes[2, 0].set_title("karinca 5")
        axes[2, 1].plot(karinca6, 'y')
        axes[2, 1].set_title("karinca 6")

        plt.tight_layout()  # Öğeler arasında boşluk ayarlar
        plt.show()

# ====================================================================================================
# ====================================================================================================
# ====================================================================================================
# ====================================================================================================
# ====================================================================================================
# ====================================================================================================

KKA = KARINCA_KOLONI_ALGORITMASI(itirasyon=1000)

KKA.Run()
