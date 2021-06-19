# from sys import maxsize
# def maxSubArraySum(a,size):

#     max_so_far = -maxsize - 1
#     max_ending_here = 0

#     for i in range(0, size):
#         max_ending_here = max_ending_here + a[i]
#         if (max_so_far < max_ending_here):
#             max_so_far = max_ending_here

#         if max_ending_here < 0:
#             max_ending_here = 0
#     return max_so_far

def maxSubArraySum(a1, size):

    max_so_far = a1[0]
    max_ending_here = 0
    a = a1
    # previous=a1[0]
    # for x in a1:
    #         a.append(previous-x)
    #         previous=x
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0

        # Do not compare for all elements. Compare only
        # when  max_ending_here > 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    return max_so_far


# Driver function to check the above function
prices = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum contiguous sum is", maxSubArraySum(prices, len(prices)))
