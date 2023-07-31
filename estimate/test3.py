
courses = []
for x in range(1):
    courses.append("Java-разработчик с нуля")
    courses.append("Fullstack-разработчик на Python")
    courses.append("Python-разработчик с нуля")
    courses.append("Frontend-разработчик с нуля")

mentors = []
for x in range(1):
    mentors.append(["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"])
    mentors.append(["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"])
    mentors.append(["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"])
    mentors.append(["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"])


def get_key(uniq_names, value):
    for k, v in uniq_names.items():
        if v == value:
            return k


courses_list = []
for course, mentor in zip(courses, mentors):
    course_dict = {"title": course, "mentors": mentor}
    courses_list.append(course_dict)

for course_numb, course in enumerate(courses_list):
    names_list = []
    same_name_list = []
    print(course["mentors"])
    for names in course["mentors"]:
        names_list.append(names.split(' ')[0])
    # print(f'На курсе {course["title"]} есть тёзки: ', end='')
    for numb, name in enumerate(names_list):
        if names_list.count(name) > 1:
            same_name_list.append(courses_list[course_numb]["mentors"][numb])
    same_name_list.sort()
    # print(*same_name_list, sep=', ')  # Это вы мне? Подсчитываем тёзок на каждом курсе

