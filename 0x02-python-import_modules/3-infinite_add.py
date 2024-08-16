#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    num = len(sys.argv) - 1
    total = 0
    if num == 0:
        print(0, end="")
    else:
        for item in range(num):
            total += int(sys.argv[item + 1])
    print("{}".format(total))
