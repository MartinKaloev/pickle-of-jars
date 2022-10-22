#
import os
import pickle
class jar_of_picles:
	def __init__(self):
		self.ime_="fail save"
		self.break_="1"
		self.data_=[]
		self.data_ext=[]
		self.low=2
		self.big=4
		self.broi=4
		self.expected_avg=3



	def savs(self):
		f=open(self.ime_, 'wb')
		pickle.dump(self.data_,f)
		f.close()
		ff=open(self.ime_+".txt","w")
		ff.write(str(self.data_))
		ff.close()

	def loads(self):
		if os.path.exists(self.ime_):
			if ".txt" in self.ime_:
				f=open(self.ime_, 'r')
				proxy=list(map(int, f.readline().split(",")))
				#proxy=proxy.replace("\n",'')
				#proxy=proxy.split(",")
				self.data_ext=proxy
				self.data_.extend(self.data_ext)
				f.close()
			else:
				f=open(self.ime_, 'rb')
				self.data_ext=pickle.load(f)
				self.data_.extend(self.data_ext)
				f.close()
			print("pickle loaded")
		else:
			print("pickle jar empty")