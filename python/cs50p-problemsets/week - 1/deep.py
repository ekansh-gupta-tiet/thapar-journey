def main():

    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    cleaned_answer = answer.strip().lower()

    
    if cleaned_answer == "42" or cleaned_answer == "forty-two" or cleaned_answer == "forty two":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
