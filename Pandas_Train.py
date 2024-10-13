#NumPy (Numerical Python) bilimsel hesaplamaları hızlı bir şekilde yapmamızı sağlayan bir matematik kütüphanesidir.
#Numpy’ın temelini numpy dizileri oluşturur
#Numpy dizileri python listelerine benzer fakat hız ve işlevsellik açısından python listelerinden daha kullanışlıdır.
#Ayrıca python listelerinden farklı olarak Numpy dizileri homojen yapıda olmalıdır yani dizi içindeki tüm elemanlar aynı veri tipinden olmalıdır.

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")



Fiyat = pd.Series([40, 15, 22, 35, 78,54], 
    index=['Dubai Çikolatası', 'Soda', 'Bisküvi', 'Cips','Alman Çikolatası','Polonya Çikolatası'])

#print(Fiyat)



#print(Fiyat[[name.endswith("Çikolatası") for name in Fiyat.index]])
#print([name.endswith("Çikolatası") for name in Fiyat.index])

#print(Fiyat[4])

#Fiyat.index.name = "Ürünler"
#Fiyat.name = "Fiyatlar"
#print(Fiyat) 


#print(Fiyat[Fiyat<20])

data = pd.DataFrame({'value':[632, 1638, 569, 115, 433, 1130, 754, 555],
                     'patient':[1, 1, 1, 1, 2, 2, 2, 2],
                     'phylum':['Firmicutes', 'Proteobacteria', 'Actinobacteria', 
    'Bacteroidetes', 'Firmicutes', 'Proteobacteria', 'Actinobacteria', 'Bacteroidetes']})
#print(data)

#print(data[["patient","phylum","value"]]) Farklı sırada çıktılar.

#data.loc[3] Spesifik satırlara erişmek için .loc kullan

#print(data.shape[0])  Data'nın büyüklüğünü görmek için .shape[0]


#print(data[data['phylum'].apply(lambda x: x.endswith('bacteria')) & data['value'].apply(lambda x: x>1000)]) Nested loop kullanmadan kolayca filtre





































#MicroData = pd.read_csv("C:/Users/bozca/OneDrive/Belgeler/GitHub/ie-421/microbiome.csv", sep=",")


#print(MicroData.head())

