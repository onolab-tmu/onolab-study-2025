import matplotlib.pyplot as plt
import numpy as np


def plot_example():
    np.random.seed(100)
    fs = 8000
    sec = 0.2
    freq = 100
    t = np.arange(fs * sec) / fs
    s = np.sin(2 * np.pi * freq * t)
    x = np.random.randn(int(fs * sec))
    x /= np.max(np.abs(x))

    fig = plt.figure()
    plt.plot(t, x, label="White noise")
    plt.plot(t, s, label="Sin wave")

    plt.title("Example")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()

    fig.patch.set_linewidth(0.5)
    fig.patch.set_edgecolor("red")
    return fig


# example 1, default
fig = plot_example()
plt.savefig("example1.pdf", edgecolor=fig.get_edgecolor())
plt.savefig("example1.png", edgecolor=fig.get_edgecolor())
plt.close()

# example 2, large font
plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["font.size"] = 24
fig = plot_example()
plt.savefig("example2.pdf", edgecolor=fig.get_edgecolor())
plt.savefig("example2.png", edgecolor=fig.get_edgecolor())
plt.close()

# example 3, large font with default tight_layout
plt.rcParams["figure.figsize"] = (6.4, 4.8)
fig = plot_example()
plt.tight_layout()
plt.savefig("example3.pdf", edgecolor=fig.get_edgecolor())
plt.savefig("example3.png", edgecolor=fig.get_edgecolor())
plt.close()

# example 4, large font with tuned tight_layout
fig = plot_example()
plt.tight_layout(pad=0.2)
plt.savefig("example4.pdf", edgecolor=fig.get_edgecolor())
plt.savefig("example4.png", edgecolor=fig.get_edgecolor())
plt.close()

# example 5, good example
mm = 1 / 25.4  # mm to inch
figsize = (194.2 * mm, 120 * mm)
plt.rcParams["font.size"] = 28
plt.rcParams["figure.figsize"] = figsize
fig = plot_example()
plt.tight_layout(pad=0.2)
plt.savefig("example5.pdf", edgecolor=fig.get_edgecolor())
plt.savefig("example5.png", edgecolor=fig.get_edgecolor())
plt.close()
