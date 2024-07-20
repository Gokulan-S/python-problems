#  https://www.hackerrank.com/challenges/no-idea/

def calculate_happiness(n, m, arr, A, B):
    happiness = 0
    A = set(A)
    B = set(B)
    
    for i in arr:
        if i in A:
            happiness += 1
        elif i in B:
            happiness -= 1
    
    return happiness

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    result = calculate_happiness(n, m, arr, A, B)
    print(result)
