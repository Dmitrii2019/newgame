#__author__ = 'Гродзинский Дмитрий Александрович'

print('Добро пожаловать в Python_geme !!!')
alphabet = 'абвгдеёжзийклмнопрстуФхцчшщъыьэюя'

name = input('Видитите свое Имя: ')
age = int(input('Сколько Вам лет: '))
floor = input('Укажите Ваш пол: ')
pets_name = input('Как зовут Вашего питмца: ')
answer = int(input('любите играть в игры ? Да ведите 1 Нет ведите 0: '))

if answer:
     if age >= 18:
         print('Можно начинать игру', name)
         if age >= 90:
              print('Но в вашем возрасте игра для Вас может быть утомительной')
              answer = int(input('Вы уверены что хотите играть,если Да ведите 1 если Нет ведите 0: '))
              if answer:
                  answer = int(input('да у нас перестраховывается игра, будим играть ? Да ведите 1 Нет ведите 0: '))
                  if answer:
                      print('Хорошо тогда начнем игру')
                      print('Я могу назвать буквы алфавита, которых нет в твоем имени')
                      for i in alphabet:
                          if not i in name:
                              print(i)
                      print('Игра окончена')
                  else:
                      print('Досвидание', name)
              else:
                  print('Досвидание', name)
         else:
             print('Я могу назвать буквы алфавита, которых нет в твоем имени')
             for i in alphabet:
                 if not i in name:
                     print(i)
             print('Игра окончена')
     else:
         print(name,'игра предназначена для лиц достигших 18 лет')
else:
    print('Игра окончена', name)

