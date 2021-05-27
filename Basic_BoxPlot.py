import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def boxplot_of_four_normal_distribution():
  np.random.seed(100)
  x1 = 25 + 3.0*np.random.randn(1000)
  x2 = 35 + 5.0*np.random.randn(1000)
  x3 = 55 + 10.0*np.random.randn(1000)
  x4 = 45 + 3.0*np.random.randn(1000)
  labels = ['X1', 'X2', 'X3', 'X4']

  fig = plt.figure(figsize=(8,6))
  ax = fig.add_subplot(111)
  ax.set(title="Box plot of Multiple Datasets",
        ylabel='Value', xlabel='Dataset')
  ax.boxplot([x1, x2, x3, x4], labels=labels, notch=True, sym='+', patch_artist=True)
  plt.savefig('box_distribution.png')
  
  if __name__ == '__main__':
    boxplot_of_four_normal_distribution()
