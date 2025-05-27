# -*- coding: utf-8 -*-
import sqlite3
import tkinter as tk
import os


from resources import loading_window

class Totals:
    def __init__(self):
        self.total_first_semester = 0
        self.total_second_semester = 0
        self.total_academic_year = 0
        self.counter_first_semester = 0
        self.counter_second_semester = 0
        self.counter_academic_year = 0



def task1(root, name_db):
    root.withdraw()
    loading = loading_window(root)

    conn = sqlite3.connect(name_db)
    cursor = conn.cursor()
    job_info = cursor.execute("SELECT * FROM РОБОЧА_ІНФОРМАЦІЯ").fetchall()
    person_info = cursor.execute("SELECT * FROM ЛЮДСЬКА_ІНФОРМАЦІЯ").fetchall()
    vacancy_info = cursor.execute("SELECT * FROM ІНФОРМАЦІЯ_ВАКАНСІЯ").fetchall()
    first_semester_info = cursor.execute("SELECT * FROM ПЕРШИЙ_СЕМЕСТР").fetchall()
    second_semester_info = cursor.execute("SELECT * FROM ДРУГИЙ_СЕМЕСТР").fetchall()
    academic_year_info = cursor.execute("SELECT * FROM АКАДЕМІЧНИЙ_РІК").fetchall()
    code_and_year_info = cursor.execute("SELECT * FROM КОД_РІК").fetchall()
    conn.close()

    path_to_file_txt = "resources/Середнє навантаження НПП/result.txt"

    if os.path.exists(path_to_file_txt):
        os.remove(path_to_file_txt)


    people = (Totals(),Totals(),Totals(),Totals(),Totals(),Totals(),Totals(),Totals())
    i=-1

    # Середнє навантаження НПП
    # количесво ставок и количество нагрузки за год сумируем
    # потом нагрузку делим на количество ставок

    # Середнє лекційне навантаження НПП
    # лекционная без ассистентов и без старших викладачыв которые не читают лекции часі и ставки
    # потом нагрузку делим на количество ставок

    # Середнє аудіторне навантаження НПП
    # cреднее аудиторное складываем практику плюс лабы часі и ставки
    # потом нагрузку делим на количество ставок
    # добавляем среднюю лекионную (2 запит которій біл)

    for helper in job_info:
        i+=1

        people[7].counter_first_semester += float(first_semester_info[i][1])
        people[7].counter_second_semester += float(second_semester_info[i][1])
        people[7].counter_academic_year += float(academic_year_info[i][1])

        people[7].total_first_semester += float(first_semester_info[i][22])
        people[7].total_second_semester += float(second_semester_info[i][22])
        people[7].total_academic_year += float(academic_year_info[i][22])

        if str(helper[1]) == "заф. кафедри":
            people[0].counter_first_semester+=float(first_semester_info[i][1])
            people[0].counter_second_semester += float(second_semester_info[i][1])
            people[0].counter_academic_year += float(academic_year_info[i][1])

            people[0].total_first_semester+=float(first_semester_info[i][22])
            people[0].total_second_semester+=float(second_semester_info[i][22])
            people[0].total_academic_year+=float(academic_year_info[i][22])

        elif  str(helper[1]) == "професор":
            people[1].counter_first_semester += float(first_semester_info[i][1])
            people[1].counter_second_semester += float(second_semester_info[i][1])
            people[1].counter_academic_year += float(academic_year_info[i][1])

            people[1].total_first_semester += float(first_semester_info[i][22])
            people[1].total_second_semester += float(second_semester_info[i][22])
            people[1].total_academic_year += float(academic_year_info[i][22])

        elif str(helper[1]) == "доцент":

            people[2].counter_first_semester += float(first_semester_info[i][1])
            people[2].counter_second_semester += float(second_semester_info[i][1])
            people[2].counter_academic_year += float(academic_year_info[i][1])

            people[2].total_first_semester += float(first_semester_info[i][22])
            people[2].total_second_semester += float(second_semester_info[i][22])
            people[2].total_academic_year += float(academic_year_info[i][22])

        elif str(helper[1]) == "ст. викладач":
            people[3].counter_first_semester += float(first_semester_info[i][1])
            people[3].counter_second_semester += float(second_semester_info[i][1])
            people[3].counter_academic_year += float(academic_year_info[i][1])

            people[3].total_first_semester += float(first_semester_info[i][22])
            people[3].total_second_semester += float(second_semester_info[i][22])
            people[3].total_academic_year += float(academic_year_info[i][22])

        elif str(helper[1]) == "асистент":
            people[4].counter_first_semester += float(first_semester_info[i][1])
            people[4].counter_second_semester += float(second_semester_info[i][1])
            people[4].counter_academic_year += float(academic_year_info[i][1])

            people[4].total_first_semester += float(first_semester_info[i][22])
            people[4].total_second_semester += float(second_semester_info[i][22])
            people[4].total_academic_year += float(academic_year_info[i][22])

        elif str(helper[1]) == "в.о. заф. кафедри":
                people[5].counter_first_semester += float(first_semester_info[i][1])
                people[5].counter_second_semester += float(second_semester_info[i][1])
                people[5].counter_academic_year += float(academic_year_info[i][1])

                people[5].total_first_semester += float(first_semester_info[i][22])
                people[5].total_second_semester += float(second_semester_info[i][22])
                people[5].total_academic_year += float(academic_year_info[i][22])

        elif str(helper[1]) == "викладач":
                people[6].counter_first_semester += float(first_semester_info[i][1])
                people[6].counter_second_semester += float(second_semester_info[i][1])
                people[6].counter_academic_year += float(academic_year_info[i][1])

                people[6].total_first_semester += float(first_semester_info[i][22])
                people[6].total_second_semester += float(second_semester_info[i][22])
                people[6].total_academic_year += float(academic_year_info[i][22])


    for person in people:

        if float(person.total_first_semester) == 0 or float(person.counter_first_semester) == 0:
            person.total_first_semester = 0
        else:
            person.total_first_semester = round(float(person.total_first_semester) / float(person.counter_first_semester), 2)


        if float(person.total_second_semester) == 0 or float(person.counter_second_semester) == 0:
            person.total_second_semester = 0
        else:
            person.total_second_semester = round(float(person.total_second_semester) / float(person.counter_second_semester), 2)

        if float(person.total_academic_year) == 0 or float(person.counter_academic_year) == 0:
            person.total_academic_year = 0
        else:
            person.total_academic_year = round(float(person.total_academic_year) / float(person.counter_academic_year),2)


    with open(path_to_file_txt, "a") as file:
        file.write(f"Середнє навантаження НПП (заф. кафедри):\n\tперший семестр: {people[0].total_first_semester}\n\tдругий семестр: {people[0].total_second_semester}\n\tрік {people[0].total_academic_year}\n\n")
        file.write(f"Середнє навантаження НПП (професор):\n\tперший семестр: {people[1].total_first_semester}\n\tдругий семестр: {people[1].total_second_semester}\n\tрік {people[1].total_academic_year}\n\n")
        file.write(f"Середнє навантаження НПП (доцент):\n\tперший семестр: {people[2].total_first_semester}\n\tдругий семестр: {people[2].total_second_semester}\n\tрік {people[2].total_academic_year}\n\n")
        file.write(f"Середнє навантаження НПП (ст. викладач):\n\tперший семестр: {people[3].total_first_semester}\n\tдругий семестр: {people[3].total_second_semester}\n\tрік {people[3].total_academic_year}\n\n")
        file.write(f"Середнє навантаження НПП (асистент):\n\tперший семестр: {people[4].total_first_semester}\n\tдругий семестр: {people[4].total_second_semester}\n\tрік {people[4].total_academic_year}\n\n")
        file.write(f"Середнє навантаження НПП (в.о. заф. кафедри):\n\tперший семестр: {people[5].total_first_semester}\n\tдругий семестр: {people[5].total_second_semester}\n\tрік {people[5].total_academic_year}\n\n")
        file.write(f"Середнє навантаження НПП (викладач):\n\tперший семестр: {people[6].total_first_semester}\n\tдругий семестр: {people[6].total_second_semester}\n\tрік {people[6].total_academic_year}\n\n")
        file.write(f"Середнє навантаження НПП (всі):\n\tперший семестр: {people[7].total_first_semester}\n\tдругий семестр: {people[7].total_second_semester}\n\tрік {people[7].total_academic_year}\n\n")

    loading.destroy()
    root.deiconify()
    washed_down_main_menu(root, name_db)

