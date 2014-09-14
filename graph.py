
plot = True if raw_input("Do you want to plot a graph?(y/n)").lower()=='y' else False

if plot:
    import matplotlib.pyplot as plt

    plt.figure(1)

    plt.ylabel('points')
    plt.xlabel('turn')

    plt.axhline(color='black')

    plt.title('Cabo performances')


names = raw_input("Please enter the names of the players\n").split(" ")
scores, fifty, color, finished = {}, {}, {}, {}
turn = 1

# Set up the scoring system
i=0
colors = ['r', 'g', 'b', 'm', 'y', 'k', 'w', 'c']
for name in names:
    names[names.index(name)] = name.capitalize()
    scores[name.capitalize()]=[0]
    fifty[name.capitalize()] = False
    color[name.capitalize()] = colors[i]
    i+=1
del colors
del names

while(len(scores) != 1):
    print scores
    turnstring = "\n\nTurn " + str(turn) + "  ("
    for name, score in scores.iteritems():
        turnstring +=  name[:2] + ": " + str(score[-1]) + "  "
    print turnstring[:-2]+ ")\n"
    
    del turnstring
    for name in scores.keys():
        new_score = -3
        while new_score < -2:
            new_score = int(raw_input("Please enter the score of "+name+"\n"))
        scores[name].append(scores[name][-1]+new_score)

        del new_score

        if not fifty[name] and (scores[name][-1]==50 or scores[name][-1]==100):
            scores[name][-1] -= 50
            fifty[name] = True
    
    if plot:

        for name, score in scores.iteritems():
            plt.plot(range(turn+1), score, color[name]+'D-', label=name)

        plt.ylim(min(min(scores.itervalues())), 100)

        plt.legend(loc=0)

        plt.show()

    turn+=1

    loser = ""
    for name, score in scores.iteritems():
        if max(score)>100:
            print "\n%s lost with %d points\n" % (name, max(score))
            finished[name] = scores[name]
            loser = name

    if loser != "":
        del scores[loser]
else:
    print "%s wins with %d points!!\n" % (scores.keys()[0], scores.values()[0][-1])
    finished[scores.keys()[0]] = scores.values()[0]
    del scores

if raw_input("Do you want to save the scores?(y/n)\n").lower()=="y":
    import os.path
    filename = raw_input("Enter the file name:\n")
    filename = "cabo" if filename=="" else filename
    i = 0
    while os.path.isfile(filename):
        filename += "(%d)" % i
        i+=1
    out = open(filename, "w")

    for name, score in finished.iteritems():
        out.write("'%s': %s\n" % (name, str(score)))
    out.close()


# plt.plot(xrange(11), [0, 4, 9, 8, 12, 23, 23, 41, 41, 40, 39], 'bD-', label='Carlos')
# plt.plot(xrange(11), [0, -1, 0, 9, 9, 30, 51, 56, 62, 69, 81], 'gD-', label='Emma')
# plt.plot(xrange(11), [0, 6, 36, 0, 4, 4, 11, 11, 17, 23, 28], 'rD-', label='Natalie')
