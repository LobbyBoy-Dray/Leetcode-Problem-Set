# x与y是字符串：x+y>y+x则y一定出现在x前面
numList = [3,30,34,5,9]
numList = [0,1,2,3,4,5]
numList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def minNumber(numList):
    numList = [str(i) for i in numList]
    def mergeSort(numList):
        if len(numList) <= 1:
            return numList
        list1 = numList[:len(numList)//2]
        list2 = numList[len(numList)//2:]
        list1 = mergeSort(list1)
        list2 = mergeSort(list2)
        finalList = []
        while len(list1) > 0 and len(list2) > 0:
            if list1[0] + list2[0] > list2[0] + list1[0]:
                finalList.append(list2[0])
                list2.pop(0)
            else:
                finalList.append(list1[0])
                list1.pop(0)
        if len(list1) != 0:
            finalList.extend(list1)
        if len(list2) != 0:
            finalList.extend(list2)
        return finalList
    return "".join(mergeSort(numList))

print(minNumber(numList))