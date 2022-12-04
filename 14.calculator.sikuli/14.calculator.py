import uuid
from random import randint
import datetime
import actions
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\fields'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\tabs'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\buttons'))
                                                

def get_place(i):
    i = int(i)
    if i == 0:
        return 0, 3
    return (i - 1) % 3, (9 - i) // 3

region = actions.start()
actions.navigate(3)
region.click("add_child.png")
wait(0.5)
child_region = find("child_fields.png").grow(0, 300, 0, 0)
child_region.click("calculator.png")
digits = child_region.find("calculator.png").grow(200, 200, 0, 200).find("calculator_digits.png")

height = str(randint(0, 300))
for i in height:
    col, row = get_place(i)
    print((col, row))
    digits.getRow(row,4).getCol(col,3).highlight(2)   
    digits.getRow(row,4).getCol(col,3).click()
type(Key.ENTER)
type(Key.ENTER)

actions.save_and_open()
actions.form_work(3, False, ['', height, ''])

region.click("cross.png")

    
