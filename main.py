# Лабораторна робота №3, варіант 5
# Функція: вартість передавання даних. Якщо обсяг більший за ліміт - інший тариф.
# Lambda: переведення мегабайтів у кілобайти.


def transfer_cost(volume, price, limit, price_over_limit):
    """Повертає вартість передавання volume МБ.

    Якщо volume не більший за limit - ціна price за 1 МБ,
    інакше увесь обсяг рахується за ціною price_over_limit.
    """
    if volume > limit:
        return volume * price_over_limit
    return volume * price


mb_to_kb = lambda mb: mb * 1024   # 1 МБ = 1024 КБ

try:
    price = float(input("Ціна 1 МБ, грн: ").replace(",", "."))
    limit = float(input("Ліміт обсягу, МБ: ").replace(",", "."))
    price_over_limit = float(input("Ціна 1 МБ понад ліміт, грн: ").replace(",", "."))

    if price < 0 or limit < 0 or price_over_limit < 0:
        print("Помилка: значення не можуть бути від'ємними")
    else:
        print("\nОбсяг, МБ | Обсяг, КБ | Вартість, грн")
        for volume in range(10, 101, 10):   # діапазон 10..100 з кроком 10
            cost = transfer_cost(volume, price, limit, price_over_limit)
            print(f"{volume:9} | {mb_to_kb(volume):9} | {cost:.2f}")
except ValueError:
    print("Помилка: потрібно ввести число")
