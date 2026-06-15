import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ").strip()
        if name:
            names.append(name)

    except EOFError:

        print()
        break

if names:
    formatted_names = p.join(names)
    print(f"Adieu, adieu, to {formatted_names}")
