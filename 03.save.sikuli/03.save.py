import actions
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\fields'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\tabs'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\buttons'))

region = actions.start()
region.click("field.png")
text_in_field = 'some text'
type(text_in_field)

actions.save_and_open()

if region.find(text_in_field) == -1:
    raise Exception('No saved data:' + text_in_field)
region.click("cross.png")