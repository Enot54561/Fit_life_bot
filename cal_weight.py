min_index = 25
protein = 1.5
fat = 0.9
carbohydrates = 2


def calc_weight(height, weight):
    height1 = height / 100
    result = int(weight / height1 ** 2)
    if result <= min_index:
        return input_bgu(weight)
    else:
        return input_bgu(calc_percent(weight, 85))


def input_bgu(weight):
    return str(f'<b> Внимание! Расчет произведен по средним значениям! </b>\n'
               f'Ваши индивидуальные особенности не учитываются!\n\n'
               f'Белки - {round(weight * protein, 2)}\n'
               f'Жиры - {round(weight * fat, 2)}\n'
               f'Углеводы - {round(weight * carbohydrates, 2)} \n\n'
               f'Начать сначала /start')


def calc_percent(num, percent):
    return (percent * num) / 100
