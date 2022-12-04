import actions

addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\fields'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\tabs'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\buttons'))
                                                

region = actions.start()
child = ['', '', '']
for i in range(10):
    actions.form_work(3, True, child)

exists(Pattern("top_scroll_button.png").exact())
exists(Pattern("bottom_scroll_button.png").exact())
region.click("cross.png")

    
