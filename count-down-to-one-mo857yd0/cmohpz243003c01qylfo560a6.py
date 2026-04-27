import sys

def main():
    n = int(sys.stdin.read())
    print("\n".join(str(x) for x in range(n, 0, -1)))

if __name__ == "__main__":
    main()