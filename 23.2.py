import math


def find_farthest_orbit(list_of_orbits):
    area = list()
    area = [math.pi*list_of_orbits[i][0]*list_of_orbits[i][1] for i in range(len(list_of_orbits))]
    # print(area)
    max_area = max(area)
    max_index = area.index(max_area)
    ellipse = (list_of_orbits[max_index][0], list_of_orbits[max_index][1])
    return ellipse


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))
