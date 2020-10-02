try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('Было вызвано исключение IOError. {}'.format(e.args[-1]))
finally:
    print("Я буду напечатан вне зависимости от исключений в блоке try!")

# Вывод: Было вызвано исключение IOError. No such file or directory
#        Я буду напечатан вне зависимости от исключений в блоке try!