from Plugins.Plugin import PluginDescriptor
from enigma import getDesktop
from Components.Language import language
from os import environ
import gettext
from Tools.Directories import resolveFilename, SCOPE_LANGUAGE, SCOPE_PLUGINS
import KravenVB

lang = language.getLanguage()
environ["LANGUAGE"] = lang[:2]
gettext.bindtextdomain("enigma2", resolveFilename(SCOPE_LANGUAGE))
gettext.textdomain("enigma2")
gettext.bindtextdomain("KravenVB", "%s%s" % (resolveFilename(SCOPE_PLUGINS), "Extensions/KravenVB/locale/"))

def _(txt):
	t = gettext.dgettext("KravenVB", txt)
	if t == txt:
		t = gettext.gettext(txt)
	return t

def main(session, **kwargs):
	reload(KravenVB)
	try:
		session.open(KravenVB.KravenVB)
	except:
		import traceback
		traceback.print_exc()

def main_menu(menuid):
	if menuid == "system":
		return [("KravenVB", main, _("Configuration tool for KravenVB"), 27)]
	else:
		return []

def Plugins(**kwargs):
	list = []
	if distro =='openatv':
		list.append(PluginDescriptor(name="Setup KravenVB", description=_("Configuration tool for KravenVB"), where = PluginDescriptor.WHERE_MENU, fnc = main_menu))
	# TODO 2019-08-09 - Uncomment and indent to avoid hooking plugins menu:
	#else:
	screenwidth = getDesktop(0).size().width()
	if screenwidth and screenwidth == 1920:
		list.append(PluginDescriptor(name="KravenVB", description=_("Configuration tool for KravenVB"), where = PluginDescriptor.WHERE_PLUGINMENU, icon='pluginfhd.png', fnc=main))
	else:
		list.append(PluginDescriptor(name="KravenVB", description=_("Configuration tool for KravenVB"), where = PluginDescriptor.WHERE_PLUGINMENU, icon='plugin.png', fnc=main))
	# END TODO
	return list

