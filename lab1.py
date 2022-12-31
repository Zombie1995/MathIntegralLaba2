import numpy as np
from scipy.integrate import dblquad

X_START = -9
Y_START = -8
X_END = 31
Y_END = 81

def calc_integral(axis_div_num, x_start=X_START, y_start=Y_START, x_end=X_END, y_end=Y_END, lower=True):
    # Подстраиваем входные значения области, чтобы они не выходили за пределы G
    x_start = np.clip(x_start, X_START, X_END)
    y_start = np.clip(y_start, Y_START, Y_END)
    x_end = np.clip(x_end, X_START, X_END)
    y_end = np.clip(y_end, Y_START, Y_END)

    x_step = (x_end - x_start) / axis_div_num
    y_step = (y_end - y_start) / axis_div_num
    mu = x_step * y_step # Мера Жордана одна для всех участков
    integral = 0
    for x in np.linspace(x_start, x_end, axis_div_num, endpoint=False):
        for y in np.linspace(y_start, y_end, axis_div_num, endpoint=False):
            if lower:
                integral += np.arctan(x + y) * mu # Из свойств нашей функции понятно, что для нахождения минимального значения на участке нужно брать наименьшие x и y
            else:
                integral += np.arctan((x + x_step) + (y + y_step)) * mu # Для максимальных значений - максимальные x и y
    return integral

def calc_true_integral(x_start=X_START, y_start=Y_START, x_end=X_END, y_end=Y_END):
    # Подстраиваем входные значения области, чтобы они не выходили за пределы G
    x_start = np.clip(x_start, X_START, X_END)
    y_start = np.clip(y_start, Y_START, Y_END)
    x_end = np.clip(x_end, X_START, X_END)
    y_end = np.clip(y_end, Y_START, Y_END)

    return dblquad(lambda x, y: np.arctan(x+y), x_start, x_end, lambda x: y_start, lambda x: y_end)

processing = True

while processing:
    x_start = float(input("X_START: "))
    y_start = float(input("Y_START: "))
    x_end = float(input("X_END: "))
    y_end = float(input("Y_END: "))

    axis_div_num = int(input('Na skolko razbit kazduyu is osey?: '))

    print("Processing...")

    min_int = calc_integral(axis_div_num, x_start=x_start, y_start=y_start, x_end=x_end, y_end=y_end, lower=True)
    max_int = calc_integral(axis_div_num, x_start=x_start, y_start=y_start, x_end=x_end, y_end=y_end, lower=False)

    integral = calc_true_integral(x_start=x_start, y_start=y_start, x_end=x_end, y_end=y_end)[0]

    print(f"Istinnoe znachenie: {integral}")
    
    print(f"Nijniy integral Darbu: {min_int}; Oshibka: {integral - min_int}")
    print(f"Verhniy integral Darbu: {max_int}; Oshibka: {integral - max_int}")

    processing_string = input("Prdoljit ('y' - da, 'n' - net)?: ")

    if processing_string == 'n':
        processing = False
    else:
        processing = True
