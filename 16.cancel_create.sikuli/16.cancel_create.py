import actions
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\fields'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\tabs'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\buttons'))
                                                

region = actions.start()
general = ['Interesting_description', '']
actions.form_work(0, True, general)
region.click("open.png")
wait(0.4)
type(Key.ESC)
actions.form_work(0, False, general)

region.click("cross.png")
    
