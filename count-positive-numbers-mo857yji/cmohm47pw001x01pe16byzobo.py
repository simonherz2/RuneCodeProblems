import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    arr = data[1:1 + n]
    print(sum(1 for x in arr if x > 0))

if __name__ == "__main__":
    main()