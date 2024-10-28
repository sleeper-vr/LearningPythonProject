def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    validation_list = [".com",".ru",".net",]
    valid_recipient = False
    valid_sender = False
    for valid in validation_list:
        if sender.endswith(valid):
            valid_sender = True
        if recipient.endswith(valid):
            valid_recipient = True
    if not '@' in recipient:
        valid_recipient = False
    if not '@' in sender:
        valid_sender = False
    if not valid_recipient or not valid_sender:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return 1

    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return 2

    if sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
        return 3
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')