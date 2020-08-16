#Source vertex (source_x, source_y)
source_x = 2
source_y = 0
#current vertex to update states
current_i = source_x
current_j = source_y
#final goal (goal_x, goaly)
goal_x = 4
goal_y = 5

g = 0
flag = 1
#h(N) = Manhattan Distance
h = [[0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]]
#to check whether block is visited or not
checked = [[0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]]
#obstacles information
obstacle = [[0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0]]
for i in range(0,5):
    for j in range(0,6):
        #Calculating Manhattan Distance
        h[i][j] = abs(i - goal_x) + abs(j - goal_y)


def find_path(i, j):
    global current_i, current_j, goal_x, goal_y, g, h, obstacle,  checked
    right_f = 99999
    left_f = 99999
    up_f = 99999
    down_f = 99999
    above_left_f = 99999
    above_right_f = 99999
    bottom_left_f = 99999
    bottom_right_f = 99999

    #Left vertex from current vertex
    left_i = current_i
    left_j = current_j - 1
    if left_j >= 0: #to ensure that block is in given area...not out of the range of given area
        if obstacle[left_i][left_j] == 0 and checked[left_i][left_j] == 0:
            # f(x) = current(g)+1 + h(x)
            left_f = g + 1 + h[left_i][left_j]

    #Right vertex from current vertex
    right_i = current_i
    right_j = current_j + 1
    if right_j <= 5: #to ensure that block is in given area...not out of the range of given area
        if obstacle[right_i][right_j] == 0 and checked[right_i][right_j] == 0:
            right_f = g + 1 + h[right_i][right_j]

    #Upper vertex from current vertex
    up_i = current_i - 1
    up_j = current_j
    if up_i >= 0: #to ensure that block is in given area...not out of the range of given area
        if obstacle[up_i][up_j] == 0 and checked[up_i][up_j] == 0:
            up_f = g + 1 + h[up_i][up_j]

    #Down vertex from current vertex
    down_i = current_i + 1
    down_j = current_j
    if down_i <= 4: #to ensure that block is in given area...not out of the range of given area
        if obstacle[down_i][down_j] == 0 and checked[down_i][down_j] == 0:
            down_f = g + 1 + h[down_i][down_j]

    #Upper Left Vertex from current vertex
    above_left_i = current_i - 1
    above_left_j = current_j - 1
    if above_left_j >= 0 and above_left_i >= 0:
        if obstacle[above_left_i][above_left_j] == 0 and checked[above_left_i][above_left_j] == 0:
            above_left_f = g + 1 + h[above_left_i][above_left_j]

    #Upper Right Vertex from current vertex
    above_right_i = current_i - 1
    above_right_j = current_j + 1
    if above_right_j <= 5 and above_right_i >= 0:
        if obstacle[above_right_i][above_right_j] == 0 and checked[above_right_i][above_right_j] == 0:
            above_right_f = g + 1 + h[above_right_i][above_right_j]

    #Bottom Left Vertex from current vertex
    bottom_left_i = current_i + 1
    bottom_left_j = current_j - 1
    if bottom_left_j >= 0 and bottom_left_i <= 4:
        if obstacle[bottom_left_i][bottom_left_j] == 0 and checked[bottom_left_i][bottom_left_j] == 0:
            bottom_left_f = g + 1 + h[bottom_left_i][bottom_left_j]

    #Bottom Right Vertex from current vertex
    bottom_right_i = current_i + 1
    bottom_right_j = current_j + 1
    if bottom_right_j <= 5 and bottom_right_i <= 4:
        if obstacle[bottom_right_i][bottom_right_j] == 0 and checked[bottom_right_i][bottom_right_j] == 0:
            bottom_right_f = g + 1 + h[bottom_right_i][bottom_right_j]

    #to find out minimum f(x)
    if right_f <= left_f and right_f <= up_f and right_f <= down_f and right_f <= above_left_f and right_f <= above_right_f and right_f <= bottom_left_f and right_f <= bottom_right_f:
        checked[right_i][right_j] = 1
        current_i = right_i
        current_j = right_j
        g = g + 1
        print("Right (",current_i,",", current_j, ") ")

    elif left_f <= right_f and left_f <= up_f and left_f <= down_f and left_f <= above_left_f and left_f <= above_right_f and left_f <= bottom_left_f and left_f <= bottom_right_f:
        checked[left_i][left_j] = 1
        current_i = left_i
        current_j = left_j
        g = g + 1
        print("Left (",current_i,",", current_j, ") ")

    elif up_f <= left_f and up_f <= right_f and up_f <= down_f and up_f <= above_left_f and up_f <= above_right_f and up_f <= bottom_left_f and up_f <= bottom_right_f:
        checked[up_i][up_j] = 1
        current_i = up_i
        current_j = up_j
        g = g + 1
        print("Up (",current_i,",", current_j, ") ")

    elif down_f < left_f and down_f <= right_f and down_f <= up_f and down_f <= above_left_f and down_f <= above_right_f and down_f <= bottom_left_f and down_f <= bottom_right_f:
        checked[down_i][down_j] = 1
        current_i = down_i
        current_j = down_j
        g = g + 1
        print("Down (",current_i,",", current_j, ")")

    elif above_left_f < left_f and above_left_f <= right_f and above_left_f <= up_f and above_left_f <= down_f and above_left_f <= above_right_f and above_left_f <= bottom_left_f and above_left_f <= bottom_right_f:
        checked[above_left_i][above_left_j] = 1
        current_i = above_left_i
        current_j = above_left_j
        g = g + 1
        print("Above Left (", current_i, ",", current_j, ")")

    elif above_right_f < left_f and above_right_f <= right_f and above_right_f <= up_f and above_right_f <= down_f and above_right_f <= above_left_f and above_right_f <= bottom_left_f and above_right_f <= bottom_right_f:
        checked[above_right_i][above_right_j] = 1
        current_i = above_right_i
        current_j = above_right_j
        g = g + 1
        print("Above Right (", current_i, ",", current_j, ")")

    elif bottom_left_f < left_f and bottom_left_f <= right_f and bottom_left_f <= up_f and bottom_left_f <= down_f and bottom_left_f <= above_right_f and bottom_left_f <= above_left_f and bottom_left_f <= bottom_right_f:
        checked[bottom_left_i][bottom_left_j] = 1
        current_i = bottom_left_i
        current_j = bottom_left_j
        g = g + 1
        print("Bottom Left (", current_i, ",", current_j, ")")

    elif bottom_right_f < left_f and bottom_right_f <= right_f and bottom_right_f <= up_f and bottom_right_f <= down_f and bottom_right_f <= above_right_f and bottom_right_f <= above_left_f and bottom_right_f <= bottom_left_f:
        checked[bottom_right_i][bottom_right_j] = 1
        current_i = bottom_right_i
        current_j = bottom_right_j
        g = g + 1
        print("Bottom Right (", current_i, ",", current_j, ")")


while flag:
    find_path(current_i, current_j)

    if current_i == goal_x and current_j == goal_y:#check whether state is goal state or not
        print("Path Found Successfully...")
        print("Your Path from (", source_x, ",", source_y, ") to (", goal_x, ",", goal_y, ") is as printed above...")
        flag = 0
