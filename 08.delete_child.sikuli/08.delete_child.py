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

region.click("delete_child.png")
wait(0.2)
type(Key.ENTER)
wait(0.5)
assert region.exists(Pattern("disabled_delete_button.png").exact())
assert region.exists(Pattern("disabled_edit_button.png").exact())
region.click("cross.png")

    
