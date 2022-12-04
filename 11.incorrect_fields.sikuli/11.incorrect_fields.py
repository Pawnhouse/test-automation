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
incorrect_dates = [
    ['abcdYYYY', 'ab.cd.YYYY'], 
    ['32012022', '32.01.2022'], 
    ['00012022', '00.01.2022']
]
values = []
names = ['-10', 'afs', '301', '1.1', '*']
name = names[randint(0, 4)]
        
for i in range(4):
    date, str_date = incorrect_dates[randint(0, 2)]
    new_values = []
    for j in range(count[i]):
        new_values.append('')
    if i == 3:

        new_values.append(name)
    new_values.append(date)
    actions.form_work(i, True, new_values)
    new_values[-1] = str_date
    values.append(new_values)

actions.save_and_open()
navigation = ["General.png","Husband.png","Wife.png","Children.png"]
for i in range(3):
    region.click(navigation[i])
    region.find("calendar.png").left(50).doubleClick()
    type('c', Key.CTRL)
    actions.paste_from_clipboard()

region.click(navigation[3])
region.click("update_child.png")
wait(0.7)
child_region = find("child_fields.png").grow(0, 300, 0, 0)
child_region.find("calendar.png").left(50).doubleClick()
type('c', Key.CTRL)
actions.paste_from_clipboard()
child_region.find("height.png").right(100).doubleClick()
type('c', Key.CTRL)
actions.paste_from_clipboard()

child_region.click()
type(Key.ENTER)
text = actions.get_copied_text()
assert text.find(name) == -1
for i in range(4):
    assert text.find(values[i][-1]) == -1
region.click("cross.png")

    
