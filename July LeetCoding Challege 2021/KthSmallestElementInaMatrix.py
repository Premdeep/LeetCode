# Question: Kth Smallest Element in a Sorted Matrix
# Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.


# Example 1:

# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
# Example 2:

# Input: matrix = [[-5]], k = 1
# Output: -5
 
# Constraints:

# n == matrix.length
# n == matrix[i].length
# 1 <= n <= 300
# -109 <= matrix[i][j] <= 109
# All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
# 1 <= k <= n2


def merge(Alist, Blist):
    res = []
    i,j = 0,0
    while(i < len(Alist) and j < len(Blist)):
        if(Alist[i] < Blist[j]):
            res.append(Alist[i])
            i+=1
        else:
            res.append(Blist[j])
            j+=1
    if(i == len(Alist)):
        while( j < len(Blist)):
            res.append(Blist[j])
            j+=1
    elif(j == len(Blist)):
        while(i < len(Alist)):
            res.append(Alist[i])
            i+=1
    else:
        print("something is not right!")
        #nothing
    return res


def kthSmallest(matrix, k):
    res = []
    for item in matrix:
        res = merge(item, res)
    # need to convert it from iterator to a List
    res = list(res)
    return res[k-1]

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
m = [[-5]]
n =[[1,2],[1,3]]
p = [[1,2],[1,3]]
print(kthSmallest(matrix, k))
#print(kthSmallest(p,2))