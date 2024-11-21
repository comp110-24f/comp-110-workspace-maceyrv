def odds_list(min: int, max: int) -> list[int]:
    """returns list of odds between min and max"""
    odds: list[int] = min
    x: int = min
    while x <= max:
        if x % 2 == 1:
            odds.append(x)
        x +=1
    return odds

global_odds: list[int] = odds_list(2,6)
print(global_odds)
