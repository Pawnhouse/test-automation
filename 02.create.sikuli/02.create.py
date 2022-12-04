import actions
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\fields'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\tabs'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\buttons'))


region = actions.start()
fields = ["general_fields.png","Parent_fields.png","Parent_fields.png","Children_fields.png"]
for i in range(4):
    actions.navigate(i)
    if not region.exists(fields[i]):
        raise Exception('No fields')
region.click("cross.png")
