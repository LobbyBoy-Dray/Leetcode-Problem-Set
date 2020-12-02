def largestPerimeter(A):
    A = sorted(A)
    # ################ 正着遍历是傻叉…… ################
    # for idx in range(len(A)):
    #     if idx==0 or idx==1:
    #         continue
    #     tmp = A[idx-2]+A[idx-1]
    #     if (tmp>A[idx]) and (tmp+A[idx]>result):
    #         result = tmp+A[idx]
    # return result
    ################ 反着遍历直接返回 ################
    for idx in range(len(A))[::-1]:
        if idx==0 or idx==1:
            return 0
        tmp = A[idx-2]+A[idx-1]
        if tmp > A[idx]:
            return tmp+A[idx]

if __name__ == "__main__":
    demo1 = [1,2,1]
    demo2 = [3,2,3,4]
    print(largestPerimeter(demo1))
    print(largestPerimeter(demo2))