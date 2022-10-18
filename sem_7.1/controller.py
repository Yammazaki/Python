import view
import math_func as mf
import log

# def input_num():
#     a = view.num_input()
#     b = view.num_input()
#     return a, b

def calculate():
    a = view.num_input()
    b = view.num_input()
    oper = view.oper_input()
    log.input_write(f'{a} {oper} {b}')
    if oper == '+':
        return view.view_res(mf.sum(a, b))
    elif oper == '-':
        return view.view_res(mf.diff(a, b))
    elif oper == '*':
        return view.view_res(mf.mult(a, b))
    else:
        return view.view_res(mf.div(a, b))

