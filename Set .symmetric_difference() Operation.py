#  https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/

n = int(input())  
english_subscribers = set(map(int, input().split()))

m = int(input())  
french_subscribers = set(map(int, input().split()))

unique_subscribers = english_subscribers.symmetric_difference(french_subscribers)
print(len(unique_subscribers))
