def numberOfFriends(a, needed):
    friends_for = []
    for friend in a:
        couple = friend.split(":")
        if len(friends_for) == 0:
            friends_for.append((couple[0], [couple[1]]))
        else:
            for friend_for in friends_for:
                if (couple[0] == friend_for[0] and couple[1] in friend_for[1]) or (couple[1] == friend_for[0] and couple[0] in friend_for[1]):
                    continue
                elif couple[0] == friend_for[0]:
                    friend_for[1].append(couple[1])
                elif couple[1] == friend_for[0]:
                    friend_for[1].append(couple[0])
                elif couple[0] in friend_for[1]:
                    friend_for[1].append(couple[1])
                elif couple[1] in friend_for[1]:
                    friend_for[1].append(couple[0])
                else:
                    friends_for.append((couple[0], [couple[1]]))
    answer = ""
    for i in range(len(needed)):
        n = needed[i]
        for friend_for in friends_for:
            if friend_for[0] == n or n in friend_for[1]:
                answer += n + ": " + str(len(friend_for[1]))
                if i != len(needed):
                    answer += ", "
    return answer


if __name__ == "__main__":
    print(numberOfFriends(["Anne:Barbara", "Barbara:Ivan", "Vinny:Vlad"], ["Anne", "Vinny"]))
    print(numberOfFriends(["Octavia:Zoltan", "Zoltan:Marko", "Marko:Diego", "Diego:Andres"], ["Octavia", "Diego"]))