def task2(root, name_db):
    root.withdraw()
    loading = loading_window(root)

    conn = sqlite3.connect(name_db)
    cursor = conn.cursor()
    job_info = cursor.execute("SELECT * FROM РОБОЧА_ІНФОРМАЦІЯ").fetchall()
    person_info = cursor.execute("SELECT * FROM ЛЮДСЬКА_ІНФОРМАЦІЯ").fetchall()
    vacancy_info = cursor.execute("SELECT * FROM ІНФОРМАЦІЯ_ВАКАНСІЯ").fetchall()
    first_semester_info = cursor.execute("SELECT * FROM ПЕРШИЙ_СЕМЕСТР").fetchall()
    second_semester_info = cursor.execute("SELECT * FROM ДРУГИЙ_СЕМЕСТР").fetchall()
    academic_year_info = cursor.execute("SELECT * FROM АКАДЕМІЧНИЙ_РІК").fetchall()
    code_and_year_info = cursor.execute("SELECT * FROM КОД_РІК").fetchall()
    conn.close()

    path_to_file_txt = "resources/Середнє лекційне навантаження НПП/result.txt"

    if os.path.exists(path_to_file_txt):
        os.remove(path_to_file_txt)

    people = (Totals(), Totals(), Totals(), Totals(), Totals(), Totals(), Totals())
    i = -1

    for helper in job_info:
        i+=1

        if str(helper[1]) != "асистент" and (str(helper[1]) == "ст. викладач" and float(first_semester_info[i][3]) != 0 or str(helper[1]) != "ст. викладач"):
            people[0].counter_first_semester += float(first_semester_info[i][1])
            people[0].total_first_semester += float(first_semester_info[i][3])

        if str(helper[1]) != "асистент" and (str(helper[1]) == "ст. викладач" and float(second_semester_info[i][3]) != 0 or str(helper[1]) != "ст. викладач"):
            people[0].counter_second_semester += float(second_semester_info[i][1])
            people[0].total_second_semester += float(second_semester_info[i][3])

        if str(helper[1]) != "асистент" and ( str(helper[1]) == "ст. викладач" and float(academic_year_info[i][3]) != 0 or str(helper[1]) != "ст. викладач"):
            people[0].counter_academic_year += float(academic_year_info[i][1])
            people[0].total_academic_year += float(academic_year_info[i][3])

        if str(helper[1]) == "заф. кафедри":
            people[1].counter_first_semester+=float(first_semester_info[i][1])
            people[1].counter_second_semester += float(second_semester_info[i][1])
            people[1].counter_academic_year += float(academic_year_info[i][1])

            people[1].total_first_semester+=float(first_semester_info[i][3])
            people[1].total_second_semester+=float(second_semester_info[i][3])
            people[1].total_academic_year+=float(academic_year_info[i][3])

        if  str(helper[1]) == "професор":
            people[2].counter_first_semester += float(first_semester_info[i][1])
            people[2].counter_second_semester += float(second_semester_info[i][1])
            people[2].counter_academic_year += float(academic_year_info[i][1])

            people[2].total_first_semester += float(first_semester_info[i][3])
            people[2].total_second_semester += float(second_semester_info[i][3])
            people[2].total_academic_year += float(academic_year_info[i][3])

        if str(helper[1]) == "доцент":

            people[3].counter_first_semester += float(first_semester_info[i][1])
            people[3].counter_second_semester += float(second_semester_info[i][1])
            people[3].counter_academic_year += float(academic_year_info[i][1])

            people[3].total_first_semester += float(first_semester_info[i][3])
            people[3].total_second_semester += float(second_semester_info[i][3])
            people[3].total_academic_year += float(academic_year_info[i][3])

        if str(helper[1]) == "ст. викладач" and float(first_semester_info[i][3]) != 0:
            people[4].counter_first_semester += float(first_semester_info[i][1])
            people[4].total_first_semester += float(first_semester_info[i][3])

        if str(helper[1]) == "ст. викладач" and float(second_semester_info[i][3]) != 0:
            people[4].counter_second_semester += float(second_semester_info[i][1])
            people[4].total_second_semester += float(second_semester_info[i][3])

        if str(helper[1]) == "ст. викладач" and float(academic_year_info[i][3]) != 0:
            people[4].counter_academic_year += float(academic_year_info[i][1])
            people[4].total_academic_year += float(academic_year_info[i][3])


        if str(helper[1]) == "в.о. заф. кафедри":
            people[5].counter_first_semester += float(first_semester_info[i][1])
            people[5].counter_second_semester += float(second_semester_info[i][1])
            people[5].counter_academic_year += float(academic_year_info[i][1])

            people[5].total_first_semester += float(first_semester_info[i][3])
            people[5].total_second_semester += float(second_semester_info[i][3])
            people[5].total_academic_year += float(academic_year_info[i][3])

        if str(helper[1]) == "викладач":
            people[6].counter_first_semester += float(first_semester_info[i][1])
            people[6].counter_second_semester += float(second_semester_info[i][1])
            people[6].counter_academic_year += float(academic_year_info[i][1])

            people[6].total_first_semester += float(first_semester_info[i][3])
            people[6].total_second_semester += float(second_semester_info[i][3])
            people[6].total_academic_year += float(academic_year_info[i][3])


    for person in people:
        if float(person.total_first_semester) == 0 or float(person.counter_first_semester) == 0:
            person.total_first_semester = 0
        else:
            person.total_first_semester = round(float(person.total_first_semester) / float(person.counter_first_semester),2)

        if float(person.total_second_semester) == 0 or float(person.counter_second_semester) == 0:
            person.total_second_semester = 0
        else:
            person.total_second_semester = round(float(person.total_second_semester) / float(person.counter_second_semester), 2)

        if float(person.total_academic_year) == 0 or float(person.counter_academic_year) == 0:
            person.total_academic_year = 0
        else:
            person.total_academic_year = round(float(person.total_academic_year) / float(person.counter_academic_year), 2)


    with open(path_to_file_txt, "a") as file:
        file.write(f"Середнє лекційне навантаження НПП (заф. кафедри):\n\tперший семестр: {people[1].total_first_semester}\n\tдругий семестр: {people[1].total_second_semester}\n\tрік {people[1].total_academic_year}\n\n")
        file.write(f"Середнє лекційне навантаження НПП (професор):\n\tперший семестр: {people[2].total_first_semester}\n\tдругий семестр: {people[2].total_second_semester}\n\tрік {people[2].total_academic_year}\n\n")
        file.write(f"Середнє лекційне навантаження НПП (доцент):\n\tперший семестр: {people[3].total_first_semester}\n\tдругий семестр: {people[3].total_second_semester}\n\tрік {people[3].total_academic_year}\n\n")
        file.write(f"Середнє лекційне навантаження НПП (ст. викладач, який веде лекції):\n\tперший семестр: {people[4].total_first_semester}\n\tдругий семестр: {people[4].total_second_semester}\n\tрік {people[4].total_academic_year}\n\n")
        file.write(f"Середнє лекційне навантаження НПП (в.о. заф. кафедри):\n\tперший семестр: {people[5].total_first_semester}\n\tдругий семестр: {people[5].total_second_semester}\n\tрік {people[5].total_academic_year}\n\n")
        file.write(f"Середнє лекційне навантаження НПП (викладач):\n\tперший семестр: {people[6].total_first_semester}\n\tдругий семестр: {people[6].total_second_semester}\n\tрік {people[6].total_academic_year}\n\n")
        file.write(f"Середнє лекційне навантаження НПП (всі):\n\tперший семестр: {people[0].total_first_semester}\n\tдругий семестр: {people[0].total_second_semester}\n\tрік {people[0].total_academic_year}\n\n")

    loading.destroy()
    root.deiconify()
    washed_down_main_menu(root, name_db)



