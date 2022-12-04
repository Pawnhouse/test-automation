import uuid
import actions
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\fields'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\tabs'))
addImagePath(unicd('D:\\ТиВП\\Лабораторные\\lab8\\img\\buttons'))

                                                
region = actions.start()
test_values = ['Two_apps_running_simultaneously', '']
actions.form_work(0, True, test_values);
region.click("save.png")
file_name = str(uuid.uuid4())
type(file_name)
type(Key.ENTER)
region.click("cross-1.png")

for i in range(3):
    doubleClick("app.png")
    wait(1)
    region.click("open.png")
    type(file_name)
    type(Key.ENTER)
    actions.form_work(0, False, test_values)

close = region.find("cross.png")
for i in range(3):
    close.click()
    wait(0.05)

    
