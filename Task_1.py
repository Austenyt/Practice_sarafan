def main():
    while True:
        try:
            n = int(input('Введите цифру от 1 до 9: '))
            if 1 <= n <= 9:
                result = ''.join(str(i) * i for i in range(1, n + 1))
                print(result)
                break
            else:
                print('Число должно быть в диапазоне от 1 до 9.')
        except ValueError:
            print('Пожалуйста, введите целое число.')


if __name__ == '__main__':
    main()
