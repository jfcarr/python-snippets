from xml.dom.minidom import parse,parseString

dom = parse('xmltest.xml')
names=dom.getElementsByTagName('name')

for name in names:
	firstName = name.getElementsByTagName("first")[0].firstChild.data
	lastName = name.getElementsByTagName("last")[0].firstChild.data
	
	print 'Full name is ' + firstName + ' ' + lastName
