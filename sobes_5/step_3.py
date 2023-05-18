def last_stone(stones):
    if len(stones) == 1:
        return stones[0]
    elif len(stones) == 0:
        return (0)
    else:
        current_stones = sorted(stones)
        if current_stones[-1] == current_stones[-2]:
            current_stones.pop(-1)
            current_stones.pop(-1)
        else:
            current_stones.append(current_stones[-1] - current_stones[-2])
            current_stones.pop(-2)
            current_stones.pop(-2)
        return last_stone(current_stones)