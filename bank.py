import account
import Ssevro


def main():
    rate = int(input("Введите процентную ставку: "))
    money = int(input("Введите сумму: "))
    val = int(input("Укажите код валюты (доллары - 400, евро - 401, кроны - 402, фунты - 403, франки - 404): "))
    period = int(input("Введите период ведения счета в месяцах: "))

    result = account.calculate_income(rate, money, period)
    print("Параметры счета:\n", "Сумма: ", money, "\n", "Ставка: ", rate, "\n", "Период: ", period, "\n",
          "Сумма на счете в конце периода: " , result)
    print



if __name__ == "__main__":
    main()