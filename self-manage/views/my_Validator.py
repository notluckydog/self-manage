import wx

class MyNumberValidator(wx.Validator):
	# 创建验证器子类
	#在输入金额的时候，规范输出格式
	def __init__(self):
		wx.Validator.__init__(self)
		self.ValidInput = ['.','0','1','2','3','4','5','6','7','8','9']
		self.StringLength = 0
		self.dot = 0        #字符串中小数点个数
		self.Bind(wx.EVT_CHAR,self.OnCharChanged)  #  绑定字符输入事件
		self.pot = []     #用来记录最近输出的内容，用来判断有没有删除小数点

	def OnCharChanged(self, event):
		# 得到输入字符的 ASCII 码
		keycode = event.GetKeyCode()

		# 把 ASII 码 转成字符
		InputChar = chr(keycode)

		# 退格（ASCII 码 为8），删除一个字符。
		if keycode == 8:
			self.StringLength -= 1
			#如果删除的是小数点且有数字的话
			if len(self.pot)>=1 and self.pot[-1] =='.':
				self.dot-=1
				self.pot.pop()

			elif len(self.pot) ==0:
				event.Skip()
			else:
				self.pot.pop()
				# 事件继续传递
				event.Skip()
			return


		if InputChar in self.ValidInput:
			# 第一个字符为 .,非法，拦截该事件，不会成功输入
			if InputChar == '.' and self.StringLength == 0 and self.dot>=1:
				return False
			# 在允许输入的范围，继续传递该事件。
			elif InputChar == '.' and self.StringLength >0:
				#输入小数点后记录，不允许输入两个小数点
				self.dot +=1
			else:
				self.pot.append(InputChar)
				event.Skip()
				self.StringLength += 1
				return True
		return False

	def Clone(self):
		return MyNumberValidator()

	def Validate(self,win):#1 使用验证器方法

		textCtrl = self.GetWindow()
		text = textCtrl.GetValue()
		valid_text = ''
		for i in text:
			if i in self.ValidInput:
				valid_text += i
		textCtrl.SetValue(valid_text)
		return True

	def TransferToWindow(self):
		return True

	def TransferFromWindow(self):
		return True
