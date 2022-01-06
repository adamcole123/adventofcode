import math

class SeaDepthScanner:

    def fast(self, data):
        count = 0
        index = 0
        prev = None

        for num in data:
            if index == len(data) - 1:
                current = data[index]
            elif index == len(data) - 2:
                current = data[index] + data[index + 1]
            else:
                current = data[index] + data[index + 1] + data[index + 2]
            
            if prev == None:
                prev = current
                continue 
                
            if current > prev:
                count = count + 1
                
            prev = current
            index = index + 1
        print("The increase rate is: " + str(count))
        
    def slow(self, data):
        count = 0
        prev = None;

        for num in data:
            if prev is None:
                prev = num
                continue
            
            if num > prev:
                count = count + 1
            
            prev = num
        print("The fast increase rate is: " + str(count))