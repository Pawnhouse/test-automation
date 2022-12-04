import actions
import uuid
import os
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\fields'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\tabs'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\buttons'))
                                                
file_name = str(uuid.uuid4())
region = actions.start()
region.click("save.png")
wait(0.3)
paste(file_name)
type(Key.ENTER)
region.click("cross.png")

region = actions.start()
region.click("save.png")
wait(0.3)
paste(file_name)
type(Key.ENTER)

exists(Pattern("override_message.png").exact())
type(Key.ESC)
assert os.path.exists('family files/' + file_name + '.cds')

region.click("cross.png")

    
