import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def sine_wave_plot():
  fig = plt.figure(figsize=(12,3))
  ax = fig.add_subplot(111)
  t = np.linspace(0.0, 2.0, 200)
  v = np.sin(2.5*np.pi*t)
  plt.plot(t, v, color='red', label='sin(t)')
  ax.set(title='Sine Wave',
        xlabel='Time (seconds)', ylabel='Voltage (mV)',
        xlim=(0, 2), ylim=(-1, 1))
  ax.set_xticks(np.arange(0,2.2,0.2), minor = False)
  ax.set_yticks(np.arange(-1,2,1), minor = False)
  plt.grid(ls = '--')
  plt.legend()
  plt.savefig('sinewave.png')
  
if __name__ == '__main__':
  sine_wave_plot()
