import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def multi_curve_plot():
  fig = plt.figure(figsize=(12,3))
  ax = fig.add_subplot(111)
  x = np.linspace(0.0, 5.0, 20)
  y1 = x
  y2 = x**2
  y3 = x**3
  plt.plot(x, y1, color='red', marker='o', label='y = x')
  plt.plot(x, y2, color='green', marker='s', label='y = x**2')
  plt.plot(x, y3, color='blue', marker='^', label='y = x**3')
  ax.set(title='Linear, Quadratic, & Cubic Equations',
        xlabel='X', ylabel='f(X)')
  plt.legend()
  plt.savefig('multicurve.png')

if __name__ == '__main__':
  multi_curve_plot()
