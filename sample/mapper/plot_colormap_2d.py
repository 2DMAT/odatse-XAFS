import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.ticker as mticker

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", default=None)
args = parser.parse_args()

def load_colormap(filename):
    data = np.loadtxt(filename, unpack=True)
    return data

data = load_colormap("output/ColorMap.txt")

x = data[0]
y = data[1]
f = data[2]

fig = plt.figure()
ax = fig.add_subplot()

plt.scatter(x, y, c=f, s=50, cmap="Blues_r", alpha=1.0, zorder=1.0, norm=colors.SymLogNorm(linthresh=0.5, vmin=0.5, vmax=5))
#plt.scatter(x, y, c=f, s=50, cmap="Blues_r", alpha=1.0, zorder=1.0, norm=colors.Normalize(vmin=0, vmax=2))

ax.set_aspect("equal", adjustable="box")

plt.xlabel("x")
plt.ylabel("y")
plt.colorbar(ticks = mticker.LogLocator(subs="auto"))

if args.output:
    plt.savefig(args.output)
else:
    plt.show()
