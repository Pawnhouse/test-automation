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
x = datetime.datetime(randint(2000, 2020), 1, 1)
date = x.strftime('%d%m%Y')
str_date = x.strftime('%d.%m.%Y')

start_values = []
start_values.append(str(uuid.uuid4()).replace('-', '_'))
start_values.append(str(randint(0, 300)))
new_values.append('')
actions.form_work(3, True, new_values)

region.click("update_child.png")
wait(0.7)
work_region = find("child_fields.png").grow(0, 300, 0, 0)
labels = ["name.png", "height.png"]
new_values = [
    str(uuid.uuid4()).replace('-', '_'),
    str(randint(0, 300)),
    str_date
]

for i in range(2):
    work_region.find(labels[i]).right(100).doubleClick()
    type(Key.BACKSPACE)
    paste(new_values[i])
work_region.find("calendar.png").left(50).click()
for i in range(8):
    type(Key.BACKSPACE)
type(date)
type(Key.ENTER)

actions.form_work(3, False, new_values)
region.click("cross.png")

    
