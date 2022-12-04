import actions
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\fields'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\tabs'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\buttons'))
                                                

region = actions.start()
actions.navigate(3)
region.click("add_child.png")
wait(0.4)
type(Key.ESC)
assert region.exists(Pattern("disabled_delete_button.png").exact())
assert region.exists(Pattern("disabled_edit_button.png").exact())

region.click("cross.png")

    
