per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Введите сумму которую планирует положить под проценты:'))
tkb = per_cent['ТКБ']
ckb = per_cent['СКБ']
vtb = per_cent['ВТБ']
sber = per_cent['СБЕР']
sum = []
sum.append(money / 100 * tkb)
sum.append(money / 100 * ckb)
sum.append(money / 100 * vtb)
sum.append(money / 100 * sber)
print('Накопленные средства за год:')
print('ТКБ:', money / 100 * tkb)
print('СКБ:', money / 100 * ckb)
print('ВТБ:', money / 100 * vtb)
print('СБЕР:', money / 100 * sber)
m = max(sum)
print('Максимальная сумма, которую вы можете заработать:', m)