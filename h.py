def solution(S, T):
    if S == T:
        return "EQUAL"

    if len(T) - 1 == len(S):
        cc = ""
        insert = True
        j = 0
        for i in range(len(S)):
            if T[j] != S[i]:
                if cc == "":
                    cc = T[j]
                    j += 1
                else:
                    insert = False
                    break
            j += 1
        if insert:
            if cc == "":
                cc = T[len(T) - 1]
            return "INSERT " + cc

    if len(T) == len(S):
        ctr = ""
        ctrw = ""
        replace = True
        for i in range(len(S)):
            if S[i] != T[i]:
                if ctr == "":
                    ctr = S[i]
                    ctrw = T[i]
                else:
                    replace = False
                    break
        if replace:
            return "REPLACE " + ctr + " " + ctrw

    if len(T) == len(S):
        pcs = ""
        pct = ""
        ccs = ""
        cct = ""
        swap = True
        for i in range(len(T)):
            if T[i] != S[i]:
                if pcs == "":
                    pct = T[i]
                    pcs = S[i]
                elif ccs == "":
                    ccs = S[i]
                    cct = T[i]
                else:
                    swap = False
                    break

        if swap:
            if pcs == cct and pct == ccs:
                return "SWAP " + pcs + " " + ccs

    return "IMPOSSIBLE"


if __name__ == "__main__":
    print(solution("o", "odd"))
