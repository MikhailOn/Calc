"""
хотим сделать калькулятор для выражений -2 + 3.5 * 2 - 3 ^ 2
"""

#считаем выражение от пользователя
instr = input('Введите выражение')

#чистим строку (пробелы)
#-> "-2+3.5*2-3^2"
instr = instr.replace(' ','')

#распарсим

"""
на вход строку
(+ * - ^)
(-2 3.5 2 3 2)
[{'opr': '', 'val': -2}, {'opr': +, 'val': 3,5}, {'opr': *, 'val': 2}, ...]
на выход список словарей с операциями +-*/^ и числами
"""
hp_ops = tuple('^')
mp_ops = ('*', '/')
lp_ops = tuple('+-')
supported_ops = hp_ops + mp_ops + lp_ops
digit_chars = tuple('0123456789.-')

actions = []
d = dict()
d['opr'] = 'First'
d['val'] = ''
actions.append(d)

for i, letter in enumerate(instr):
    if letter in supported_ops and (i > 0) and actions[-1]['val'] != '':
        """блок для операций"""
        actions.append({'opr': letter, 'val': ''})

    elif letter in digit_chars:
        """блок для чисел"""
        actions[-1]['val'] += letter

#вычислим операции первого приоритета (^)

"""
на вход наш набор значение и операции
на выход обновленная структура данных с операциями +- и значениями
-2 + 3.5 * 2 - 3 ^ 2
-2 + 3.5 * 2 - 9
"""
i = 0
actions.reverse()
while i < len(actions):

    """проверим операции в действии на соответсвие операции первого приоритета
    если она не соответвует, то ничего не делаем ///
    если соответсвует:
        1 вычисляем результат для числа в этом лействии и соседе слева
        2 записываем результат в соседе СПРАВА
        3 удаляем текущее действие
    """
    action = actions[i]
    operation = action.get('opr')
    if operation in hp_ops:
        if operation == '^':
            pre_res = float(actions[i+1].get('val')) ** float(action.get('val'))
            actions[i+1]['val'] = str(pre_res)
            del actions[i]
    else:
        i += 1
actions.reverse()

#вычислим операции 2го приоритета (* /)

"""
на вход наш набор значение и операции
на выход обновленная ?структура данных? с операциями +- и значениями
-2 + 3.5 * 2 - 9
-2 + 7 - 9
"""
i = 0
result = '0'
error = False
while i < len(actions):

    """проверим операции в действии на соответсвие операции второго приоритета
    если она не соответвует, то ничего не делаем
    если соответствует:
        1 вычисляем результат для числа в этом лействии и соседе слева
        2 записываем результат в соседе СЛЕВА
        3 удаляем текущее действие
    """
    action = actions[i]
    operation = action.get('opr')
    if operation in mp_ops:
        if float(action.get('val')) == 0 and operation == '/':
            result = 'Inf'
            error = True
        else:
            eval_str = actions[i-1].get('val') + operation + action.get('val')
            pre_res = eval(eval_str)
            actions[i-1]['val'] = str(pre_res)
        actions.pop(i)
    else:
        i += 1

#вычислим операции 3го приоритета (+ -)
#-2 + 7 - 9 = -4

if not error:
    for action in actions:
        var_A = result
        var_B = action.get('val')
        operation = action.get('opr')
        if operation in lp_ops:
            result = str(eval(var_A + operation + var_B))
        else:
            result = var_B

#выведем результат
print('Результат: {}'.format(result))