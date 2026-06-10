def main():
    months = [
        "January", "February", "March", "April", "May", "june", "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date = input("Date: ").strip()

        if "/" in date:
            try:
                month, day, year = date.split("/")
                month = int(month)
                year = int(year)
                day = int(day)

                if 1 <= month <= 12 and 1 <= day <= 31:

                  print(f"{year}-{month:02d}-{day:02d}")
                  break

            except ValueError:

                continue

        elif "," in date:
            try:
                parts = date.replace(",", "").split()

                if len(parts) == 3:
                    month_name, day_str, year_str = parts

                    if month_name in months:
                        month = months.index(month_name) + 1
                        day = int(day_str)
                        year = int(year_str)

                        if 1 <= day <= 31:
                           print(f"{year}-{month:02d}-{day:02d}")

            except ValueError:
                continue

if __name__ == "__main__":
   main()

