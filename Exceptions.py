#  https://www.hackerrank.com/challenges/exceptions/

def handle_division(a, b):
    try:
        result = int(a) // int(b)
        return result
    except ZeroDivisionError as e:
        return f"Error Code: {e}"
    except ValueError as e:
        return f"Error Code: {e}"

def main():
    T = int(input())
    results = []
    for _ in range(T):
        a, b = input().split()
        result = handle_division(a, b)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
