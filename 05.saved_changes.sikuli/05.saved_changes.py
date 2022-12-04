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

region.click("save.png")
file_name = str(uuid.uuid4())
type(file_name)
type(Key.ENTER)


isCreate = randint(0, 1)
if isCreate:
    region.click("create.png")
else:
    region.click("open.png")

text = text()
if text.find('unsaved') == -1 and text.find('Unsaved') == -1 :
    type(Key.ESC)
    region.click("cross.png")
else:
    raise Exception('notification should not appear')
    
