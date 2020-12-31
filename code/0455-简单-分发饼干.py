def findContentChildren(g, s):
    # 每次，最小尺寸的饼干，去满足最大的可以满足的胃口
    g.sort()
    s.sort()
    idx_g = 0
    idx_s = 0
    counter = 0
    while (idx_g < len(g)) and (idx_s < len(s)):
        if s[idx_s] >= g[idx_g]:
            counter += 1
            idx_g   += 1
        idx_s   += 1
    return counter