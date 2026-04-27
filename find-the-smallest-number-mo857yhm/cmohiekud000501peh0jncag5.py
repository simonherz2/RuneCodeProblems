import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    arr = data[1:1 + n]
    print(min(arr))

if __name__ == "__main__":
    main()