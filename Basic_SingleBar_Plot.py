import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def Sbarplot_of_iris_sepal_length():
  fig = plt.figure(figsize=(8,6))
  ax = fig.add_subplot(111)
  species = ['setosa', 'versicolor', 'viriginica']
  index = [0.2, 1.2, 2.2]
  sepal_len = [5.01, 5.94, 6.59]
  ax.set(title='Mean Sepal Length of Iris Species',
        xlabel='Species', ylabel='Sepal Length (cm)',
        xlim=(0, 3), ylim=(0, 7))
  ax.bar(index, sepal_len, color='red', width=0.5, edgecolor='black')
  ax.set_xticks([0.45, 1.45, 2.45])
  ax.set_xticklabels(species)
  plt.savefig('bar_iris_sepal.png')

if __name__ == '__main__':
  Sbarplot_of_iris_sepal_length()
