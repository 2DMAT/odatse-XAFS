import numpy as np
from numpy.random import Generator, MT19937

rng = Generator(MT19937(12345))

labels = [
    ("c(k)_E[001]", "e(k)_E[001]"),
    ("c(k)_E[1-10]", "e(k)_E[1-10]"),
    ("c(k)_E[110]", "e(k)_E[110]"),
]
npol = len(labels)

nsample=10


kk = []
chik = []
errk = []

for idx in range(npol):
    fname = "output/0/Log00000000_00000000/call_{:02d}/chi.dat".format(idx+1)
    print(idx, fname)

    k, chi, mag, th = np.loadtxt(fname, unpack=True)
    m = (k >= 3.5) & (k <= 10.0)

    k = k[m]
    chi = chi[m]
    
    if len(kk) > 0:
        assert np.all(kk[0] == k)

    nitems = len(k)
    x = rng.standard_normal((nsample, nitems))
    y = np.mean(x, axis=0)
    z = np.var(x, axis=0)

    mag = 0.01 / (1 + (k/10)**2)

    kk.append(k)
    chik.append(chi + y * mag)
    errk.append(z * mag)
    
with open("mock_data.txt", "w") as f:
    f.write("  k")
    for idx in range(npol):
        f.write("  {}  {}".format(*labels[idx]))
    f.write("\n\n")

    for k in range(len(kk[0])):
        f.write("{:.2f}".format(kk[0][k]))
        for idx in range(npol):
            f.write("\t{:12.8f}".format(chik[idx][k]))
            f.write("\t{:12.8f}".format(errk[idx][k]))
        f.write("\n")
