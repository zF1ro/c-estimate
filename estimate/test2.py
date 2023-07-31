# request.POST: <QueryDict: {'csrfmiddlewaretoken': ['UenhDVqfn0RwMsmlVlypJVphYeHvE0KcYwJ6bxq7P1zzEGwYXygMsi30GaLAni0X'], 'work-TOTAL_FORMS': ['
# 3'], 'work-INITIAL_FORMS': ['3'], 'work-MIN_NUM_FORMS': ['0'], 'work-MAX_NUM_FORMS': ['1000'], 'work-0-id': ['104', '104'], 'work-0-title_w':
# ['3.31111'], 'work-0-quantity_w': ['33'], 'work-0-unit_w': ['33'], 'work-0-margin_w': ['33'], 'work-1-id': ['103', '103'], 'work-1-title_w': [
# '3.2 test'], 'work-1-quantity_w': ['32'], 'work-1-unit_w': ['32'], 'work-1-margin_w': ['32'], 'work-2-id': ['102', '102'], 'work-2-title_w': [
# '3.1'], 'work-2-quantity_w': ['31'], 'work-2-unit_w': ['31'], 'work-2-margin_w': ['31']}>
# request.FILES: <MultiValueDict: {}>

###################


# True False
# request.POST: <QueryDict: {'csrfmiddlewaretoken': ['1lrbrCNr1eDSQq4keaTAzqfbine3yTWx5DN0ZeNjtflVIEeXgnBXiNTU0ji8hbci'], 'work104-title_w': ['3.3 11111'], 'work104-quantity_w': ['33'], 'work104-unit_w': ['33'], 'work104-margin_w': ['33'], 'res104-TOTAL_FORMS': ['3'], 'res104-INITIAL_FORMS': ['3'], 'res104-MIN_NUM_FORMS': ['0'], 'res104-MAX_NUM_FORMS': ['1000'], 'res104-0-id': ['50'], 'res104-0-quantity_r': ['33'], 'res104-0-unit_r': ['33'], 'res104-0-unit_cost_r': ['33'], 'res104-1-id': ['49'], 'res104-1-quantity_r': ['33'], 'res104-1-day_cost_r': ['33'], 'res104-2-id': ['48'], 'res104-2-quantity_r': ['33'], 'res104-2-day_cost_r': ['33'], 'work103-title_w': ['3.2 test'], 'work103-quantity_w': ['32'], 'work103-unit_w': ['32'], 'work103-margin_w': ['32'], 'res103-TOTAL_FORMS': ['2'], 'res103-INITIAL_FORMS': ['2'], 'res103-MIN_NUM_FORMS': ['0'], 'res103-MAX_NUM_FORMS': ['1000'], 'res103-0-id': ['52'], 'res103-0-quantity_r': ['32'], 'res103-0-day_cost_r': ['32'], 'res103-1-id': ['51'], 'res103-1-quantity_r': ['32'], 'res103-1-day_cost_r': ['32'], 'work102-title_w': ['3.1'], 'work102-quantity_w': ['31'], 'work102-unit_w': ['31'], 'work102-margin_w': ['31'], 'res102-TOTAL_FORMS': ['3'], 'res102-INITIAL_FORMS': ['3'],'res102-MIN_NUM_FORMS': ['0'], 'res102-MAX_NUM_FORMS': ['1000'], 'res102-0-id': ['55'], 'res102-0-quantity_r': ['31'], 'res102-0-unit_r': ['31'], 'res102-0-unit_cost_r': ['31'], 'res102-1-id': ['54'], 'res102-1-quantity_r': ['31'], 'res102-1-day_cost_r': ['31'], 'res102-2-id': ['53'], 'res102-2-quantity_r': ['31'], 'res102-2-day_cost_r': ['31']}>

# request.FILES: <MultiValueDict: {}>
# ошибка: <ul class="errorlist nonform"><li>Данные ManagementForm отсутствуют или были подделаны. Отсутствующие поля: work-TOTAL_FORMS, work-INI
# TIAL_FORMS. Если проблема не исчезнет, вам может потребоваться отправить отчет об ошибке.</li></ul>

x = [1, 2]
y = [1, 2]

xy = []
for num in range(5):
    xy.append([num, num])

for x, y in xy:
    print(x)
    print(y)

print(xy)
