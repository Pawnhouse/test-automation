from sikuli import *
import uuid

def start():
    doubleClick("app.png")
    wait(1)
    region = find("head.png")
    region = region.grow(5, 5, 0, 220)
    region.click("create.png")
    return region


def main_region():
    region = find("head.png")
    region = region.grow(5, 5, 0, 220)
    return region

def save_and_open():
    region = main_region()
    region.click("save.png")
    file_name = str(uuid.uuid4())
    wait(0.3)
    paste(file_name)
    type(Key.ENTER)
    region.click("cross.png")
    
    doubleClick("app.png")
    wait(1)
    region.click("open.png")
    wait(0.3)
    paste(file_name)
    type(Key.ENTER)


def insert_date(region, date):
    region.find("calendar.png").left(50).click()
    for i in range(8):
        type(Key.LEFT)
    type(str(date))


def paste_from_clipboard():
    click("copy_file.png")
    type('v', Key.CTRL)
    paste('')
    type('s', Key.CTRL)


def get_copied_text():
    wait(0.1)
    f = open('copied_text.txt', 'r')
    text = f.read()
    f.close()
    click("copy_file.png")
    type('a', Key.CTRL)
    type(Key.BACKSPACE)
    type('s', Key.CTRL)
    return text


def navigate(i):
    navigation = ["General.png", "Husband.png", "Wife.png", "Children.png"]
    region = main_region()
    region.click(navigation[i])

def form_work(i, is_input, values):
    paste('')  
    fields = [
        ["description.png"],
        ["first_name.png","middle_name.png","last_name.png"],
        ["first_name.png","middle_name.png","last_name.png"],
        ["name.png","height.png"]
    ]
    wait(0.5)
    region = main_region()
    work_region = region
    navigate(i)
    wait(0.2)
    if i == 3:
        if is_input:
            region.click("add_child.png")
        else:
            region.click("update_child.png")
        wait(0.7)
        work_region = find("child_fields.png").grow(0, 300, 0, 0)
    
    for j in range(len(fields[i])):
        if is_input:
            work_region.find(fields[i][j]).right(100).click()
            paste(values[j])
        else:
            work_region.find(fields[i][j]).right(100).doubleClick()
            type('c', Key.CTRL)
            paste_from_clipboard()
            
    if is_input:
        insert_date(work_region, values[-1])
    else:
        work_region.find("calendar.png").left(50).doubleClick()
        type('c', Key.CTRL)
        paste_from_clipboard()
    if i == 3:
        work_region.find("calendar.png").left(50).click()
        type(Key.ENTER)
    if not is_input:
        text_values = get_copied_text().replace('.    ', '')
        #print text_values
        #print ''.join(values)
        assert text_values == ''.join(values)
            


