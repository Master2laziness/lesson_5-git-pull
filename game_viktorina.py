import random

def inicilization_program():

    print('Викторина! Чтобы победить напиши года рождения пяти известных людей и не только!')
    status = bool(False)

    list_data_of_born_names =['ВВ Путин', 'БН Ельцин', 'ДJ Трамп', 'АГ Лукашенко', 'МС Леонов', 'год 2000',
                              'год 2005', 'год 2010', 'год 2015', 'год 2020']
    list_data_of_born_days = ['07.10.1952', '01.02.1931', '14.06.1946', '30.08.1954', '29.01.1994', '01.01.2000',
                              '01.01.2005', '01.01.2010', '01.01.2015', '01.01.2020']
    list_transcriptions_days = ['', 'первое', 'второе', 'третье', 'четвёртое', 'пятое', 'шестое', 'седьмое',
                                'восьмое', 'девятое', 'десятое', 'одинадцаое', 'двенадцатое', 'тринадцатое',
                                'четырнадетоеое', '15-ое', '16-ое', '17-ое', '18-ое', '19-ое', '20-ое',
                                '21-ое', '22-ое', '23-ие', '24-ое', '25-ое', '26-ое', '27-ое', '28-ое',
                                'двадцать девятое', 'тридцатое', '31-ое',]
    list_transcriptions_month =['', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                                'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

    numbers_of_question = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    randomresult = random.sample(numbers_of_question, 5)
    # print(type(randomresult))
    print('Номера билетов с вопросами: ' + str(randomresult))

    score = int(0)
    while status != True:
        for i in randomresult: # range(1, 5):
            birthday_date = str(input('Пожалуйста, напишите дату рождения когда родился ' + str(list_data_of_born_names[i]) + ': '))
            if list_data_of_born_days[i] == birthday_date:
                score += 1
            elif list_data_of_born_days[i] != birthday_date:
                # Формирую список из трёх числовых элементов: день, месяц, год
                convert_to_translate_date = list_data_of_born_days[i].split('.')
                print('Правильный ответ: ' + list_transcriptions_days[int(convert_to_translate_date[0])] + ' ' +
                    list_transcriptions_month[int(convert_to_translate_date[1])] + ' ' + (convert_to_translate_date[2]))

        print('Количество правильных ответов', score)
        print('Количество неправильных ответов', 5-score)
        print('Процент правильных ответов', score*100/5)
        print('Процент неправильных ответов', (5-score)*100/5)
        answer_user = str(input('Пожалуйста, ответьте, если вы хотите продолжить викторину, напишите - да, чтобы завершить - нет. '))
        if answer_user == 'да':
            score = 0
            status = False
        elif answer_user == 'нет':
            score = 0
            status = True
            print('Викторина окончена:)')