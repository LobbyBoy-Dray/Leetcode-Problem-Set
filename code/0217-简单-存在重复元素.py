def containsDuplicate(nums):
    my_dict = dict()
    for i in nums:
        if i in my_dict:
            return True
        else:
            my_dict[i] = "mmp"
    return False