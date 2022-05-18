import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# sns.set(rc={'figure.fgsize':(8, 8)})
# sns.lineplot(x=[1,2,3,4], y=[1,4,9,16],
#              label='linia nr1', color='red',
#              marker='o', linestyle=':')
# sns.lineplot(x=[1,2,3,4], y=[2,5,10,17],
#              label='linia nr2',color='green',
#              marker='^', linestyle=':')
# plt.xlabel('oś x')
# plt.ylabel('oś y')
# plt.title('Wykres liniowy')
# plt.show()


# s = pd.Series(np.random.randn(1000))
# s = s.cumsum()
# sns.set()
# wykres = sns.replot(kind='line',data=s, label='linia')
# wykres.fig.set_size_inches(8,6)
# wykres.fig.suptitle('Wykres liniowy losowych danych')
# wykres.set_xlabels('indeksy')
# wykres.set_ylabels('wartości')
# wykres.add_legend()
# wykres.fgure.subplots_adjust(left=0.1,right=0.9,
#                              bottom=0.1, top=0.9)

# sns.set()
# df = pd.read_csv('iris.csv', header=0,sep=',',decimal='.')
# print(df)
# wykres = sns.lineplot(data=df, x=df.index, y='sepal length',
#                       hue='class', palette=['red','green', 'bule'])
# wykres.set_xlabel('indeksy')
# wykres.set_tittle('Wykres liniowy funkcji liowych')
# wykres.legend(title='Rodzaj kwiatu')
# plt.show()

#wykres punktowy

sns.set()
data = {'a': np.arange(10),
        'c': np.random.randn(0,50,10),
        'd': np.random.randn(10)}
data['b'] = data['a']+10*np.random.randn(10)
data['d'] = np.abs(data['d'])*100
print(data['c'])
print(data['d'])
df = pd.DataFrame(data)
plot = sns.relplot(data = df, x="a", y="b",
                   hue="c", palette='bright', size="d", legend=True)
plot.fig.set_size_inches(6,6)
plot.set(xticks=data['a'])
plt.show()
