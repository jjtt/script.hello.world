import xbmcaddon
import xbmcgui
from subprocess import call
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
icon        = addon.getAddonInfo('icon')

call(["/usr/bin/mpc", "toggle"])
 
msg = "Play/Pause"
 
xbmcgui.Dialog().notification(addonname, msg, icon, 1000)
