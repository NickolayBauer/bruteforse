
from time import time
from itertools import product, count
import math

def hack():
	
	password = input("Ввведите пароль: ")
	start_time = time()
	for j in count(1):
		for i,comb in enumerate(product('1234567890',repeat = j)):
			print('комбинаций: ',i,' пароль: ', ''.join(comb))
			if ''.join(comb) == password:
				end_time = time()-start_time
				print('пройдено кoомбинаций: ',i,"пароль: ",''.join(comb),'затраченное время: ',end_time)
				return end_time
def check_one():	
	end = int(hack())
	if end <= 60:
		print('крайне ненаджёный пароль')
	elif end <= 600:
		print('можно успеть доехать от курской до бауманской')
	elif end <= 9000:
		print('за это время без пробок можно добраться крыма')
	else:
		print('достаточно долго, чтобы мне стало лень это писать')


def to_time(sec):
	return 'hours: ',int(sec/3600), 'minutes: ',int(sec%3600/60) ,'sec: ',int(sec%3600%60)

	
def check_two():
	password = input('Введите пароль: ')
	a = (26+26+10+33)**len(password)
	print('количество вариантов перебора : ',a,'\nНа AMD Athlon X2 Dual-Core 7850 пароль будет взломан за \n',to_time(int(a/3800000000)))

check_one()
check_two()
