from main import *

while True:
    print('Тип файла:','\n1.Фаил\текст','\n2.JSON формат','\n3.HTML формат','\n0.Exit')
    type = int(input())
    if type == 1:
        print('1.RUS текс \n2.ENG текс')
        type = int(input())
        if type == 1:
            print('RU: \n1.Имя \n2.Email адрес')
            type = int(input())
            if type == 1:
                file = input('Введите путь до файла: ')
                file = file = open_file(file, 'r')
                print('Rus Name:',Russian(file).ru_name())
                break
            elif type == 2:
                file = input('Введите путь до файла: ')
                file = file = open_file(file, 'r')
                print('Emails: ',Email(file).email())
                break
            else:
                print('ERROR, try again')
                continue
        elif type == 2:
            print('EN: \n1.Имя \n2.Email адрес')
            type = int(input())
            if type == 1:
                file = input('Введите путь до файла: ')
                file = file = open_file(file, 'r')
                print('Eng Name:',English(file).eng_name())
                break
            elif type == 2:
                file = input('Введите путь до файла: ')
                file = file = open_file(file, 'r')
                print('Emails: ',Email(file).email())
                break
            else:
                print('ERROR, try again')
                continue
        else:
            print('ERROR, try again')
            continue
    elif type == 2:
        print('JSON')
        break
    elif type == 3:
        print('1.Lenta.ru news \n2.Email с сайтов \n3.Url с сайтов')
        type = int(input())
        if type == 1:
            page = HTML('https://m.lenta.ru/').get_html()
            for news in HTML(page).get_lenta():
                print(news)
            break
        elif type == 2:
            url = input('Введите сайт: ')
            content = HTML(url).get_content()
            print(Email(content).email())
            break
        elif type == 3:
            url = input('Введите сайт: ')
            content = HTML(url).get_content()
            print(HTML(content).get_url())
            break
        else:
            print('ERROR, try again')
            continue
    elif type == 0:
        print('Exit...')
        break
    else:
        print('ERROR, try again')
        continue
