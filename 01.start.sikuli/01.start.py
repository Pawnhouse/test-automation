addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\fields'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\tabs'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\buttons'))


doubleClick("app.png")
wait(1)
region = find("head.png")
region = region.grow(5, 5, 0, 220)
text = region.text()
tabs_names = ['General', 'Husband', 'Wife', 'Children']
for name in tabs_names:
    if text.find(name) == -1:
        raise Exception('No expected tab: ' + name)
if not exists("general_fields.png"):
    raise Exception('No default fields')
region.click("cross.png")
