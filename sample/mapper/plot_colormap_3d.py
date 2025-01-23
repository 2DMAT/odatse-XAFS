import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-z", type=float, default=0.0)
parser.add_argument("-o", "--output", default=None)
args = parser.parse_args()

def load_colormap(filename):
    data = np.loadtxt(filename, unpack=True)
    return data

z = args.z

data = load_colormap("output/ColorMap.txt")
mask = np.isclose(data[2], z)

x = data[0][mask]
y = data[1][mask]
f = data[3][mask]

fig = plt.figure()
ax = fig.add_subplot()

plt.scatter(x, y, c=f, s=50, cmap="Blues_r", alpha=1.0, zorder=1.0, norm=colors.SymLogNorm(linthresh=0.5, vmin=0.1, vmax=10))
#plt.scatter(x, y, c=f, s=50, cmap="Blues_r", alpha=1.0, zorder=1.0, norm=colors.Normalize(vmin=0, vmax=2))

ax.set_aspect("equal", adjustable="box")

plt.xlabel("x")
plt.ylabel("y")
plt.title("z = {:.3f}".format(z))
plt.colorbar()

if args.output:
    plt.savefig(args.output)
else:
    plt.show()
