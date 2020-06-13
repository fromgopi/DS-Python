import math


def maxHeight(wallPos, wallHeight):
    wall_pos_length = len(wallPos)
    wall_hei_length = len(wallHeight)
    max_mud_wall_height = 0

    print("Length of the wallPosition = " + str(wall_pos_length))

    for i in range(0, wall_pos_length-1):
        if wallPos[i] < wallHeight[i - 1]:
            print(str(wallPos[i]) + " < " + str(wallHeight[i - 1]))
            height_difference = abs(wallHeight[i + 1] - wallHeight[i]) + 1
            print("Height Diff is = " + str(height_difference))
            gap_length = wallHeight[i + 1] - wallHeight[i] + 1
            print("gap diff is = " + str(gap_length))
            local_max = 0
            if gap_length > height_difference:
                low = max(wallHeight[i + 1], wallHeight[i]) + 1
                print("Lowest Point = " + str(low))
                remaining_gap = gap_length - height_difference + 1
                print("Remaining Gap to be filled is = " + str(remaining_gap))
                local_max = low + remaining_gap / 2
                print("Local_max = " + str(local_max))
            else:
                local_max = min(wallHeight[i + 1], wallHeight[i]) + gap_length
            max_mud_wall_height = max(max_mud_wall_height, local_max)

    print("Maximum Height of the mud wall = " + str(max_mud_wall_height))


def max_height(wall_position, wall_height):
    max_height = 0
    for i in range(0, len(wall_position)-1):
        space_between = wall_position[i+1]-wall_position[i]
        print("space deference = " + str(space_between))
        if space_between > 1:
            max_height = wall_height[i]
            counter = 0
            for j in range(0, space_between):
                if j == 1:
                    print("If case is ")
                    max_height += max_height
                elif max_height < wall_height[i+1]:
                    max_height += max_height
    print("Max height of the mud wall is = " + str(max_height))


if __name__ == '__main__':
    # wallPositions = [7, 12, 16, 22, 26, 29]
    # wallPositions = [7, 14, 21, 26, 29, 30, 33]
    wallPositions = [1, 2, 4, 7]
    # wallHeights = [8, 8, 9, 8, 8, 11]
    # wallHeights = [29, 31, 15, 37, 16, 35, 33]
    wallHeights = [4, 5, 7, 11]

    # maxHeight(wallPos=wallPositions, wallHeight=wallHeights)
    max_height(wall_position=wallPositions, wall_height=wallHeights)
