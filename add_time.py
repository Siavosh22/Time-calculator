def add_time(start_time,duration_time,starting_day=None):
    answer = ""
    ap = ""
    start_time_total = start_time.split(" ")
    start_time_time = start_time_total[0].split(":")
    ap = start_time_total[1]
    duration_time = duration_time.split(":")
    a = int(start_time_time[0])
    b = int(start_time_time[1])
    c = int(duration_time[0])
    d = int(duration_time[1])
    if ap == "PM":
        a = a +12
    total_duration_time = (c*60)+ d
    time_starter = (a*60) + b
    total_min = total_duration_time + time_starter
    final_total_min = total_min % 60
    total_hour = total_min // 60
    current_hour = total_hour % 24
    days = total_hour // 24
    final_hour = current_hour % 12
    if current_hour // 12 == 0:
        new_ap = "AM"
        if final_hour == 0:
            final_hour = 12
    else:
        new_ap = "PM"
        if final_hour == 0:
            final_hour = 12
    answer = str(final_hour)+":"+str(final_total_min) +" "+ new_ap
    if not starting_day == None:
        weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day = 0
        while True:
            if starting_day.lower() == weeks[day].lower():
                break
            day = day + 1
        new_day = weeks[((day + (days % 7)) % 7)]
        answer = answer + ","+ new_day
    if days == 1:
        answer = answer + " (next day)"
    elif days > 1:
        days = str(days)
        answer = answer + " (" + days + " days later)"

    print(answer)






