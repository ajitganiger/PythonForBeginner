__author__ = 'aganiger'


def find_month(month):
    switcher = {
        1: "Januarry",
        2: "Feb",
        3: "March"
    }
    print(switcher.get(month, "Invalid Month"))


find_month(3)