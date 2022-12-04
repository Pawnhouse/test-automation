import actions
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\fields'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\tabs'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\buttons'))
                                                

region = actions.start()
region.click("open.png")
wait(0.4)
paste('broken')
type(Key.ENTER)

wait(0.2)
assert exists(Pattern("file_error.png").exact())

type(Key.ENTER)
region.click("cross.png")
    
