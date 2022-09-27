def convert(date):
    '''
    Enter data as this format "Month Day, Year"

    @Example "September 1, 2010
    '''
    months = [
        "Janurary",
        "Feburary",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December" 
      ]

date = "May 24"

# ["May", "24", "2022"]
month, day, year = date.split()

day_number = day[:2]
if day.isdigit() or int(day) < 1 or int(day) > 31:
    raise Exception("Invalid date, please enter number 1-31!")

formatted_month = month.capatalize()

index = -1
for index in range(le(months)):
    if months[i].startswith(formatted_month):
        index = i + 1
        break

    if index == -1:
        raise Exception("Invalid month! Must be one of", months)

month_number = index
    if index < 10:
        month_number = "0{0}".format(index)


print("Formatted month:", formatted_month)

if not year.isidgit():
    raise Exception("Invalid year format; must be digit!")

print(month_number + "/" + str(day_number) "/" + str(year))

convert("May 24, 2022")
