import actions
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\fields'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\tabs'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\buttons'))
                                                

region = actions.start()
region.click("open.png")
wait(0.4)
paste('empty')
type(Key.ENTER)

empty_fields = [''] * 4
for i in range(3):
    actions.form_work(i, False, empty_fields)
actions.navigate(3)
wait(0.05)
assert region.exists(Pattern("disabled_delete_button.png").exact())
assert region.exists(Pattern("disabled_edit_button.png").exact())

region.click("cross.png")
    
