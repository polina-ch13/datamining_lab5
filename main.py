import pandas as pd
from itertools import combinations

shop = pd.read_excel("lab.xlsx", sheet_name="Tov")
# print(shop)

print("Введите уровень поддержки:")
supp_lvl = int(input())
# supp_lvl = 3
print("Введите количество товаров в чеке:")
check = int(input())

TID = shop["TID"]
Tovar = shop["Tov"]

# уникальные товары
tov = []

for tv in Tovar:
    if tv not in tov:
        tov.append(str(tv))

# разный товар
print("все товары")
print(tov)
# print(len(tov))
tov_sup = []

# проверяю сколько раз по 1 товару встретилось в чеках
for tv in tov:
    k = 0
    i = 0
    for td in TID:
        if str(Tovar[i]) == str(tv):
            k = k + 1
        i = i + 1
    tov_sup.append(k)

print("чеки с 1 товаром")
print(tov_sup)

tov_new = []
i = 0
for tv in tov:
    if not (tov_sup[i] < supp_lvl):
        tov_new.append(tv)
    i = i + 1

tov_new.sort()
tov = tov_new

# минус чеки с 1 товаром
print("Товары без чеков на 1 товар")
print(tov)
print()

# все покупатели/чеки
cust = []
for n in TID:
    if n not in cust:
        cust.append(n)

C = 2

while (C <= check):
    # комбинации по 2
    comb = set(combinations(tov, C))
    cnt = 0
    for subset in comb:
        # print(subset)
        cnt = cnt + 1
    print("Все комбинации по "+str(C))
    print(comb)

    tov_sup = [0] * cnt
    for n in cust:
        # корзина каждого покупателя
        bask = []
        i = 0
        for inv in TID:
            if str(inv)[0] != 'C':
                if TID[i] == n:
                    if not (Tovar[i] not in tov):
                        bask.append(Tovar[i])
            i = i + 1
        bask.sort()
        # print(bask)
        j = 0
        cm = set(combinations(bask, C))
        for subs in comb:
            for sb in cm:
                if subs == sb:
                    tov_sup[j] = tov_sup[j] + 1
            j = j + 1

    # print(tov_sup)  # кол-во комб по 2

    comb_new = []
    i = 0
    for subs in comb:
        if not (tov_sup[i] < supp_lvl):
            comb_new.append(subs)
            # print(subs)
        i = i + 1
    comb = comb_new
    print(comb)
    tov = []
    # новый список товаров соответствующий tov_sup
    for sb in comb:
        for s in sb:
            if s not in tov:
                tov.append(s)

    tov.sort()
    tov_new = tov
    tov = tov_new
    C = C + 1
