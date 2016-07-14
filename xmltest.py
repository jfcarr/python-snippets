import xml.etree.ElementTree as ET

tree = ET.parse('xmltest.xml')
root = tree.getroot()

firstName = ''
lastName = ''

for names in root.iter('names'):
	for name in names:
		for details in name:
			if details.tag == 'first':
				firstName = details.text
			if details.tag == 'last':
				lastName = details.text
		print 'Full name is ' + firstName + ' ' + lastName
