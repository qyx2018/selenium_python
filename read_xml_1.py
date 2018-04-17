from xml.dom import minidom

dom = minidom.parse('info.xml')

root = dom.documentElement

tagname = root.getElementsByTagName('browser')
print(tagname[0].tagName)

tagname = root.getElementsByTagName('login')
print(tagname[1].tagName)

tagname = root.getElementsByTagName('province')
print(tagname[2].tagName)