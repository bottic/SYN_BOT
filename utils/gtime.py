import datetime
from calendar import Calendar

delta = datetime.timedelta(hours=3, minutes=0)
now = datetime.datetime.now(datetime.timezone.utc) + delta  # текущие дата и время
y = now.year
m = now.month
d = now.day
h = now.hour
mi = now.minute

s = now.second
ms = now.microsecond


def get_day() -> str:
    datetime.datetime(y, m, d, h, mi, s, ms)
    return datetime.datetime.isoweekday(now)

    # if language == 'ru':
    #     time_ru = {1: 'Понедельник', 2: 'Вторник', 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота",
    #                7: "Воскресенье"}
    #     return time_ru[datetime.datetime.isoweekday(now)]
    # else:
    #     time_eng = {1: 'Mon', 2: 'Tue', 3:"Wed", 4:"Thu", 5:"Fri", 6: "Sat", 7: "Sun"}
    #     return time_eng[datetime.datetime.isoweekday(now)]


def get_date():
    return now.strftime("%d.%m.%y")


def get_dates():
    obj = Calendar()
    month = int(get_date().split('.')[1])
    year = int('20' + get_date().split('.')[2])

    out = []
    for el in obj.itermonthdates(year, month):
        out.append(f"{el.day}.{el.month}.{el.year}")
    return out


def get_week_dates():
    day = int(get_date().split('.')[0])
    month = int(get_date().split('.')[1])
    year = int('20' + get_date().split('.')[2])
    day_of_week = get_day()
    all_dates = get_dates()
    el = f"{day}.{month}.{year}"

    i_a = all_dates.index(el)
    row_list = all_dates[i_a - day_of_week + 1:(7 - day_of_week) + i_a + 1]
    return row_list
