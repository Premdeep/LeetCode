# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

# Example 1:

# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].
# Example 2:

# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100


Alist = [1,2,3,2,1]
Blist = [3,2,1,4,7]
# BruteForce with 3 loops
def findLength(nums1, nums2):
    lenA = len(nums1)
    lenB = len(nums2)
    maxLen  = 0
    for i in range(lenA):
        for j in range(lenB):
            index = 0
            while((i+index)<  lenA and (j + index) < lenB and (nums1[i+index] == nums2[j + index])):
                index+=1
            if(index > maxLen):
                maxLen = index

    return maxLen

#print(findLength(Alist, Blist))

# BruteForce with Matrix
rows = len(Alist)
cols = len(Blist)
matrix = [[0 for i in range(rows)] for j in range(cols)]

def findLengthMatrix(nums1, nums2):
    rows = len(nums1)
    cols = len(nums2)
    #create the matrix with all 0's
    matrix = [[0 for i in range(cols)] for j in range(rows)]
    #fill the matrix
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = 1 if(nums1[i] == nums2[j]) else 0
    # fill it with max repeated subArray length
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] != 0:
                matrix[i][j] += matrix[i-1][j-1] 
    # find the max value out of all rows
    maxLen = 0
    for rows  in matrix:
        temp = max(rows)
        maxLen = max(temp, maxLen)
    return maxLen

# nums1 = [0,1,1,1,1]
# nums2 = [1,0,1,0,1]

nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4]

print(findLengthMatrix(nums1, nums2))
    




