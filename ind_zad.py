if __name__ == '__main__':


    def say_name(name, surname):


        def sname():
            print("Уважаемый " + surname + " "
                + name + "! Вы делаете работу по замыканиям функций.")

        return sname


    print("Введите Имя и фамилию: ")
    name, surname = input().split()
    n = say_name (name, surname)
    n()
