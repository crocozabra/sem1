#https://www.e-olymp.com/uk/submissions/9849247
n = int(input())

def counter(col):
    counts = dict.fromkeys(col, 0)
    for e in col:
        counts[e] += 1
    return counts

for i in range(n):

    votes_num = int(input())
    votes = []

    for j in range(votes_num):
        votes.append(int(input()))
    votes_counts = counter(votes)
    max_n = max(votes_counts.values())
    #for x in votes_counts.keys():
        #if :


    print(min(x for x in votes_counts.keys() if votes_counts[x] == max_n))

            #break






