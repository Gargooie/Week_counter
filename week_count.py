from datetime import date

# the input is converted to right format
a, b, c = input("enter the date(e.g. 2020 5 12): ").split(' ')
date2 = date(int(a), int(b), int(c))


def week_count(date2):
    # the last day of preceding week minus a week 'cause the first week is not 0
    date1 = date(2018, 12, 23)
    # The date should be correct format
    if type(date2) not in [date]:
        raise TypeError("Wrong date format")
    if (date2 - date1).days < 0:
        raise ValueError("The date is earlier than given date")
    # days=weeks output
    return (date2 - date1).days // 7


print("Week number: " + str(week_count(date2)))
