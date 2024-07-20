#  https://www.hackerrank.com/challenges/symmetric-difference/

def symmetric_difference(a, b):
    return sorted(a.symmetric_difference(b))

if __name__ == '__main__':
    
    M = int(input())
    a = set(map(int, input().split()))
    N = int(input())
    b = set(map(int, input().split()))
    
    result = symmetric_difference(a, b)
    for element in result:
        print(element)
