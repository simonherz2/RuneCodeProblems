import sys

def main():
    n = int(sys.stdin.read())
    print("Even" if n % 2 == 0 else "Odd")

if __name__ == "__main__":
    main()