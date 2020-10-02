try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('Было вызвано исключение IOError. {}'.format(e.args[-1]))
