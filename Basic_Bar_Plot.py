#imports
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def barplot_of_iris_measurements():
  #define figure size and plots
  fig = plt.figure(figsize=(8,6))
  ax = fig.add_subplot(111)
  #define data
  sepal_len = [5.01, 5.94, 6.59]
  sepal_wd = [3.42, 2.77, 2.97]
  petal_len = [1.46, 4.26, 5.55]
  petal_wd = [0.24, 1.33, 2.03]
  #define ticks
  species = ['setosa', 'versicolor', 'viriginica']
  species_index1 = [0.7, 1.7, 2.7]
  species_index2 = [0.9, 1.9, 2.9]
  species_index3 = [1.1, 2.1, 3.1]
  species_index4 = [1.3, 2.3, 3.3]
  #set the plot data
  ax.set(title='Mean Measurements of Iris Species',
        xlabel='Species', ylabel='Iris Measurements (cm)',
        xlim=(0.5, 3.7), ylim=(0, 10))
  #define bar styles
  ax.bar(species_index1, sepal_len, color='c', width=0.2, edgecolor='black', label='Sepal Length')
  ax.bar(species_index2, sepal_wd, color='m', width=0.2, edgecolor='black', label='Sepal Width')
  ax.bar(species_index3, petal_len, color='y', width=0.2, edgecolor='black', label='Petal Length')
  ax.bar(species_index4, petal_wd, color='orange', width=0.2, edgecolor='black', label='Petal Width')
  #set tick positions
  ax.set_xticks([1.1, 2.2, 3.1])
  #set user-defined ticks
  ax.set_xticklabels(species)
  #call legend
  plt.legend()
  #plot the chart
  plt.savefig('bar_iris_measure.png')
  
if __name__ == '__main__':
  #call the function
  barplot_of_iris_measurements()
