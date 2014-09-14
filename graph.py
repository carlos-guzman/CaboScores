import matplotlib.pyplot as plt

plt.figure(1)

plt.ylabel('points')
plt.xlabel('turn')

plt.axhline(color='black')

plt.title('Cabo performances')

plt.plot(xrange(11), [0, 4, 9, 8, 12, 23, 23, 41, 41, 40, 39], 'bD-', label='Carlos')
plt.plot(xrange(11), [0, -1, 0, 9, 9, 30, 51, 56, 62, 69, 81], 'gD-', label='Emma')
plt.plot(xrange(11), [0, 6, 36, 0, 4, 4, 11, 11, 17, 23, 28], 'rD-', label='Natalie')

plt.ylim(-5, 100)

plt.legend(loc=0)

plt.show()