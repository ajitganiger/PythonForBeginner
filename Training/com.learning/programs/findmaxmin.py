__author__ = 'aganiger'


def maxmin(input):
    min = input[0]
    max = input[0]
    for i in range(1, len(input)):
        if input[i] < min:
            min = input[i]
        elif input[i] > max:
            max = input[i]
        else:
            pass

    return min, max


def main():
    input = [9, 5, 6, 12, 45, 78, 23, 56, 99, -20]
    print("min and max values are ", maxmin(input))

main()