def task3(root, name_db):
    root.withdraw()
    loading = loading_window(root)

    conn = sqlite3.connect(name_db)
    cursor = conn.cursor()
    job_info = cursor.execute("SELECT * FROM РОБОЧА_ІНФОРМАЦІЯ").fetchall()
    person_info = cursor.execute("SELECT * FROM ЛЮДСЬКА_ІНФОРМАЦІЯ").fetchall()
    vacancy_info = cursor.execute("SELECT * FROM ІНФОРМАЦІЯ_ВАКАНСІЯ").fetchall()
    first_semester_info = cursor.execute("SELECT * FROM ПЕРШИЙ_СЕМЕСТР").fetchall()
    second_semester_info = cursor.execute("SELECT * FROM ДРУГИЙ_СЕМЕСТР").fetchall()
    academic_year_info = cursor.execute("SELECT * FROM АКАДЕМІЧНИЙ_РІК").fetchall()
    code_and_year_info = cursor.execute("SELECT * FROM КОД_РІК").fetchall()
    conn.close()

    path_to_file_txt = "resources/Середнє аудиторне навантаження НПП/result.txt"

    if os.path.exists(path_to_file_txt):
        os.remove(path_to_file_txt)

    people_l = (Totals(), Totals(), Totals(), Totals(), Totals(), Totals(), Totals())
    i = -1

    for helper in job_info:
        i += 1

        if str(helper[1]) != "асистент" and (
                str(helper[1]) == "ст. викладач" and float(first_semester_info[i][3]) != 0 or str(
                helper[1]) != "ст. викладач"):
            people_l[0].counter_first_semester += float(first_semester_info[i][1])
            people_l[0].total_first_semester += float(first_semester_info[i][3])

        if str(helper[1]) != "асистент" and (
                str(helper[1]) == "ст. викладач" and float(second_semester_info[i][3]) != 0 or str(
                helper[1]) != "ст. викладач"):
            people_l[0].counter_second_semester += float(second_semester_info[i][1])
            people_l[0].total_second_semester += float(second_semester_info[i][3])

        if str(helper[1]) != "асистент" and (
                str(helper[1]) == "ст. викладач" and float(academic_year_info[i][3]) != 0 or str(
                helper[1]) != "ст. викладач"):
            people_l[0].counter_academic_year += float(academic_year_info[i][1])
            people_l[0].total_academic_year += float(academic_year_info[i][3])

        if str(helper[1]) == "заф. кафедри":
            people_l[1].counter_first_semester += float(first_semester_info[i][1])
            people_l[1].counter_second_semester += float(second_semester_info[i][1])
            people_l[1].counter_academic_year += float(academic_year_info[i][1])

            people_l[1].total_first_semester += float(first_semester_info[i][3])
            people_l[1].total_second_semester += float(second_semester_info[i][3])
            people_l[1].total_academic_year += float(academic_year_info[i][3])

        if str(helper[1]) == "професор":
            people_l[2].counter_first_semester += float(first_semester_info[i][1])
            people_l[2].counter_second_semester += float(second_semester_info[i][1])
            people_l[2].counter_academic_year += float(academic_year_info[i][1])

            people_l[2].total_first_semester += float(first_semester_info[i][3])
            people_l[2].total_second_semester += float(second_semester_info[i][3])
            people_l[2].total_academic_year += float(academic_year_info[i][3])

        if str(helper[1]) == "доцент":
            people_l[3].counter_first_semester += float(first_semester_info[i][1])
            people_l[3].counter_second_semester += float(second_semester_info[i][1])
            people_l[3].counter_academic_year += float(academic_year_info[i][1])

            people_l[3].total_first_semester += float(first_semester_info[i][3])
            people_l[3].total_second_semester += float(second_semester_info[i][3])
            people_l[3].total_academic_year += float(academic_year_info[i][3])

        if str(helper[1]) == "ст. викладач" and float(first_semester_info[i][3]) != 0:
            people_l[4].counter_first_semester += float(first_semester_info[i][1])
            people_l[4].total_first_semester += float(first_semester_info[i][3])

        if str(helper[1]) == "ст. викладач" and float(second_semester_info[i][3]) != 0:
            people_l[4].counter_second_semester += float(second_semester_info[i][1])
            people_l[4].total_second_semester += float(second_semester_info[i][3])

        if str(helper[1]) == "ст. викладач" and float(academic_year_info[i][3]) != 0:
            people_l[4].counter_academic_year += float(academic_year_info[i][1])
            people_l[4].total_academic_year += float(academic_year_info[i][3])

        if str(helper[1]) == "в.о. заф. кафедри":
            people_l[5].counter_first_semester += float(first_semester_info[i][1])
            people_l[5].counter_second_semester += float(second_semester_info[i][1])
            people_l[5].counter_academic_year += float(academic_year_info[i][1])

            people_l[5].total_first_semester += float(first_semester_info[i][3])
            people_l[5].total_second_semester += float(second_semester_info[i][3])
            people_l[5].total_academic_year += float(academic_year_info[i][3])

        if str(helper[1]) == "викладач":
            people_l[6].counter_first_semester += float(first_semester_info[i][1])
            people_l[6].counter_second_semester += float(second_semester_info[i][1])
            people_l[6].counter_academic_year += float(academic_year_info[i][1])

            people_l[6].total_first_semester += float(first_semester_info[i][3])
            people_l[6].total_second_semester += float(second_semester_info[i][3])
            people_l[6].total_academic_year += float(academic_year_info[i][3])

    for person in people_l:
        if float(person.total_first_semester) == 0 or float(person.counter_first_semester) == 0:
            person.total_first_semester = 0
        else:
            person.total_first_semester = round(
                float(person.total_first_semester) / float(person.counter_first_semester), 2)

        if float(person.total_second_semester) == 0 or float(person.counter_second_semester) == 0:
            person.total_second_semester = 0
        else:
            person.total_second_semester = round(
                float(person.total_second_semester) / float(person.counter_second_semester), 2)

        if float(person.total_academic_year) == 0 or float(person.counter_academic_year) == 0:
            person.total_academic_year = 0
        else:
            person.total_academic_year = round(float(person.total_academic_year) / float(person.counter_academic_year),
                                               2)


    people = (Totals(), Totals(), Totals(), Totals(), Totals(), Totals(), Totals(), Totals())
    i = -1

    for helper in job_info:
        i += 1

        people[0].counter_first_semester += float(first_semester_info[i][1])
        people[0].counter_second_semester += float(second_semester_info[i][1])
        people[0].counter_academic_year += float(academic_year_info[i][1])

        people[0].total_first_semester += float(first_semester_info[i][4]) + float(first_semester_info[i][5])
        people[0].total_second_semester += float(second_semester_info[i][4]) + float(second_semester_info[i][5])
        people[0].total_academic_year += float(academic_year_info[i][4]) + float(academic_year_info[i][5])

        if str(helper[1]) == "заф. кафедри":
            people[1].counter_first_semester += float(first_semester_info[i][1])
            people[1].counter_second_semester += float(second_semester_info[i][1])
            people[1].counter_academic_year += float(academic_year_info[i][1])

            people[1].total_first_semester += float(first_semester_info[i][4]) + float(first_semester_info[i][5])
            people[1].total_second_semester += float(second_semester_info[i][4]) + float(second_semester_info[i][5])
            people[1].total_academic_year += float(academic_year_info[i][4]) + float(academic_year_info[i][5])

        if str(helper[1]) == "професор":
            people[2].counter_first_semester += float(first_semester_info[i][1])
            people[2].counter_second_semester += float(second_semester_info[i][1])
            people[2].counter_academic_year += float(academic_year_info[i][1])

            people[2].total_first_semester += float(first_semester_info[i][4]) + float(first_semester_info[i][5])
            people[2].total_second_semester += float(second_semester_info[i][4]) + float(second_semester_info[i][5])
            people[2].total_academic_year += float(academic_year_info[i][4]) + float(academic_year_info[i][5])

        if str(helper[1]) == "доцент":
            people[3].counter_first_semester += float(first_semester_info[i][1])
            people[3].counter_second_semester += float(second_semester_info[i][1])
            people[3].counter_academic_year += float(academic_year_info[i][1])

            people[3].total_first_semester += float(first_semester_info[i][4]) + float(first_semester_info[i][5])
            people[3].total_second_semester += float(second_semester_info[i][4]) + float(second_semester_info[i][5])
            people[3].total_academic_year += float(academic_year_info[i][4]) + float(academic_year_info[i][5])

        if str(helper[1]) == "ст. викладач" :
            people[4].counter_first_semester += float(first_semester_info[i][1])
            people[4].counter_second_semester += float(second_semester_info[i][1])
            people[4].counter_academic_year += float(academic_year_info[i][1])

            people[4].total_first_semester += float(first_semester_info[i][4]) + float(first_semester_info[i][5])
            people[4].total_second_semester += float(second_semester_info[i][4]) + float(second_semester_info[i][5])
            people[4].total_academic_year += float(academic_year_info[i][4]) + float(academic_year_info[i][5])

        if str(helper[1]) == "в.о. заф. кафедри":
            people[5].counter_first_semester += float(first_semester_info[i][1])
            people[5].counter_second_semester += float(second_semester_info[i][1])
            people[5].counter_academic_year += float(academic_year_info[i][1])

            people[5].total_first_semester += float(first_semester_info[i][4]) + float(first_semester_info[i][5])
            people[5].total_second_semester += float(second_semester_info[i][4]) + float(second_semester_info[i][5])
            people[5].total_academic_year += float(academic_year_info[i][4]) + float(academic_year_info[i][5])

        if str(helper[1]) == "викладач":
            people[6].counter_first_semester += float(first_semester_info[i][1])
            people[6].counter_second_semester += float(second_semester_info[i][1])
            people[6].counter_academic_year += float(academic_year_info[i][1])

            people[6].total_first_semester += float(first_semester_info[i][4]) + float(first_semester_info[i][5])
            people[6].total_second_semester += float(second_semester_info[i][4]) + float(second_semester_info[i][5])
            people[6].total_academic_year += float(academic_year_info[i][4]) + float(academic_year_info[i][5])

        if str(helper[1]) == "асистент":
            people[7].counter_first_semester += float(first_semester_info[i][1])
            people[7].counter_second_semester += float(second_semester_info[i][1])
            people[7].counter_academic_year += float(academic_year_info[i][1])

            people[7].total_first_semester += float(first_semester_info[i][4]) + float(first_semester_info[i][5])
            people[7].total_second_semester += float(second_semester_info[i][4]) + float(second_semester_info[i][5])
            people[7].total_academic_year += float(academic_year_info[i][4]) + float(academic_year_info[i][5])


    for person in people:
        if float(person.total_first_semester) == 0 or float(person.counter_first_semester) == 0:
            person.total_first_semester = 0
        else:
            person.total_first_semester = round(
                float(person.total_first_semester) / float(person.counter_first_semester), 2)

        if float(person.total_second_semester) == 0 or float(person.counter_second_semester) == 0:
            person.total_second_semester = 0
        else:
            person.total_second_semester = round(
                float(person.total_second_semester) / float(person.counter_second_semester), 2)

        if float(person.total_academic_year) == 0 or float(person.counter_academic_year) == 0:
            person.total_academic_year = 0
        else:
            person.total_academic_year = round(float(person.total_academic_year) / float(person.counter_academic_year),2)

    with open(path_to_file_txt, "a") as file:
        file.write(f"Середнє аудиторне навантаження НПП (заф. кафедри):\n\tперший семестр: {round(people[1].total_first_semester+people_l[1].total_first_semester,2)}\n\tдругий семестр: {round(people[1].total_second_semester+people_l[1].total_second_semester,2)}\n\tрік {round(people[1].total_academic_year+people_l[1].total_academic_year,2)}\n\n")
        file.write(f"Середнє аудиторне навантаження НПП (професор):\n\tперший семестр: {round(people[2].total_first_semester+people_l[2].total_first_semester,2)}\n\tдругий семестр: {round(people[2].total_second_semester+people_l[2].total_second_semester,2)}\n\tрік {round(people[2].total_academic_year+people_l[2].total_academic_year,2)}\n\n")
        file.write(f"Середнє аудиторне навантаження НПП(доцент) :\n\tперший семестр: {round(people[3].total_first_semester+people_l[3].total_first_semester,2)}\n\tдругий семестр: {round(people[3].total_second_semester+people_l[3].total_second_semester,2)}\n\tрік {round(people[3].total_academic_year+people_l[3].total_academic_year,2)}\n\n")
        file.write(f"Середнє аудиторне навантаження НПП (ст. викладач):\n\tперший семестр: {round(people[4].total_first_semester+people_l[4].total_first_semester,2)}\n\tдругий семестр: {round(people[4].total_second_semester+people_l[4].total_second_semester,2)}\n\tрік {round(people[4].total_academic_year+people_l[4].total_academic_year,2)}\n\n")
        file.write(f"Середнє аудиторне навантаження НПП (асистент):\n\tперший семестр: {round(people[7].total_first_semester,2)}\n\tдругий семестр: {round(people[7].total_second_semester,2)}\n\tрік {round(people[7].total_academic_year,2)}\n\n")
        file.write(f"Середнє аудиторне навантаження НПП (в.о. заф. кафедри):\n\tперший семестр: {round(people[5].total_first_semester+people_l[5].total_first_semester,2)}\n\tдругий семестр: {round(people[5].total_second_semester+people_l[5].total_second_semester,2)}\n\tрік {round(people[5].total_academic_year+people_l[5].total_academic_year,2)}\n\n")
        file.write(f"Середнє аудиторне навантаження НПП (викладач):\n\tперший семестр: {round(people[6].total_first_semester+people_l[6].total_first_semester,2)}\n\tдругий семестр: {round(people[6].total_second_semester+people_l[6].total_second_semester,2)}\n\tрік {round(people[6].total_academic_year+people_l[6].total_academic_year,2)}\n\n")
        file.write(f"Середнє аудиторне навантаження НПП (всі):\n\tперший семестр: {round(people[0].total_first_semester+people_l[0].total_first_semester,2)}\n\tдругий семестр: {round(people[0].total_second_semester+people_l[0].total_second_semester,2)}\n\tрік {round(people[0].total_academic_year+people_l[0].total_academic_year,2)}\n\n")


    loading.destroy()
    root.deiconify()
    washed_down_main_menu(root, name_db)

