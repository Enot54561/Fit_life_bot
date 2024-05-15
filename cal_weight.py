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


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def input_bgu(weight):
    return str(f'Белки - {weight * protein}\n'
               f'Жиры - {weight * fat}\n'
               f'Углеводы - {weight * carbohydrates}')


def calc_percent(num, percent):
    return (percent * num) / 100
