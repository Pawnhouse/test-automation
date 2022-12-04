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
values = []
x = datetime.datetime.now()
date = x.strftime('%d%m%Y')
str_date = x.strftime('%d.%m.%Y')

for i in range(4):
    new_values = []
    for j in range(count[i]):
        new_values.append(str(uuid.uuid4()).replace('-', '_'))
    if i == 3:
        new_values.append(str(randint(0, 300)))
    new_values.append(date)
    actions.form_work(i, True, new_values)
    new_values[-1] = str_date
    values.append(new_values)

actions.save_and_open()
for i in range(4):
    actions.form_work(i, False, values[i])
region.click("cross.png")

    
