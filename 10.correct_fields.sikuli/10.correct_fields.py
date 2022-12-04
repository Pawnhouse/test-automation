import uuid
from random import randint
import datetime
import actions
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\fields'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\tabs'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\buttons'))
                                                

region = actions.start()
count = [1, 3, 3, 1]

x = datetime.datetime.now()
date = x.strftime('%d%m%Y')
str_date = x.strftime('%d.%m.%Y')
description = ''
if randint(0, 1):
    description = 'a' * 50
actions.form_work(0, True, ['', date])
values = [['', str_date]]

for i in range(1, 4):
    new_values = []
    for j in range(count[i]):
        names = ['a', 'Text', 'Name', 'Long_name', '']
        name = names[randint(0, 4)]
        new_values.append(name)
    if i == 3:
        names = ['0', '300', '']
        name = names[randint(0, 2)]
        new_values.append(name)
    insert, str_insert = date, str_date
    if randint(0, 1):
        insert, str_insert = '', ''
    new_values.append(insert)
    actions.form_work(i, True, new_values)
    new_values[-1] = str_insert
    values.append(new_values)

actions.save_and_open()
for i in range(4):
    actions.form_work(i, False, values[i])
region.click("cross.png")

    
