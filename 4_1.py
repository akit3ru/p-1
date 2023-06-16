"""
def strcounter(s):
    # O (N*M)
    for sym in set(s):
        count = 0
        for sub_sym in s:
            if sym == sub_sym:
                count += 1
        print(sym, count)


strcounter('abcaddf')
# N = 7 кол-во символов
# М = 5 кол-во уникальных символов
# S = 5*7 = 35 асимптотическая сложность
# O - кол-во операций


def strcounter(s):
    # O (N**2)
    for sym in s:
        count = 0
        for sub_sym in s:
            if sym == sub_sym:
                count += 1
        print(sym, count)


# S = 7*7 = 49
strcounter('abcaddf')
"""


def strcounter(s):
    # O(N)
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1


print('изменения')
strcounter('abcaddf')
