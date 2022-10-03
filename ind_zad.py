def say_name(name, surname):
        def sname():
            print("Уважаемый " + surname + " " + name + "! Вы делаете работу по замыканиям функций.")

        return sname


print("Введите Имя и фамилию: ")
n, s = input().split()
n1 = say_name (name = n, surname = s)
n1()
