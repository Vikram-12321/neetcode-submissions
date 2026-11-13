class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [2, 1, 1, 3]
        # Look at 3. 
        # what can we say about [2, 1, 1]? 
        # Memory Stack: None    Operation: None           Stack: [2, 1, 1, 3]
        # Memory Stack: 3       Operation: pop            Stack: [2, 1, 1]
        # We pop 1, is 1 > 3? Yes => add 1
        # We pop 1 again, is 1 > 1, no, is 1>3, yes => add 2
        # We pop 2, is 1>2, no - look at index of thing larger than 1 - 3: is 3>2 yes => add ( 1 + 2) = 3

        stack = [] # Stack = [2, 1, 1, 3]
        n = len(temperatures)
        indicies = []

        for temp in temperatures: 
            stack.append(temp)
        
        for i in range(n):
            temp = stack.pop() # Iter 1: 3, Iter 2: 1, Iter 3: 1, Iter 4: 2

            if i == 0:
                indicies.append((temp, 0)) # [(3,0)]

            else:
                max_found = False
                index = len(indicies) - 1
                jumps = 0
                while max_found == False:

                    (temp2, max_idx) = indicies[index] 
                    # Iter 1: (3,0) = indicies[0]
                    # Iter 2: (1, 1) = indicies[1] 
                        # Iter 2i: (3,0) = indicies[0]
                    # Iter 3: (1, 2) = indicies[2] 
                        # Iter 3i: (3,0) = indicies[0] (index = 0, jumps = 2)

                    if temp2 > temp: 
                        indicies.append((temp, jumps + 1))
                        max_found = True
                        # Iter 1: 3 > 1 - Yes, then: indicies.append((1, 0+1))
                        # Iter 2: 1 > 1 - False
                            # Iter 2i: 3 > 1 - Yes!, then: indicies.append((1, 1+1))
                        # Iter 3: 1 > 2: False
                            # Iter 3i: 3 > 2 - Yes!, then: indicies.append((2, 2+1))

                    elif max_idx == 0:
                        indicies.append((temp, 0))
                        max_found = True
                        # Iter 2: Max idx = 1, False
                        # Iter 3: Max idx = 2, False
                    
                    elif temp2 <= temp:
                        index -= max_idx
                        jumps += max_idx

                        if jumps > len(indicies):
                            indicies.append((temp, 0))
                            max_found = True
                        # Iter 2: Max idx = 1, index = 1 -= 1 = 0, jumps = 0 += 1 = 1
                        # iter 3: Max idx = 2, index = 2 -= 2 = 0, jumps = 0 += 2 = 2                        

        # [(3,0), (1, 1), (1, 2), (2,3)]

        result = [item[1] for item in indicies][::-1] #O(n)

        return result 


            

        