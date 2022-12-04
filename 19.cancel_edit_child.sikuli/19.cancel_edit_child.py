import actions
from random import randint
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\fields'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\tabs'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\buttons'))
                                                

region = actions.start()
child = ['John', '140', '03072009']
new_child = ['Adam', '150', '12112008']
actions.form_work(3, True, child)
child[2] = '03.07.2009'
region.click("update_child.png")
wait(0.5)

fields = ["name.png","height.png"]
work_region = find("child_fields.png").grow(0, 300, 0, 0)
for i in range(3):
    if randint(0, 1):
        new_child[i] = ''
for j in range(2):
    work_region.find(fields[j]).right(100).doubleClick()
    paste(new_child[j])
work_region.find("calendar.png").left(50).click()
for i in range(8):
    type(Key.BACKSPACE)
paste(new_child[2])

type(Key.ESC)
actions.form_work(3, False, child)

region.click("cross.png")

    
