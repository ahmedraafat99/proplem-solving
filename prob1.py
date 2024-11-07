def century_from_year(year):
    return (year - 1) // 100 + 1

while True:
    try:
        year = int(input("Input year to determine century (or type '0' to exit): "))
        if year == 0:
            break
        print("Century:", century_from_year(year))
    except ValueError:
        print("Please enter a valid year.")
        ##
