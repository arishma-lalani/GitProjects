# Question 7

def convert_seconds_since_midnight(seconds_since_midnight):
    if type(seconds_since_midnight) != int:
        return "Error: Input is not an integer!"
    if seconds_since_midnight < 0 or seconds_since_midnight > 24 * 3600:
        return "Error: Input has to be between 0 and 86399 seconds!"

    total_hours_since_midnight = seconds_since_midnight // 3600
    seconds_left_after_hours_calculated = seconds_since_midnight % 3600

    total_minutes_since_midnight = seconds_left_after_hours_calculated // 60
    total_seconds_since_midnight = seconds_left_after_hours_calculated % 60

    if total_hours_since_midnight < 12:
        AM_or_PM = "AM"
    else:
        AM_or_PM = "PM"

    twelve_hour_format = total_hours_since_midnight % 12
    if twelve_hour_format == 0:
        twelve_hour_format = 12

    final_formatted_time = f"{twelve_hour_format:02d}:{total_minutes_since_midnight:02d}:{total_seconds_since_midnight:02d} {AM_or_PM}"
    return final_formatted_time

print(convert_seconds_since_midnight(19067))