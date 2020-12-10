def lemonadeChange(bills):
    # 20块钱对于找零没有任何帮助——不会找20块给人的
    num_5  = 0
    num_10 = 0
    for bill in bills:
        if bill == 5:
            num_5 += 1
        if bill == 10:
            if num_5 == 0:
                return False
            else:
                num_10 += 1
                num_5  -= 1
        if bill == 20:
            # 优先找10块的，why？因为10块的只能用来找20元
            # 如果找10块都完不成，找5块更完不成
            # 找15元
            if (num_10>=1) and (num_5>=1):
                num_10 -= 1
                num_5  -= 1
            elif (num_5>=3):
                num_5  -= 3
            else:
                return False
    return True