import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def scatter_plot():
  fig = plt.figure(figsize=(12,3))
  ax = fig.add_subplot(111)
  s = [50, 60, 55, 50, 70, 65, 75, 65, 80, 90, 93, 95]
  months = [i for i in range(1, 13)]
  plt.scatter(months, s, color='red')
  ax.set(title="Cars Sold by Company 'X' in 2017",
        xlabel='Months', ylabel='No. of Cars Sold',
        xlim=(0, 13), ylim=(20, 100))
  ax.set_xticks([1,3,5,7,9,11])
  ax.set_xticklabels(['Jan', 'Mar', 'May', 'Jul', 'Sep', 'Nov'])
  plt.savefig('scatter.png')

if __name__ == '__main__':
  scatter_plot()
