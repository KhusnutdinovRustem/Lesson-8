# -*- coding: utf-8 -*-

x, y = 10, 29
if x < 0:
    print('Х меньше нуля')
    z = x ** 2 + y
else:
    print('Х больше нуля')
    z = x - y
print('Результат', z)

name = input('Enter your name >>>')
if name == 'Ola':
    opponent = 'Ola'
    print('Hi, Ola!')
else:
    if name == 'Sofi':
        opponent = 'Sofi'
        print('Hi, Sofi!')
    else:
        if name == 'Katy':
            opponent = 'Katy'
            print('Hi, Katy!')
        else:
            opponent = 'anonymous'
            print('Hi, anonymous!')

if x < 0:
    if y > 0:
        z = -x + y
    else:
        z = -x - y
else:
    z = x + y

    if x < 0:
        if y > 0:
            pass
        else:
            print('направо!')
    else:
        print('стой!')

    my_poem = ['Варкалось, хливкие шорьки пырялись по наве', 'И хрюкотали зелюки как мюмзики в мове',
               'О бойся Бармаглота, сын! Он так свирлеп и дик', 'А в глуше рымит исполин - Злопастный Брандашмыг!']

    x = 2
    y = x * x + 1
    is_big = x >= 3000

    x = my_poem[-1]
    print(x)
    my_list = [2, 3, 4, 5, 6, ]

    # noinspection PyRedeclaration
    x, y = 3, 8
    if x == 3:
        print(42)

    if x < 0:
        if y > 0:
            print('налево!')
        else:
            print('направо!')
    else:
        print('стой!')

    count_of_my_pets = 34
    if count_of_my_pets > 10:
        print('I need more space for my pets!')

    my_favorite_pets_and_bird = ['cat', 'wolf', 'ostrich']
    if 'lion' in my_favorite_pets_and_bird:
        print('Wow!')

    MyFavoritePetsAndBirds = ['cat', 'wolf', 'ostrich']

    l1 = 34
    I1 = 43
    if l1 > I1:
        print()
    O1 = 9
    if O1 > 0:
        print()

    ss = ['cat', 'wolf', 'ostrich']
    if 'lion' in ss:
        print('Wow!')
