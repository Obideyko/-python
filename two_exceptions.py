try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print("Было вызвано исключение. {}".format(e.args[-1]))