import numpy as np
import matplotlib.pyplot as plt

#G2
list1 = [3.456560798,2.725605233,3.338530385,3.491016428,2.025135173,5.796021613,4.440392342,5.621812521,3.638393266,5.350184531]
#G3
list2 = [2.215607103,3.550987074,2.922748378,3.45003419,2.604943915,2.43711697,3.518269054,2.529751657,5.255892334,4.362922878]

def scatterLists(l1, l2):
    np1 = np.array(l1)
    np2 = np.array(l2)

    fig, ax = plt.subplots()
    ax.scatter(np1, np2)

    plt.show()

'''UNCOMMENT BELOW CODE TO DISPLAY SCATTERPLOT OF SAMPLE LISTS'''
scatterLists(list1, list2)


