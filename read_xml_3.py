from xml.dom import minidom

dom = minidom.parse('info.xml')

root = dom.documentElement

provinces = dom.getElementsByTagName('province')
citys = dom.getElementsByTagName('city')

p2 = provinces[1].firstChild.data
print(p2)

c1 = citys[0].firstChild.data
print(c1)

c2 = citys[1].firstChild.data
print(c2)