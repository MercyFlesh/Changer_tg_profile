import datetime

def get_time():
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=+3)
    minutes = f"{now:%H:%M}"
    return minutes


def time_progress():
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=+3)
    now_seconds = (int(now.strftime('%H')) * 60 + int(now.strftime('%M'))) * 60 + int(now.strftime('%S'))
    
    if now_seconds >= 28800 and now_seconds <= 84600:
        percent_progress = (now_seconds - 28800)/55800 # 8:00 - 23:30
    else:
        percent_progress = 0

    scale_progress = int(20 * percent_progress)
    scale = "Work day progress: ["

    for _ in range(0, scale_progress): 
        scale += '█'
    for _ in range(0, 20 - scale_progress):
        scale += '─'
    scale += ']'
    temp = f"{now:%H:%M} {scale}{round(percent_progress * 100, 2)}%"

    return temp
