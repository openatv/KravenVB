#
#  Menu EntryID Converter
#
#  Coded by tomele for Kraven Skins
#
#  This code is licensed under the Creative Commons 
#  Attribution-NonCommercial-ShareAlike 3.0 Unported 
#  License. To view a copy of this license, visit
#  http://creativecommons.org/licenses/by-nc-sa/3.0/ 
#  or send a letter to Creative Commons, 559 Nathan 
#  Abbott Way, Stanford, California 94305, USA.
#

from Components.Converter.Converter import Converter
from Components.Element import cached
from Poll import Poll

class KravenVBMenuEntryID(Poll,Converter,object):
	def __init__(self, type):
		Poll.__init__(self)
		Converter.__init__(self, type)
		self.poll_interval = 1000
		self.poll_enabled = True
		self.type = str(type)
	
	@cached
	def getText(self):
		cur = self.source.current
		if cur and len(cur) > 2:
			selection = cur[2]
		return "Menu: "+selection
	
	text = property(getText)
