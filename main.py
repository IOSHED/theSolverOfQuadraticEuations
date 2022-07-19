from typing import List


class Program:
    userData = None
    a, b, c = None, None, None
    x1, x2 = None, None

    @staticmethod
    def error():
        print(">>> Вы ввели некорректные данные! ")

    @staticmethod
    def gettingData() -> List[str]:
        return input(">>> Введите, пожалуйста, квадратное уравнение: ").split()

    @staticmethod
    def calculationDiscriminant(a: float, b: float, c: float) -> float:
        return (b * b) - 4 * a * c

    @classmethod
    def parsingValues(cls):
        cls.a = float(cls.userData[0].replace("x^2", ""))

        if cls.userData[1] == "+":
            cls.b = float(cls.userData[2].replace("x", ""))
        if cls.userData[1] == "-":
            cls.b = -(int(cls.userData[2].replace("x", "")))
        else:
            Program.error()

        if cls.userData[3] == "+":
            cls.c = int(cls.userData[4])
        elif cls.userData[3] == "-":
            cls.c = -(int(cls.userData[4]))
        else:
            Program.error()

    @classmethod
    def calculation(cls):
        discriminant = Program.calculationDiscriminant(cls.a, cls.b, cls.c)
        if discriminant > 0:
            cls.x1 = -cls.b - discriminant / 2 * cls.a
            cls.x2 = -cls.b + discriminant / 2 * cls.a
        elif discriminant == 0:
            cls.x1 = -cls.b / 2 * cls.a
        else:
            print(">>> Корней нет! ")

    @classmethod
    def conclusion(cls):
        print(f">>> первый корень: {cls.x1}, второй корень: {cls.x2}! ")

    @classmethod
    def run(cls):
        while True:
            cls.userData = Program.gettingData()
            if len(cls.userData) == 5:
                Program.parsingValues()
                Program.calculation()
                Program.conclusion()
            elif len(cls.userData) == 3:
                pass
            else:
                Program.error()
                continue


if __name__ == "__main__":
    Program.run()
