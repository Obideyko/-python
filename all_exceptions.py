try:
    file = open('test.txt', 'rb')
except Exception:
    # Логирование, если оно вам требуется
    raise