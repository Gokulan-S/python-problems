#  https://www.hackerrank.com/challenges/py-set-intersection-operation/

n = int(input())  
english_subscribers = set(map(int, input().split()))

m = int(input())  
french_subscribers = set(map(int, input().split()))

common_subscribers = english_subscribers.intersection(french_subscribers)

print(len(common_subscribers))
