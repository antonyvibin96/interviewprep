def x_large_sum_subarray(arr,x):
    max_so_far=[]
    s=0
    for elem in arr:
        s=max(elem,elem+s)
        max_so_far.append(s)
    oall_sum=sum(arr[:x])
    op=oall_sum
    for i in range(x,len(arr)):
        oall_sum=oall_sum+arr[i]-arr[i-x]
        op=max(op,oall_sum)
        op=max(op,oall_sum+max_so_far[i-x])
    return op

li=[5,4,-2,10,6,7,2,-8]
print(sum(li))
print(x_large_sum_subarray(li,4))
