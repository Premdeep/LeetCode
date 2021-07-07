nums = [2, 7, 11, 15]
target = 9

for (i, x) in enumerate(nums):
    for(j, y) in enumerate(nums):
        if(i != j):
            if(x + y) == target:
                print(i, j)
                
           