import matplotlib.pyplot as plt
import numpy as np

mm = 1 / 25.4
plt.rcParams["font.size"] = 9
plt.rcParams["figure.figsize"] = (86 * mm, 54 * mm)


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
plt.tight_layout()

fig.patch.set_linewidth(0.5)
fig.patch.set_edgecolor("red")

plt.savefig("paper_mod.pdf")
plt.savefig("paper_mod.png")
