usd = 57
euro = 60
czk = 27
gbp = 78
сhf = 60

money = int(input("Введите сумму, которую вы хотите обменять: "))
currency = int(input("Укажите код валюты (доллары - 400, евро - 401, кроны - 402, фунты - 403, франки - 404): "))

if currency == 400:
    cache = round(money / usd, 2)
    print("Валюта: доллары США")
elif currency == 401:
    cache = round(money / euro, 2)
    print("Валюта: евро")
elif currency == 402:
    cache = round(money / czk, 2)
    print("Валюта: кроны")
elif currency == 403:
    cache = round(money / gbp, 2)
    print("Валюта: фунты")
elif currency == 404:
    cache = round(money / euro, 2)
    print("Валюта: франки")
else:
    cache = 0
    print("Неизвестная валюта")

print("К получению:", cache)