import time

class SkillBox(object):
	"""docstring for SkillBox"""
	def __init__(self, n, c, m):
		super(SkillBox, self).__init__()
		self.name = n
		self.cours = c
		self.money = m
		print(f'Здравствуйте {self.name} вы выбрали курс по {self.cours} стоимостью {self.money} руб')
		self.start()

	def __repr__(self):
		return self.name, self.cours

	def start(self):
		a = input('Хотели бы вы начать? y/n :')
		if a == 'y':
			self.start_cours()
		elif a == 'n':
			print('денег мы вам не вернем(((')

	def start_cours(self):
		for i in reversed(range(5)):
			time.sleep(1)
			print(i)
			if i == 0:
				print('вы выучили питон до мидл разработчика')

SkillBox('Sarutor', 'Python', 60000)