import math
import re

class NavigationController:

    def standard_mode(self, data):
        horizontal_pos = 0
        depth = 0
        
        for direction in data:
            split = re.split(" ", direction)
            if split[0] == "forward":
                horizontal_pos = horizontal_pos + int(split[1])
            elif split[0] == "up":
                depth = depth - int(split[1])
            elif split[0] == "down":
                depth = depth + int(split[1])  
                
        print("The final position is: " + str(horizontal_pos) + ", " + str(depth))
        print("The coordinates multiplied is: " + str(horizontal_pos * depth))
        
    def aim_mode(self, data):
        horizontal_pos = 0
        depth = 0
        aim = 0
        
        for direction in data:
            split = re.split(" ", direction)
            if split[0] == "forward":
                horizontal_pos = horizontal_pos + int(split[1])
                depth = depth + (aim * int(split[1]))
            elif split[0] == "up":
                aim = aim - int(split[1])
            elif split[0] == "down":
                aim = aim + int(split[1])  
                
        print("The final position is: " + str(horizontal_pos) + ", " + str(depth))
        print("The coordinates multiplied is: " + str(horizontal_pos * depth))