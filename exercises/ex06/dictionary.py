__author__: str = "730715418"


def invert(input: dict[str, str]) -> dict[str, str]:
    result = {}
    for key, value in input.items():
        if value in result:
            raise KeyError(f"Duplicate key found when inverting: {value}")
        result[value] = key
    return result


def favorite_color(rainbow: dict[str, str]) -> str:
    if not rainbow:
        return ""

    color_count: dict[str, int] = {}
    for name, color in rainbow.items():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    if color_count:
        max_count = max(color_count.values())
        for color in rainbow.values():
            if color_count[color] == max_count:
                return color


def count(number: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for item in number:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for abc in words:
        first_letter = abc[0].lower()
        if first_letter in result:
            result[first_letter].append(abc)
        else:
            result[first_letter] = [abc]
    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    if day in attendance:
        if student not in attendance[day]:
            attendance[day].append(student)
    else:
        attendance[day] = [student]
