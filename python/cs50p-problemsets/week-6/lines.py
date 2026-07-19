import sys

def main():
 
    check_arguments()

    filename = sys.argv[1]

    try:
        with open(filename, "r") as file:
            loc_count = 0
            for line in file:
                if is_code_line(line):
                    loc_count += 1

            print(loc_count)

    except FileNotFoundError:
        sys.exit("File does not exist")


def check_arguments():
    """Validates command-line arguments."""
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")


def is_code_line(line):
    """
    Returns True if the line is actual code.
    Returns False if it is a blank line or a comment.
    """

    stripped_line = line.lstrip()


    if not stripped_line or stripped_line.startswith("#"):
        return False

    return True


if __name__ == "__main__":
    main()
