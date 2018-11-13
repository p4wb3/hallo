# numbList = []
# numbList.append(10)
# print(numbList)
# numbList=[1,2,3,4,5,6,7,8,9,10,1,1,1,1]
# print(numbList)
# print(numbList.count(1))
# print(numbList.extend(1))
# print(("*")*80)

# name = input('podaj imie : ')
# age = input('podaj wiek :')
# copies = input('how many copies:')
# copies = int(copies)
#
# print(('twoje imie: ' + name  +' twoj wiek : '+ age+'\n')*copies)

# print(("*")*80)

# num= input('give number: ')
# try:
#     num = int(num)
#     if num % 2 == 0:
#         print('number ' + str(num) + ' you give is even')
#     elif num % 2 != 0:
#         print('number' + str(num) + ' you give is not even')
# except ValueError:
#     print('the value ypu give is not a number')
# print(("*")*80)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# newList= []
# numb= input('Give number : ')
# newlist = []
#
# try:
#     numb = int(numb)
#     [newlist.append(x) for x in a if x < numb]
#     print(newlist)
# except ValueError:
#     print('this is not a number')

# for i in a:
#     if i < 5:
#         newList.append(i)
# print(newList)

# print(("*")*80)

# numb = input('give number: ')
# divList= []
# try:
#     numb = int(numb)
#     for i in range(2,numb+1):
#         if numb % i == 0:
#             divList.append(i)
#     print(divList)
# except ValueError:
#     print('bad input')

# print(("*")*80)


# newList=[]
# firstList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# secondList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# import random
#
# firstList.extend(secondList)
# newList = list(set(firstList))
# newList.sort()
# print(newList)
# import random
# import timeit
#
# # Random lists from [0-999] interval
# randomList = [random.randint(0, 100) for r in range(10)]
# randomList.sort()
# newList.extend(randomList)
# randomList=list(set(newList))
# print(randomList)
# print(("*")*80)

'''
metoda która przyjmie dwie listy  liczb od uzytkownika i zwroci połączoną z:
niepowtarzającynmi sie elementami 
'''
# inputList1 = input('podaj pięć liczb : ')
# list1 = inputList1.split(" ")
# inputList2 = input('podaj pięć liczb : ')
# list2 = inputList2.split(" ")
# try:
#     list1 = [int(i) for i in list1]
#     list2 = [int(i) for i in list2]
# except ValueError:
#     print("to many spaces or wrong type of value")
#     raise
#
# def noDuplicateList(list1,list2):
#     list1.extend(list2)
#     UniqelistElement = list(set(list1))
#     print("list after marging same element: ", UniqelistElement)
#
#
# def showDuplicates(list1,list2):
#     listOfDuplicate = []
#     list1.extend(list2)
#     for i in list1:
#        if list1.count(i)>1:
#             listOfDuplicate.append(i)
#     listOfDuplicate= list(set(listOfDuplicate))
#     listOfDuplicate.sort()
#     print(listOfDuplicate)
#
#
# showDuplicates(list1,list2)

# noDuplicateList(list1, list2)

# normalText = input('Give palindrome text : ')
#
# palindromeText = normalText[::-1]
#
# if palindromeText == normalText:
#     print("{} = {}".format(normalText,palindromeText))
# else:
#     print("{} != {}".format(normalText, palindromeText))

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# newList = [x for x in a if x%2==0 ]
#
# print(newList)
# import random
# a=[]
# for x in range(10):
#     a.append(random.randint(1, 101))
#     b = [x for x in a if x%2==0 ]
#
# print('Wylosowana lista to : {} \nliczby parzyste listy to {}'.format(a,b))

#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock



# while True:
#     # optionList = {'Rock': 1, 'Scissors': 2, 'Paper': 3}
#     p1answer = int(input('Hit 1 2 3 option:\n1.Rock\n2.Scissors\n3.Paper\n:'))
#     p2answer = int(input('Hit 1 2 3 option:\n1.Rock\n2.Scissors\n3.Paper\n:'))
#     # a = (optionList.get(p1answer))
#     # b = (optionList.get(p2answer))
#     # result = a - b
#     result = p1answer-p2answer
#     if [p1answer,p2answer] in [1, 2, 3]:
#
#             if result in [-1,2]:
#                 print('Player 1 Wins!!!!!!!!!!')
#                 if input("do you want to play another game:y//n:\n")=='y':
#                     continue
#                 else:
#                     print('game over')
#                     break
#
#             elif result in [-2,1]:
#                 print('player 2 win!!!')
#                 if input("do you want to play another game:y//n:\n")=='y':
#                     continue
#                 else:
#                     print('game over')
#                     break
#     else:
#         print('wrong input')
#         break
#
# print(("*")*80)
# import random
# ranNumb= random.randint(1,10)
# print(ranNumb)
# x=0
#
#
# while True:
#
#     playerNumb = (input('podaj cyfre:'))
#
#     try:
#         playerNumb= int(playerNumb)
#         x = x + 1
#     except ValueError:
#         continue
#
#
#
#     if playerNumb != ranNumb:
#
#         if playerNumb <ranNumb:
#             print('liczba jest zamała')
#
#             continue
#         elif playerNumb> ranNumb:
#             print('liczba jest za duża')
#             continue
#
#     else:
#
#         print('you win \nliczba prób:'+ str(x))
#         break
# print(("*")*80)
