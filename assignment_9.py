def zipper_file(filename, strings):
    file = open(filename, "w")

    for i in range(0, len(strings), 2):
        file.write(strings[i] + strings[i + 1] + "\n")

    file.close()


def reformat_date(dates):
    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]

    result = []

    for date in dates:
        parts = date.split("/")

        month = int(parts[0])
        day = parts[1]
        year = parts[2]

        new_date = "Office Hours on " + months[month - 1] + " " + day + ", " + year
        result.append(new_date)

    return result
