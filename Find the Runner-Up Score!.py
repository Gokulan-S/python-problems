#    https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1=list(arr)
    max_score = max(arr1)
    while max_score in arr1:
        arr1.remove(max_score)
    runner_up_score = max(arr1)
    print(runner_up_score)
