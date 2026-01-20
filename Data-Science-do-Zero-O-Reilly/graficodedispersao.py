from matplotlib import pyplot as plt

friends=[70, 65, 72, 63, 71, 64]
minutes=[100, 200, 300, 400, 500, 600]
labels=["a", "b", "c", "d", "e", "f"]
plt.scatter(friends, minutes)

for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count),
                 xytext=(5, -5),
                 textcoords='offset points')
plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("Number of Friends")
plt.show()
plt.ylabel("Daily Minutes Spent on the Site")
