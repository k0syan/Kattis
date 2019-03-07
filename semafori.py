if __name__ == "__main__":
    n, l = [int(i) for i in input().split()]
    total_time = 0
    total_distance = 0
    previous_position = 0
    while n != 0:
        d, r, g = [int(a) for a in input().split()]
        total_time += d - previous_position
        total_distance += d - previous_position
        previous_position = d
        
        mn = total_time % (r + g)
        if mn <= r:
            total_time += r - mn

        n -= 1

    if total_distance < l:
        total_time += l - total_distance
    print(total_time)
