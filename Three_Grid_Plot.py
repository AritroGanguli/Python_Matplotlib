import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

def generate_figure():
    x = np.arange(1, 101)
    y1 = x
    y2 = x**2
    y3 = x**3

    fig = plt.figure(figsize=(8,6))
    g = gridspec.GridSpec(2,2)

    axes1 = plt.subplot(g[0,0], title='y=x')
    axes1.plot(x, y1)
    axes2 = plt.subplot(g[1,0], title='y=x**2')
    axes2.plot(x, y2)
    axes3 = plt.subplot(g[:,1], title='y=x**3')
    axes3.plot(x, y3)

    plt.tight_layout()
    plt.savefig('figure.png')
        
if __name__ == '__main__':
  generate_figure()
