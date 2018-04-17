from xml.dom import minidom

dom = minidom.parse('info.xml')

root = dom.documentElement

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)