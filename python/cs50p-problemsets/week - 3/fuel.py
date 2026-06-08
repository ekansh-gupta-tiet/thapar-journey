def main():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            if x <= y and y > 0 and x >= 0:
                break

        except (ValueError, ZeroDivisionError):

            pass

    percentage = round((x / y) * 100)

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

if __name__ == "__main__":
   main()


