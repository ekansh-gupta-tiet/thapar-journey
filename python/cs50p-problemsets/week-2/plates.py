def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")

    else:
        print("Invalid")

def is_valid(s):

    if len(s) < 2 or len(s) > 6:
      return False

    if not s.isalnum():
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    has_seen_digit = False

    for char in s:
        if char.isdigit():
            if not has_seen_digit and char == '0':
                return False
            has_seen_digit = True


        elif char.isalpha():

            if has_seen_digit:
                return False


    return True

if __name__ == "__main__":
    main()


