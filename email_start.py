import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

url = """C:\\Users\\sa066009\\OneDrive - Saipem\\Mozambico\\20210520_HRS Database_v02_invio 25-05-2021.xlsx"""
df = pd.read_excel(url)

sns.lmplot(x="Sex", y="age @31/12/2021", data=df)

plt.show()