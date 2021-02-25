def ReadInputFile(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    line = lines[0].rstrip()
    fline = line.split(' ')
    simulation_time = int(fline[0])
    no_of_intersection = int(fline[1])
    no_of_street = int(fline[2])
    no_of_cars = int(fline[3])
    points_destination = int(fline[4])
    list_of_streets = []
    for i in range(1, no_of_street):
        otherLines = lines[i].rstrip().split(' ')
        list_of_streets.append(otherLines)
    list_of_cars = []
    for i in range(no_of_street + 1, len(lines)):
        car = lines[i].rstrip().split(' ')
        list_of_cars.append(car)

    return list_of_streets, list_of_cars


class Street:
    def __init__(self, name, start, end, time):
        self.name = name
        self.start = start
        self.end = end
        self.time = time


class Car:
    def __init__(self, list_of_lists):
        self.number_of_streets = list_of_lists[0]
        self.streets = list_of_lists[1:]


class FinalOutPut:
    def __init__(self, list_of_intersections):
        self.no_of_intersection = len(list_of_intersections)
        self.list_of_intersections = list_of_intersections


def WriteOutputFile(output):
    createText = f"{len(output)}\n"
    for rp in output:
        createText += f"{rp[0]}\n{rp[1]}\n"
        for st in rp[2]:
            createText += f"{st}\n"

    with open("_Output.txt", 'w') as out:
        out.write(createText)


class Intersection:
    def __init__(self, id, strtInvolved):
        self.id = id
        self.strtInvolved = strtInvolved


# streets, cars = ReadInputFile('a.txt')

l = [[1, 2, ['rue-d-athenes 2', 'rue-d-amsterdam 1']], [0, 1, ['rue-de-londres 2']], [2, 1, ['rue-de-moscou 1']]]
WriteOutputFile(l)

"""
def WriteOutputFile(output):
    createText = f"{output.no_of_intersection}\n"
    for rp in output.list_of_intersection:
        createText += f"{rp.id}\n{len(rp.strtInvolved)}\n"
        for st in rp.strtInvolved:
            createText += f"{rp.strtInvolved[0]} {rp.strtInvolved[1]}"

    with open("_Output.txt", 'w') as out:
        out.write(createText)
"""
