import sys

def main():
    args = sys.argv
    assert(len(args) == 2)
    print(f"test {args[1]}")
    return 0

if __name__ == "__main__":
    main()
