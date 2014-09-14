
plot = True if raw_input("Do you want to plot?(y/n)").lower()=='y' else False

if plot:
    import matplotlib.pyplot as plt

    plt.figure(1)

    plt.ylabel('points')
    plt.xlabel('turn')

    plt.axhline(color='black')

    plt.title('Cabo performances')


names = raw_input("Please enter the names of the players\n").split(" ")
scores, fifty = {}, {}
turn = 1

# Set up the scoring system
for name in names:
    names[names.index(name)] = name.capitalize()
    scores[name.capitalize()]=[0]
    fifty[name.capitalize()] = False

colors = ['r', 'g', 'b', 'm', 'y', 'k', 'w']


over = False
while(not over):
    print "\nTurn ", turn, "\n"
    for name in names:
        scores[name].append(
            scores[name][-1]+
            int(raw_input("Please enter the score of "+name+"\n")))

        if not fifty[name] and (scores[name][-1]==50 or scores[name][-1]==100):
            scores[name][-1] -= 50
            fifty[name] = True
    
    if plot:
        i=0
        for name, score in scores.iteritems():
            plt.plot(range(turn+1), score, colors[i]+'D-', label=name)
            i+=1

        plt.ylim(-5, 100)

        plt.legend(loc=0)

        plt.show()
        # raw_input()
        plt.close()

    turn+=1

    # Check whether the game is over
    for score in scores.values(): 
        over = over or score[-1]>100
    



# plt.plot(xrange(11), [0, 4, 9, 8, 12, 23, 23, 41, 41, 40, 39], 'bD-', label='Carlos')
# plt.plot(xrange(11), [0, -1, 0, 9, 9, 30, 51, 56, 62, 69, 81], 'gD-', label='Emma')
# plt.plot(xrange(11), [0, 6, 36, 0, 4, 4, 11, 11, 17, 23, 28], 'rD-', label='Natalie')
