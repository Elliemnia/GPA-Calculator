


# GPA Calculator


def display():
    print("1 Enter course grade and units")
    print("2 Show GPA")
    print("3 Exit")

    x = int(input())

    if 1 <= x <= 3:
        return  x 
    else:
        print("error: unknown command")
        return -1


def legal(a, l, u):
    if l <= a <= u:
        return True
    return False


def main():

    total_units = 0
    total_points = 0

    while True:

        x = display()

        if x == 1:
            g = input("Enter course grade: ")
            u = input("Enter course units: ")

            if not legal(int(g), 0, 4):
                print("invalid grade range")
                continue

            if not legal(int(u), 1, 5):
                print("invalid unit range")
                continue

            total_points += int(g) * int(u)
            total_units += int(u)

        elif x == 2:
            print("GPA")
            if total_units != 0:
                print(total_points / total_units)
            else:
                print("not available")

        elif x == 3:
            break


if __name__ == "__main__":
    main()
