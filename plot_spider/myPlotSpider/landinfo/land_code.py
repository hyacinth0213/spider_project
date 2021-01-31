import numpy as np
import pandas as pd

list_l = [['Baden-Württemberg', 'BW', 'DE-BW'],
          ['Bayern', 'BY', 'DE-BY'],
          ['Berlin', 'BE', 'DE-BE'],
          ['Brandenburg', 'BB', 'DE-BB'],
          ['Bremen', 'HB', 'DE-HB'],
          ['Hamburg', 'HH', 'DE-HH'],
          ['Hessen', 'HE', 'DE-HE'],
          ['Mecklenburg-Vorpommern', 'MV', 'DE-MV'],
          ['Niedersachsen', 'NI', 'DE-NI'],
          ['Nordrhein-Westfalen', 'NW', 'DE-NW'],
          ['Rheinland-Pfalz', 'RP', 'DE-RP'],
          ['Saarland', 'SL', 'DE-SL'],
          ['Sachsen', 'SN', 'DE-SN'],
          ['Sachsen-Anhalt', 'ST', 'DE-ST'],
          ['Schleswig-Holstein', 'SH', 'DE-SH'],
          ['Thüringen', 'TH', 'DE-TH']
          ]

df = pd.DataFrame(list_l, columns=['land', 'code', 'int-code'])
print(df)
"""
df.to_csv("land_code1.csv")
read_csv = pd.read_csv("land_code1.csv")
print(read_csv)
"""
df.to_csv("land_code2.csv", index_label="index_label")
read_csv2 = pd.read_csv("land_code2.csv")
print(read_csv2)



