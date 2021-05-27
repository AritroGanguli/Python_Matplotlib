import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def generate_figure():
    t = np.arange(0.0, 5.0, 0.01)
    s1 = np.sin(2*np.pi*t)
    s2 = np.sin(4*np.pi*t)

    fig = plt.figure(figsize=(10,8))

    axes1 = plt.subplot(2, 1, 1, title='Sin(2*pi*x)')
    axes1.plot(t,s1)
    axes2 = plt.subplot(2, 1, 2, title='Sin(4*pi*x)', sharex=axes1, sharey=axes1)
    axes2.plot(t,s2)
    plt.savefig('figure.png')

if __name__ == '__main__':
  generate_figure()
