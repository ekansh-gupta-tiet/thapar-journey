import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    available_fonts = figlet.getFonts()

    if len(sys.argv) not in [1, 3]:
        sys.exit("Invalid usage")

    if len(sys.argv) == 3:
        flag = sys.argv[1]
        font_name = sys.argv[2]

        if flag not in ["-f", "--font"] or font_name not in available_fonts:
            sys.exit("Invalid usage")

        figlet.setFont(font=font_name)
    else:

        random_font = random.choice(available_fonts)
        figlet.setFont(font=random_font)

    user_input = input("Input: ")

    print("Output: ")
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()
