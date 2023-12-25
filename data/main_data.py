import os
import pandas as pd

from calendar import Calendar
import json
from utils.gtime import get_date, get_day, get_dates, get_week_dates

groups = {"дбо-101рпо": 'dbo101.xlsx', 'дбо-102рпо': "dbo102.xlsx", "дбп-101рив": 'dbp101.xlsx',
          "дбо-161рпо": "dbo101.xlsx"}


def d(group):
    group = groups[group]
    path = os.getcwd()

    # Вариант для работы бота
    excel_data_df = pd.read_excel(path + f"/data_xlsx/{group}")

    # Вариант для теста локально, не забудь перекинуть xlsx файл в папку data
    # excel_data_df = pd.read_excel(path + f"/{group}")

    json_str = excel_data_df.to_json(orient='records', force_ascii=False)
    student_details = json.loads(json_str)

    c = 0
    dict_lession = {}
    kur = []
    for el in student_details:
        if len(el["Время"].split(',')) != 1 and c == 0:
            name = el["Время"].split(',')[0].strip()
            c = 1
            kur.append(el)
            continue

        if len(el["Время"].split(',')) != 1:
            dict_lession[name] = kur
            kur = []
            name = el["Время"].split(',')[0].strip()
        kur.append(el)
    return dict_lession


def get_day_schedule(group) -> str:
    dict_lession = d(group)
    s = ''
    date = get_date()

    _d = dict_lession.get(date)

    if _d is None:
        s = "Сегодня у вас нет пар;):)()("
        return s

    for _val in _d[1:]:
        time = _val["Время"]
        lession = _val["Курс"]
        classroom = _val["Место проведения"]
        teacher = _val["Преподаватель"]

        s += ("Время: " + time + '\n' + "Предмет: " + lession + '\n'
              + "Кабинет: " + '\n' + classroom + '\n' + 'Преподаватель: ' + teacher + '\n\n')
    return s


def get_next_day_schedule(group) -> str:
    dict_lession = d(group)
    s = ''

    tdate = get_date()
    day = tdate.split('.')[0]
    month = tdate.split('.')[1]
    year = '20' + tdate.split('.')[2]
    dates = get_dates()
    index_tday = dates.index(f'{day}.{month}.{year}')

    ndate = dates[index_tday + 1]
    day = ndate.split('.')[0]
    month = ndate.split('.')[1]
    year = ndate.split('.')[2]
    year = year[2:]
    _d = dict_lession.get(f'{day}.{month}.{year}')

    if _d is None:
        s = "Завтра у вас нет пар;):)()("
        return s

    for _val in _d[1:]:
        time = _val["Время"]
        lession = _val["Курс"]
        classroom = _val["Место проведения"]
        teacher = _val["Преподаватель"]

        s += ("Время: " + time + '\n' + "Предмет: " + lession + '\n'
              + "Кабинет: " + '\n' + classroom + '\n' + 'Преподаватель: ' + teacher + '\n\n')
    return s


def get_week_schedule(group) -> str:
    dict_lession = d(group)
    s = ''

    list_of_days_week = []

    for el in get_week_dates():
        _day = el.split('.')[0]
        if len(_day) == 1:
            _day = '0' + _day
        _month = el.split('.')[1]
        if len(_month) == 1:
            _month = '0' + _month
        _year = el.split('.')[2]
        _year = _year[2:]
        list_of_days_week.append(f"{_day}.{_month}.{_year}")

    s += '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n'

    for el in list_of_days_week:
        try:
            __check = _val in dict_lession[el][1:]
            s += '                           ' + el + '\n'
            for _val in dict_lession[el][1:]:
                time = _val["Время"]
                lesson = _val["Курс"]
                classroom = _val["Место проведения"]
                teacher = _val["Преподаватель"]

                s += ("Время: " + time + '\n' + "Предмет: " + lesson + '\n'
                      + "Кабинет: " + '\n' + classroom + '\n' + 'Преподаватель: ' + teacher + '\n\n')
            s += '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n'
        except:
            pass
    return s


# print(get_week_schedule(""))
