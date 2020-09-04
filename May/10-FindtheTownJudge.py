'''
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.

You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

'''

# SOLUTION

def findJudge(N, trust):
    trusted = [0] * (N+1)
    for a, b in trust:
        trusted[a] -= 1
        trusted[b] += 1

    for i in range(1, N+1):
        if trusted[i] == N-1:
            return i
    return -1

# Directed graph approach,since a trusts b we have an array of trust values decrement a and increment b,
# since judge trusts no one, judge should have a score of N-1 (because everyone else trusts the judge)