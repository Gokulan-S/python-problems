#  https://www.hackerrank.com/challenges/designer-door-mat/

def create_door_mat(N, M):
    pattern = []
    for i in range(1, N, 2):
        line = ('.|.' * i).center(M, '-')
        pattern.append(line)


    for line in pattern:
        print(line)
    
    print('WELCOME'.center(M, '-'))
    
    for line in reversed(pattern):
        print(line)

if __name__ == '__main__':
    N, M = map(int, input().split())
    create_door_mat(N, M)
