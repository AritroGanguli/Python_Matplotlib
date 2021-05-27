import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def hist_plot_of_normal_distribution():
  np.random.seed(100)
  x1 = 25 + 3.0*np.random.randn(1000)

  fig = plt.figure(figsize=(8,6))
  ax = fig.add_subplot(111)
  ax.set(title="Histogram of a Single Dataset",
        ylabel='Bin Count', xlabel='X1')
  ax.hist(x1, bins=30)
  plt.savefig('histogram_norma.png')

if __name__ == '__main__':
  hist_plot_of_normal_distribution()
