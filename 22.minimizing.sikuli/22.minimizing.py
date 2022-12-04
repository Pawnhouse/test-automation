import uuid
import actions
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\fields'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\tabs'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\buttons'))

if not has("taskbar_button.png"):                                               
    region = actions.start()
    test_values = ['App_minimizing', '']
    actions.form_work(0, True, test_values)
    region.click("minimize_button.png")
    click("taskbar_button.png")
    wait(0.5)
    actions.form_work(0, False, test_values)
    region.click("cross.png")
else:
    print('Close app before running the test')