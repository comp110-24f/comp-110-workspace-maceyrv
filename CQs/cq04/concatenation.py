__author__ = "730715418"

"""concatenate two strings"""

# File: concatenation.py

# Define the concat function
def concat(str1: str, str2:str) -> str:
    return str1 + str2

# Global variables
word1 = "happy"
word2 = "tuesday"

if __name__ == "__main__":
# Print the result of calling concat with word1 and word2
    print(concat(word1, word2))
