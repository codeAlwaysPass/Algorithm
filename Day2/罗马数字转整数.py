rome_num_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def romeToInt(s):
    if len(s) == 0:
        return 0

    res = rome_num_map[s[0]]

    for i in range(1, len(s)):
        if s[i - 1] == "I":
            if s[i] == "V":
                res += 3
            elif s[i] == "X":
                res += 8
            else:
                res += rome_num_map[s[i]]
        elif s[i - 1] == "X":
            if s[i] == "L":
                res += 30
            elif s[i] == "C":
                res += 80
            else:
                res += rome_num_map[s[i]]
        elif s[i - 1] == "C":
            if s[i] == "D":
                res += 300
            elif s[i] == "M":
                res += 800
            else:
                res += rome_num_map[s[i]]
        else:
            res += rome_num_map[s[i]]

    return res


print(romeToInt("MCMXCIV"))
