import pandas as pd
import matplotlib.pyplot as plt 
try:
    salary = pd.read_csv("../DATASET/gaji.csv")
except:
    url = '/gaji.csv'
    salary = pd.read_csv(url)
df = salary
label = {'S1':'r', 'S2':'g', 'S3':'blue'}
fig, ax = plt.subplots()
plt.xlabel('Pengalaman (tahun)')
plt.ylabel('Gaji ($)')
plt.title('Grafik Gaji berdasarkan Pengalaman dan Pendidikan')
#plt.grid(True)

for key in label:
    X=df[df['Pendidikan']==key]['Pengalaman']
    Y=df[df['Pendidikan']==key]['Gaji']
    ax.scatter(X, Y, c=label[key],label=key, s=100)

ax.legend()
plt.show()