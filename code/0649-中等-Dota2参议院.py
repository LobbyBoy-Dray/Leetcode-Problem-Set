def predictPartyVictory(senate):
    len_se = len(senate)
    ra = []
    di = []
    for idx in range(len(senate)):
        if senate[idx] == "R":
            ra.append(idx)
        else:
            di.append(idx)
    while ra and di:
        r = ra.pop(0)
        d = di.pop(0)
        if r < d:
            # R在前，则D被禁调
            ra.append(r+len_se)
        else:
            di.append(d+len_se)
    if ra == []:
        return "Dire"
    else:
        return "Radiant"