def washed_down_main_menu(root,name_db):
    from error_menu_ import error_menu
    from change_main_menu_button_click_ import change_main_menu_button_click
    from main_menu_ import main_menu
    #from washed_down_main_menu_ import washed_down_main_menu

    root.title("Запити")
    for widget in root.winfo_children():
        widget.destroy()

    change_settings = tk.Button(root, text="Відкрити налаштування", command=lambda: change_main_menu_button_click(root,name_db))
    error_window = tk.Button(root, text="Вікно помилок", command=lambda: error_menu(root,name_db), fg="red")
    main_menu_window = tk.Button(root, text="Головне меню", command=lambda: main_menu(root,name_db))
    washed_down_window = tk.Button(root, text="Запити", command=lambda: washed_down_main_menu(root,name_db))

    root.update()
    change_settings.place(x=10, y=10)
    root.update()
    main_menu_window.place(x=10 + change_settings.winfo_width() + 10, y=10)
    root.update()
    washed_down_window.place(x=10 + change_settings.winfo_width() + 10 + 10 + main_menu_window.winfo_width(), y=10)
    root.update()
    error_window.place(
        x=10 + change_settings.winfo_width() + 10 + 10 + main_menu_window.winfo_width() + 10 + washed_down_window.winfo_width(),
        y=10)
    root.update()

    try:
        conn = sqlite3.connect(name_db)
        cursor = conn.cursor()
        check_info = cursor.execute("SELECT * FROM ПЕРЕВІРКА").fetchall()
        check_info_as_st = cursor.execute("SELECT * FROM ПЕРЕВІРКА_АСИСТЕНТ_СТ_ВИКЛАДАЧ").fetchall()
        conn.close()
        if len(check_info) + len(check_info_as_st) == 0:
            error_window.place(x=-100, y=-100)

    except Exception:
        error_window.place(x=-100, y=-100)

    hints = ["Середнє навантаження НПП","Середнє лекційне навантаження НПП","Середнє аудиторне навантаження НПП"]

    buttons = []

    def clicker(i, root, name_db):
        i = int(i)
        if i==1:
            task1(root, name_db)
        elif i==2:
            task2(root, name_db)
        elif i==3:
            task3(root, name_db)

    for i,hint in enumerate(hints,start=1):
        buttons.append(tk.Button(root, text=hint, command=lambda j=i: clicker(j,root,name_db)))
        root.update()

    empty_height = root.winfo_height()-20-washed_down_window.winfo_height()

    for button in buttons:
        empty_height -= button.winfo_height()

    empty_height /= (len(hints)+2)

    for i,button in enumerate(buttons, start=1):
        button.place(x=(root.winfo_width()-button.winfo_width())/2, y=i*empty_height+(i-1)*(button.winfo_height()))
        root.update()
        button.place(x=(root.winfo_width() - button.winfo_width()) / 2,
                     y=20 + washed_down_window.winfo_height() + i * empty_height + (i - 1) * button.winfo_height()
                     )
        root.update()

