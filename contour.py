import numpy
import pandas
from matplotlib import pyplot
from matplotlib import ticker

data_file = "contour.csv"
num_contour = 16
pyplot.rcParams["axes.linewidth"] = 1.5
pyplot.rcParams["figure.dpi"] = 100
pyplot.rcParams["figure.figsize"] = (4, 4)
pyplot.rcParams["font.family"] = "serif"
pyplot.rcParams["font.size"] = 16
pyplot.rcParams["xtick.major.width"] = 1.5
pyplot.rcParams["ytick.major.width"] = 1.5
pyplot.rcParams["xtick.minor.width"] = 1.5
pyplot.rcParams["ytick.minor.width"] = 1.5
pyplot.rcParams["xtick.major.size"] = 6
pyplot.rcParams["ytick.major.size"] = 6
pyplot.rcParams["xtick.minor.size"] = 3
pyplot.rcParams["ytick.minor.size"] = 3
pyplot.rcParams["axes.labelpad"] = 15
pyplot.rcParams["xtick.major.pad"] = 18
pyplot.rcParams["ytick.major.pad"] = 18
pyplot.rcParams["xtick.top"] = True
pyplot.rcParams["ytick.right"] = True
pyplot.rcParams["xtick.direction"] = "in"
pyplot.rcParams["ytick.direction"] = "in"

data = pandas.read_csv(data_file, header=0, index_col=0)
x = data.columns[0:].astype(float)
y = data.index[0:].astype(float)
z = data.values
zmax = numpy.absolute(z).max()

fig = pyplot.figure()
ax = fig.add_subplot(1, 1, 1)
ax.contour(x, y, z, num_contour, cmap="bwr", vmin=-1 * zmax, vmax=zmax)

ax.set_xlim(1200, 1000)
ax.set_xticks(numpy.arange(1200, 1000 - 1, -50))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))

ax.set_ylim(1200, 1000)
ax.set_yticks(numpy.arange(1200, 1000 - 1, -50))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))

ax.set_title("Synchronous")
ax.set_xlabel(r"$\nu$${_{1}}$ / cm${^{-1}}$")
ax.set_ylabel(r"$\nu$${_{2}}$ / cm${^{-1}}$")

pyplot.savefig("contour.png", dpi=200, bbox_inches="tight")

fig = pyplot.figure()
ax = fig.add_subplot(1, 1, 1)
ax.contour(x, y, z, num_contour, cmap="bwr", vmin=-1 * zmax, vmax=zmax)

fig = pyplot.figure()
ax = fig.add_subplot(1, 1, 1)
ax.pcolormesh(x, y, z, cmap="bwr", vmin=-1 * zmax, vmax=zmax)

fig = pyplot.figure()
ax = fig.add_subplot(1, 1, 1)
ax.contour(x, y, z, num_contour, colors="black", linewidths=0.5, linestyles="solid", vmin=-1 * zmax, vmax=zmax)
ax.pcolormesh(x, y, z, cmap="jet", vmin=-1 * zmax, vmax=zmax)

fig = pyplot.figure()
ax = fig.add_subplot(1, 1, 1)
ax.contour(x, y, z, num_contour, colors="black", linewidths=0.5, vmin=-1 * zmax, vmax=zmax)
ax.contourf(x, y, z, levels=0, colors=["gray", "white"], vmin=-1 * zmax, vmax=zmax)
