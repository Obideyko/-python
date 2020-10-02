try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("Было вызвано исключение EOFError.")
    raise e
except IOError as e:
    print("Было вызвано исключение IOError.")
    raise e