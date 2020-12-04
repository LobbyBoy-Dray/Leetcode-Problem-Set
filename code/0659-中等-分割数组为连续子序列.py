import heapq

def isPossible(nums):
    my_dict = dict()
    for curr in nums:
        # 先保证有curr这么一个key
        if curr not in my_dict:
            my_dict[curr] = []
        # curr-1有子序列
        if my_dict.get(curr-1):
            heapq.heappush(my_dict[curr], heapq.heappop(my_dict.get(curr-1))+1)
        # curr-1没有子序列：没有curr-1/有但是为[]
        else:
            heapq.heappush(my_dict[curr], 1)
    
    print(my_dict)
    for i in my_dict:
        if my_dict[i] == []:
            continue
        if heapq.heappop(my_dict[i]) < 3:
            return False
    return True

if __name__ == "__main__":
    lst1 = [1,2,3,3,4,4,5,5]
    lst2 = [1,2,3,4,4,5]
    print(isPossible(lst1))
    print(isPossible(lst2))
