# -*- coding: utf-8 -*-
import wx
import random
import csv
import time
from datetime import datetime

class Main(wx.Frame):
	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'Main', style=wx.MAXIMIZE | wx.MAXIMIZE_BOX)
		global start
		self.Maximize(True)
		start = time.time()
		self.SetBackgroundColour('white')

		#ディスプレイサイズによって表示が崩れないようにしてるやつら
		display = wx.DisplaySize()
		wratio = display[0] / 1920
		hratio = display[1] / 1080
		global number
		print ("No. " + str(number))
		number = number + 1
		global flag
		if random.randrange(1, 100, 1) > 51 :	
			num1, num2 = self.makeSumLine()
			right = self.makeSum3(num1, num2)
			function = self.makeSum(num1, num2, right)
			flag = self.checkSum(num1, num2, right)
			print (function)
		else :
			num1, num2 = self.makeSubLine()
			right = self.makeSub3(num1, num2)
			function = self.makeSub(num1, num2, right)
			flag = self.checkSub(num1, num2, right)
			print (function)

		qpanel = wx.Panel(self, wx.ID_ANY, size=(1600*wratio, 500*hratio), pos=(550*wratio,290*hratio))
		qpanel.SetBackgroundColour('white')
		font = wx.Font(100*wratio, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		question = wx.StaticText(qpanel, -1, function, style=wx.ALIGN_CENTER)
		question.SetFont(font)

		panel = wx.Panel(self, wx.ID_ANY, size=(1400*wratio, 250*hratio), pos=(260*wratio,790*hratio))
		text = wx.StaticText(panel, -1, "←　正しい：左クリック　　　間違い：右クリック　→")
		font = wx.Font(50*wratio, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		text.SetFont(font)
		
		m = wx.DisplaySize()

		self.Bind(wx.EVT_LEFT_DOWN, self.OnLClick, source=None)
		self.Bind(wx.EVT_RIGHT_DOWN, self.OnRClick, source=None)
		qpanel.Bind(wx.EVT_LEFT_DOWN, self.OnLClick, source=None)
		qpanel.Bind(wx.EVT_RIGHT_DOWN, self.OnRClick, source=None)
		question.Bind(wx.EVT_LEFT_DOWN, self.OnLClick, source=None)
		question.Bind(wx.EVT_RIGHT_DOWN, self.OnRClick, source=None)
		panel.Bind(wx.EVT_LEFT_DOWN, self.OnLClick, source=None)
		panel.Bind(wx.EVT_RIGHT_DOWN, self.OnRClick, source=None)
		text.Bind(wx.EVT_LEFT_DOWN, self.OnLClick, source=None)
		text.Bind(wx.EVT_RIGHT_DOWN, self.OnRClick, source=None)

	def OnLClick(self, event):#左クリック
		global actionlist
		global flag
		global start
		actionlist.append("1")

		if (flag == 1):
			actionlist.append("1")
			print("○")
		else:
			actionlist.append("0")
			print("×")
		anstime = time.time()-start
		print ("time : " + str(anstime))
		#print(" ")
		actionlist.append(anstime)
		f = open(filename, 'a')
		writer = csv.writer(f, lineterminator='\n')
		writer.writerow(actionlist)
		actionlist = []
		f.close()
		self.Destroy()
		self = Main(parent=None, id=-1)
		self.Show()

	
	def OnRClick(self, event):#右クリック
		global actionlist
		global flag
		global start
		actionlist.append("0")

		if (flag == 0):
			actionlist.append("1")
			print("○")
		else:
			actionlist.append("0")
			print("×")
		anstime = time.time()-start
		print ("time : " + str(anstime))
		#print(" ")
		actionlist.append(anstime)
		f = open(filename, 'a')
		writer = csv.writer(f, lineterminator='\n')
		writer.writerow(actionlist)
		actionlist = []
		f.close()
		self.Destroy()
		self = Main(parent=None, id=-1)
		self.Show()
#--------------------ここから足し算の関数----------------------------------------------------------------------
	def makeSumLine(self): #左辺の二つの数字を生成
		self.num1 = random.randrange(10, 99, 1)
		self.num2 = random.randrange(10, 99, 1)
		return self.num1, self.num2

	def makeSum3(self, num1, num2): #右辺の数字を間違いも含めて生成
		self.hensu = random.randrange(1, 100, 1)
		self.num3 = num1 + num2
		
		if ((100 >= self.hensu) & (self.hensu > 76)):
			self.num3 = abs(self.num3 + random.randrange(-15, 15, 1))

		elif ((75 >= self.hensu) & (self.hensu > 50)):
			self.num3 = abs(self.num3 + (random.randrange(-3, 3, 1) * 10))
		return self.num3

	def makeSum(self, num1, num2, num3): #足し算の式（右辺も含めた）の文字列の生成
		self.function = str(num1) + " + " + str(num2) + " = " + str(num3)
		return self.function

	def checkSum(self, num1, num2, num3): #数式の正誤を判定
		global actionlist
		if ((num1 + num2) == num3):
			actionlist.append("1")
			return 1
		else:
			actionlist.append("0")
			return 0
#--------------------ここから引き算の関数----------------------------------------------------------------------
	def makeSubLine(self): #左辺の二つの数字を生成
		self.num1 = random.randrange(11, 99, 1)
		self.num2 = random.randrange(10, self.num1, 1)
		return self.num1, self.num2


	def makeSub3(self, num1, num2): #右辺の数字を間違いも含めて生成
		self.hensu = random.randrange(1, 100, 1)
		self.num3 = num1 - num2
		
		if ((100 >= self.hensu) & (self.hensu > 76) & (self.num3 != 0)):
			self.num3 = abs(self.num3 + random.randrange(-15, 15, 1))

		elif ((75 >= self.hensu) & (self.hensu > 50) & (self.num3 != 0)):
			self.num3 = abs(self.num3 + ((random.randrange(-3, 3, 1)) * 10))
		return self.num3


	def makeSub(self, num1, num2, num3): #足し算の式（右辺も含めた）の文字列の生成
		self.function = str(num1) + " - " + str(num2) + " = " + str(num3)
		return self.function


	def checkSub(self, num1, num2, num3): #数式の正誤を判定
		global actionlist
		if ((num1 - num2) == num3):
			actionlist.append("1")
			return 1
		else:
			actionlist.append("0")
			return 0

	

		

if __name__ == '__main__':
	global actionlist
	global flag
	global start
	global number
	number = 1
	actionlist = ["正解", "入力", "正誤", "回答時間"]
	now = datetime.now()
	now_ymd = "{0:%Y_%m_%d_%H_%M_%S}".format(now)
	filename="math"+now_ymd+".csv"
	f = open(filename, 'w')
	writer = csv.writer(f, lineterminator='\n')
	writer.writerow(actionlist)
	actionlist = []
	f.close()

	app = wx.App()
	frame = Main(parent=None, id=-1)
	frame.Show()


	app.MainLoop()
