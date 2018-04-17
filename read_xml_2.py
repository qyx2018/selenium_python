from xml.dom import minidom

dom = minidom.parse('info.xml')

root = dom.documentElement

logins = root.getElementsByTagName('login')

username = logins[0].getAttribute('username')
print(username)

password = logins[0].getAttribute('password')
print(password)

username = logins[1].getAttribute('username')
print(username)

password = logins[1].getAttribute('password')
print(password)