# Написать программу выполняющую операции(сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (все выражение вводится целиком в виде строки)
# Вывод: 1 17/42 (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3 FIXME(complete): вместо 1/3 было 2/3. Правильно-1/3
# Баллы: 20 - 50 (в зависимости от качества кода)

class A_div_B:
    def __init__(self, st):
        self.int = 0
        self.a = 0
        self.b = 1
        self.x_init(st)

    def x_init(self, st):
        """
        :param st: строка с дробью вида "int a/b" или "a/b"
        """
        # Раскидывает строку по параметрам дроби. Неудобно было делать это в __init__
        if not st:
            # Нулевая дробь
            return
        if ' ' in st:
            # Случай, когда дробь вида k a/b
            self.int = int(st.split(' ')[0])
            self.a = int(st[st.find(' ')+1:st.find('/')])
            self.b = int(st[st.find('/')+1:])
        elif '/' in st:
            # a/b
            self.a = int(st[:st.find('/')])
            self.b = int(st[st.find('/')+1:])
        else:
            # k
            self.int = int(st)
        if self.b == 0:
            return 1/0

    def __add__(self, other):
        # //Моих знаний английского не хватило на это. Поэтому транслит.
        # Сложение дробей.
        # Приводим дроби к виду a/b
        chisl_1 = self.a + self.int * self.b
        znam_1 = self.b
        chisl_2 = other.a + other.b * other.int
        znam_2 = other.b
        # Присваемаем x нулевую дробь
        x = A_div_B('')
        if znam_1 == znam_2:
            x.a = chisl_1 + chisl_2
            x.b = znam_2
            x.int = int(x.a / x.b)
            if (x.b < 0) and (x.a > 0):
                # Без этого if остаток от деления будет работать не всегда
                x.b *= -1
                x.a %= x.b
                x.a *= -1
            elif (x.b > 0) and (x.a < 0):
                x.a = (x.a * -1) % x.b if x.int else ((x.a * -1) % x.b)*-1
            else:
                x.a %= x.b
            nod_x = nod(x.a if x.a > 0 else -x.a, x.b)
            x.a = int(x.a / nod_x)
            x.b = int(x.b / nod_x)
        else:
            x.b = znam_2 * znam_1
            x.a = chisl_1 * znam_2 + chisl_2 * znam_1
            x.int = int(x.a / x.b)
            if (x.b < 0) and (x.a > 0):
                # Без этого if остаток от деления будет работать не всегда
                x.b *= -1
                x.a %= x.b
                x.a *= -1
            elif (x.b > 0) and (x.a < 0):
                x.a = (x.a * -1) % x.b if x.int else ((x.a * -1) % x.b)*-1
            else:
                x.a %= x.b
            nod_x = nod(x.a if x.a > 0 else -x.a, x.b)
            x.a = int(x.a / nod_x)
            x.b = int(x.b / nod_x)
        return x

    def __sub__(self, other):
        # Вычитание. Домножаем дробь на -1
        other.int *= -1
        other.a *= -1 if not other.int else other.a
        return self+other

    def __str__(self):
        # Красота требует жертв.
        return '%s %s/%s' % (self.int, self.a, self.b) if self.int and self.a else '%s/%s' % (self.a, self.b) if self.a \
            else str(self.int) if self.int else '0'


def nod(a, b):
    # НОД для целых a и б
    a, b = b, a
    if b == 0:
        return a
    if a == 0:
        return 1/0
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


expression = input('Введите выражение в формате "k a/b + k1 a1/a2" или "k + k" или "a/b + a1/b1"\n: ')
# Задаём дроби в строках
expression = expression.partition(' + ') if ' + ' in expression else expression.partition(' - ')
dr1, expression, dr2 = expression
# Преобразуем строковые дроби в класс
dr1 = A_div_B(dr1)
dr2 = A_div_B(dr2)
# Выполняем
print(eval('dr1%sdr2' % expression))
