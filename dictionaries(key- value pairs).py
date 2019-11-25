month_conversions={
    'jan ':'january',
    "feb":"february",
    "mar":"march",
    "apr":"april",
    "may": "may",
    "jun": "june",
    "jul": "july",
    "aug": "august",
    "sep": "september",
    "oct": "october",
    "nov": "november",
    "dec": "december",

}
print(month_conversions.get("mar"))
print(month_conversions.keys())
print(month_conversions.fromkeys("jun"))
print(month_conversions.copy())
print(month_conversions.items())
print(month_conversions.pop("dec"))
del month_conversions["sep"]
print(month_conversions)
month_conversions.clear()
print(month_conversions)
