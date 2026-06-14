import emoji

def main():

    user_input = input("input: ")

    output = emoji.emojize(user_input, language='alias')

    print(f"Output: {output}")

if __name__ == "__main__":
    main()
