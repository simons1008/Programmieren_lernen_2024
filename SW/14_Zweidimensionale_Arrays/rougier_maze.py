# Nicolas P. Rougier (2017), From Python to Numpy
# https://www.labri.fr/perso/nrougier/from-python-to-numpy/#building-a-maze
# https://en.wikipedia.org/wiki/Maze_generation_algorithm
#
# There exist many maze generation algorithms but I tend to prefer the one I've been using
# for several years but whose origin is unknown to me. I've added the code in the cited
# wikipedia entry. Feel free to complete it if you know the original author. This algorithm
# works by creating n (density) islands of length p (complexity). An island is created by
# choosing a random starting point with odd coordinates, then a random direction is chosen.
# If the cell two steps in a given direction is free, then a wall is added at both one step
# and two steps in this direction. The process is iterated for n steps for this island.
# p islands are created. n and p are expressed as float to adapt them to the size of the
# maze. With a low complexity, islands are very small and the maze is easy to solve. With
# low density, the maze has more "big empty rooms".

import numpy as np
import matplotlib.pyplot as plt


def build_maze(width=65, height=65, complexity=0.75, density=0.50):
    # Only odd shapes
    shape = ((height//2)*2+1, (width//2)*2+1)
    # Adjust complexity and density relatively to maze size
    n_complexity = int(complexity*(shape[0]+shape[1]))
    n_density = int(density*(shape[0]*shape[1]))

    # Build actual maze
    Z = np.zeros(shape, dtype=bool)

    # Fill borders
    Z[0, :] = Z[-1, :] = Z[:, 0] = Z[:, -1] = 1

    # Islands starting point with a bias in favor of border
    P = np.random.normal(0, 0.5, (n_density, 2))
    P = 0.5 - np.maximum(-0.5, np.minimum(P, +0.5))
    P = (P*[shape[1], shape[0]]).astype(int)
    P = 2*(P//2)

    # Create islands
    for i in range(n_density):
        # Test for early stop: if all starting point are busy, this means we
        # won't be able to connect any island, so we stop.
        T = Z[2:-2:2, 2:-2:2]
        if T.sum() == T.size: break
        x, y = P[i]
        Z[y, x] = 1
        for j in range(n_complexity):
            neighbours = []
            if x > 1:          neighbours.append([(y, x-1), (y, x-2)])
            if x < shape[1]-2: neighbours.append([(y, x+1), (y, x+2)])
            if y > 1:          neighbours.append([(y-1, x), (y-2, x)])
            if y < shape[0]-2: neighbours.append([(y+1, x), (y+2, x)])
            if len(neighbours):
                choice = np.random.randint(len(neighbours))
                next_1, next_2 = neighbours[choice]
                if Z[next_2] == 0:
                    Z[next_1] = 1
                    Z[next_2] = 1
                    y, x = next_2
            else:
                break
    return Z


# Irrgarten erzeugen
Z = build_maze()

# Irrgarten in Textdatei schreiben
# List-of-lists in String umwandeln: True -> '+', False -> ' '
my_string = ''
for row in range(len(Z)):
    for val in Z[row]:
        if val:
            my_string += '+'
        else:
            my_string += ' '
    # Umbruch am Ende von row
    my_string += '\n'
# Textdatei schreiben
with open("my_maze.txt", mode = "w") as datei:
    datei.write(my_string)

# Plot by Francisco Gama (2012)
# https://gist.github.com/fcogama/3689650
plt.figure(figsize=(10,5))
plt.imshow(Z,cmap=plt.cm.binary,interpolation='nearest')
plt.xticks([]),plt.yticks([])
plt.show()
