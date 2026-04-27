import sys

def main():
    a, b, c = map(int, sys.stdin.read().split())
    print(max(a, b, c))

if __name__ == "__main__":
    main()