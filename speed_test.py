import time
from decimal import Decimal

##################
# Данные для работы кода
courses = []
for x in range(1000):
    courses.append("Java-разработчик с нуля")
    courses.append("Fullstack-разработчик на Python")
    courses.append("Python-разработчик с нуля")
    courses.append("Frontend-разработчик с нуля")

mentors = []
for x in range(1000):
    mentors.append(["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"])
    mentors.append(["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"])
    mentors.append(["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"])
    mentors.append(["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"])
##################

diff_all_2 = 0
diff_all_1 = 0
x_tic = 10
s_time = 0.00001
tic_number = 100

for x in range(x_tic):
    #####################

    diff_1 = 0
    diff_2 = 0

    for x in range(tic_number):
        if __name__ == '__main__':
            start = time.perf_counter()
            time.sleep(s_time)

            #############
            # Тестовый код № 1.
            courses_list = []
            for course, mentor in zip(courses, mentors):
                course_dict = {"title": course, "mentors": mentor}
                courses_list.append(course_dict)

            for course_numb, course in enumerate(courses_list):
                names_list = []
                same_name_list = []
                for names in course["mentors"]:
                    names_list.append(names.split(' ')[0])
                # print(f'На курсе {course["title"]} есть тёзки: ', end='')
                for numb, name in enumerate(names_list):
                    if names_list.count(name) > 1:
                        same_name_list.append(courses_list[course_numb]["mentors"][numb])
                same_name_list.sort()
                # print(*same_name_list, sep=', ')  # Это вы мне? Подсчитываем тёзок на каждом курсе
            #############

            end = time.perf_counter()
            diff_now = end - start
            diff_1 += diff_now

    # print(f'Среднее время Первого кода, за {tic_number} циклов {average_1}')

    for x in range(tic_number):
        if __name__ == '__main__':
            start = time.perf_counter()
            time.sleep(s_time)

            #############
            # Тестовый код № 2.
            def get_key(uniq_names, value):
                for k, v in uniq_names.items():
                    if v == value:
                        return k


            for m_list_id, m_list in enumerate(mentors):
                uniq_names = {}
                namesake = []
                for m_id, full_name in enumerate(m_list):
                    name = full_name.split(' ')[0]
                    if name not in uniq_names.values():
                        uniq_names[m_id] = name
                    else:
                        namesake.append(m_list[m_id])

                        key = get_key(uniq_names, name)
                        if m_list[key] not in namesake:
                            namesake.append(m_list[key])
                # namesake.sort()
            # print(f'На курсе {courses[m_list_id]} есть тёзки:', end=' ')
            # print(*sorted(namesake), sep=', ')
            #############

            end = time.perf_counter()
            diff_now = end - start
            diff_2 += diff_now

    average_1 = Decimal(diff_1 / tic_number)
    average_2 = Decimal(diff_2 / tic_number)
    # print(f'Среднее время Второго кода, за {tic_number} циклов {average_2}')
    diff_all_2 += average_2
    diff_all_1 += average_1
    if average_1 > average_2:
        print('Код № 2 Победил! Разница:', round(average_2, 10))
    else:
        print('Код № 1 Победил! Разница:', round(average_1, 10))
    ################################

average_all_1 = Decimal(diff_all_1 / x_tic)
average_all_2 = Decimal(diff_all_2 / x_tic)


if average_all_1 > average_all_2:
    diff_all_1_2 = Decimal(average_all_1 - average_all_2)
    print('Итог!!!\nКод № 2 Победил! Разница:', round(diff_all_1_2, 10))
else:
    diff_all_2_1 = Decimal(average_all_2 - average_all_1)
    print(f'Итог!!!\nКод № 1 Победил! Средняя разница за {x_tic} сравнений:', round(diff_all_2_1, 10))



