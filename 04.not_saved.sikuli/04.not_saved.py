import uuid
from random import randint
import actions
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\fields'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\tabs'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\buttons'))

region = actions.start()
region.click("field.png")
text_in_field = 'some text'
type(text_in_field)

isCreate = randint(0, 1)
if isCreate:
    region.click("create.png")
else:
    region.click("open.png")

if text().find('unsaved') == -1 and text().find('Unsaved') == -1 :
    raise Exception('No notification about unsaved changes')
type(Key.ESC)
region.click("cross.png")
