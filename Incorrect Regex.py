#  https://www.hackerrank.com/challenges/incorrect-regex/

import re

def is_valid_regex(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False

def main():
    T = int(input()) 
    results = []
    for _ in range(T):
        pattern = input().strip()
        results.append(is_valid_regex(pattern))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
