import pandas as pd
import numpy as np

tabela = pd.read_csv("imposto.csv", sep=",")
df = pd.DataFrame(
    {
        
        'Imposto':
         ['imposto 02'],
        'valorTaxa':
        ['Taxa'],
        'ValorTotal':
        ['Total'] 

     print(df.groupby(by=['Imposto 02', 'Taxa'].sum().groupby(level=[0]).cumsum))
    
})

#print(tabela)
#print(tabela["Taxa"] , ["Imposto 02"].sum())
