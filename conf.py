class conf():
	"""Configuration of the framework"""
	def __init__(self):
		"""
		Construct of the class
		"""
		self.languages = self.getLanguages()

	def getLanguages(self):
		"""
		Get all languagens of the framework
		:return: List
		"""
		return ["pt-br","en-us"]

	def langExist(self,lang):
		"""
		Check if lang exist in framework languages supported
		:return: String
		"""
		if(lang in self.languages):
			return lang
		else:
			return "pt-br"