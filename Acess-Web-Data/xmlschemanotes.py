import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
    </person>'''
xml_loops = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>    
            <name>Chuck</name>
            </user>
            <user x="7">
                <id>009</id>
                <name>Brent</name>
                </user>
                </users>
                </stuff>'''
stuff = ET.fromstring(xml_loops)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))