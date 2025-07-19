import pandas as pd
import statistics
import numpy as np
from scipy.stats import skew  

datos=[4,7,10,10,5,5,4]

moda1 = statistics.mode(datos)
#print(moda1)

moda2 = statistics.multimode(datos)
#print(moda2)

serie = pd.Series([4,7,10,10,5,5,4])
modapd = serie.mode()
#print(modapd.tolist())

df = pd.DataFrame([4,7,10,10,5,5,4])

rango=serie.max()-serie.min()
#print(rango)

Varianza=df.var()
#print(Varianza)

p50 = serie.quantile(0.50)
#print(p50)

p25 = np.percentile(datos, 25)
#print(p25)

asimetria=skew(datos)
print(asimetria)

asimetria_nosesgada=skew(datos, bias=False)
print(asimetria_nosesgada)

asimetria2=serie.skew()
print(asimetria2)