__author__ = "730715418"


def mimic(message: str) -> str:
    """Mimic the input message by returning it as output."""
    return message


def main() -> None:
    """Print result of the calling function mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
