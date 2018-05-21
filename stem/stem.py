import nltk

class stemming():
	def __init__(self):
		"""
		Construct of the class, this method imstancie RSLP stemming
		"""
		self._stem = nltk.stem.RSLPStemmer()

	def stemmingWord(self,word):
		"""
		stemming word
		"""
		return self._stem.stem(word)

