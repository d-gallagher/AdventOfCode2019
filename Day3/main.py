# R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83 = 159

# R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
# U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 135

# R8,U5,L5,D3
# U7,R6,D4,L4 = 6


with open("input.txt", "r") as infile:
    instructions = infile.readlines()

wire1 = instructions[0].split(',')
wire2 = instructions[1].split(',')


# take a line of inputs and return dictionary of moves
def parseInstructions(inputs):
    # empty dictionary of moves
    moves_dict = {}
    count = 0
    # x and y are the central port coordinates
    xPos = 0
    yPos = 0
    for input in inputs:
        # grab the direction and distance from the instruction
        direction = input[0]
        distance = input[1:]

        # print(f'{direction} {distance} steps')

        # set move direction in x/y direction
        move_x = move_y = 0
        if direction == "L":
            move_x = -1
        if direction == "R":
            move_x = 1
        if direction == "D":
            move_y = -1
        if direction == "U":
            move_y = 1

        # move in direction for distance
        for _ in range(0, int(distance)):
            xPos += move_x
            yPos += move_y

            count += 1

            # populate the dict with moves
            if (xPos, yPos) not in moves_dict:
                moves_dict[(xPos, yPos)] = count

    # return the dict of moves
    return moves_dict


# get the wires
wire1 = parseInstructions(wire1)
wire2 = parseInstructions(wire2)

# get the intersection between the two dictionaries
# https://stackoverflow.com/questions/18554012/intersecting-two-dictionaries-in-python
wire_intersections = wire1.keys() & wire2.keys()


# for intersection in wire_intersections:
#     print(intersection)


# Get the shortest distance
def get_shortest(collection):
    distances = []
    for intersection in collection:
        dist = abs(intersection[0]) + abs(intersection[1])
        # print(intersection, " : " ,dist)
        distances.append(dist)
    return min(distances)


min = get_shortest(wire_intersections)
print("MIN: ", min)


