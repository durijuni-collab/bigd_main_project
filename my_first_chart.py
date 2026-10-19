
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

prices = [45500, 40500, 67800, 72400, 71900]

fig, ax = plt.subplots(figsize=(7, 4))

ax.plot(prices, marker="o")

for i, p in enumerate(prices):
    ax.annotate(f"{p:,}", (i, p),
                textcoords="offset points",
                xytext=(0, 8), ha="center")

ax.set_title("5일간 주식 가격 변화")

fig.savefig("my_first_chart.png")
