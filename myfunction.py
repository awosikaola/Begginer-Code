def min_to_hours(min, sec):
    hours = min/60.0 + sec/3600.0
    return hours


print (min_to_hours(60, 7200))