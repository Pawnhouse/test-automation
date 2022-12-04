import uuid
from random import randint
import datetime
import actions
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\fields'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\tabs'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\buttons'))

                                                
region = actions.start()

x = datetime.datetime.now()
birthday = x.replace(year=2000)
date = birthday.strftime('%d%m%Y')
insert_date(region, date)
years_old = x.year - 2000

paste('')
region.find("age.png").right(150).doubleClick()
type('c', Key.CTRL)
actions.paste_from_clipboard()
assert actions.get_copied_text() == str(years_old)

region.click("cross.png")

    
