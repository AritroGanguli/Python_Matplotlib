import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def hbarplot():
  fig = plt.figure(figsize=(12,5))
  ax = fig.add_subplot(111)
  index = [0.2, 1.2, 2.2]
  petal_len = [1.46, 4.26, 5.55]
  species = ['setosa', 'versicolor', 'viriginica']

  ax.set(title='Mean Petal Length of Iris Species',
        xlabel='Species', ylabel='Petal Length (cm)')
  ax.barh(index, petal_len, color='c', height=0.5, edgecolor='black')
  ax.set_xticks([0.45, 1.45, 2.45])
  ax.set_xticklabels(species)
  plt.savefig('hbarplot.png')

if __name__ == '__main__':
  hbarplot()
