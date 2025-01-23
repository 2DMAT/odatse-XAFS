import numpy as np
import matplotlib.pyplot as plt
import argparse

def load_data(filenames, xcol=0, ycol=1, **kwopts):
    xs = []
    ys = []
    for filename in filenames:
        data = np.loadtxt(filename, unpack=True, **kwopts)
        xs += list(data[xcol])
        ys += list(data[ycol])
    return np.array(xs), np.array(ys)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--xcol", type=int, default=0)
    parser.add_argument("--ycol", type=int, default=1)
    parser.add_argument("-o", "--output", default=None)
    parser.add_argument("--format", default="-o")
    parser.add_argument("--skip", type=int, default=0)
    parser.add_argument("inputfiles", nargs="+")
    args = parser.parse_args()

    xs, ys = load_data(args.inputfiles, xcol=args.xcol, ycol=args.ycol)

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    #ax.set_aspect("equal", adjustable="box")
    ax.plot(xs[args.skip : -1], ys[args.skip : -1], args.format)
    ax.set_xlabel("k")
    ax.set_ylabel("$\chi(k)$")
    if args.output:
        plt.savefig(args.output)
    else:
        plt.show()
