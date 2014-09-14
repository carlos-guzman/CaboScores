import matplotlib.pyplot as plt

plt.figure(1)

plt.ylabel('points')
plt.xlabel('turn')

plt.axhline(color='black')

plt.title('Cabo performances')

names = raw_input("Please enter the names of the players\n").split(" ")
all_names = ""
scores = []
turn = 1

# Set up the scoring system
for n in range(len(names)):
    names[n] = names[n].capitalize()
    all_names += names[n]+", "
    scores.append([0])
all_names = all_names[:-2]

colors = ['r', 'g', 'b', 'm', 'y', 'k', 'w']


# while(for i in scores: i[-1]<=100):
#     current = raw_input(all_names)

for i in range(len(names)):
    plt.plot(range(turn), scores[i], colors[i]+'D-', label=names[i])

# plt.plot(xrange(11), [0, 4, 9, 8, 12, 23, 23, 41, 41, 40, 39], 'bD-', label='Carlos')
# plt.plot(xrange(11), [0, -1, 0, 9, 9, 30, 51, 56, 62, 69, 81], 'gD-', label='Emma')
# plt.plot(xrange(11), [0, 6, 36, 0, 4, 4, 11, 11, 17, 23, 28], 'rD-', label='Natalie')

plt.ylim(-5, 100)

plt.legend(loc=0)

plt.show()