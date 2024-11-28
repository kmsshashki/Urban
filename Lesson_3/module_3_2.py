def send_email(message, recipient, sender = "university.help@gmail.com"):
    server = ['com', 'ru', 'net']
    if not ('@' in recipient and '@' in sender and recipient.split('.')[-1] in server and sender.split('.')[-1] in server):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender != "university.help@gmail.com":
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru')
    else:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

        
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')