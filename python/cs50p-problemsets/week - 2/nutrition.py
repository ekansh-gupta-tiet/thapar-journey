def main():

    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "sweet cherries": 100,
        "cantaloupe": 50,
        "grapefruit": 60,
        "kiwifruit": 90,
        "pear": 100,
     }


    item = input("Item: ").strip().lower()

    if item in fruits:
        print(f"calories: {fruits[item]}")


if __name__ == "__main__":
  main()

