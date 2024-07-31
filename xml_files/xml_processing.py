import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()

print('The root tag is:', root.tag)
print('The root has the following children:')

for child in root:
    print(child.tag, child.attrib)

print("My books:\n")

for book in root:
    print('Title: ', book.attrib['title'])
    print('Author:', book[0].text)
    print('Year: ', book[1].text, '\n')

#  returns all elements by having the tag passed as an argument
for author in root.iter('author'):
    print(author.text)

# search for direct child elements
for book in root.findall('book'):
    print(book.get('title'))

# first children
print(root.find('book').get('title'))

# learning yet 
# test = """
# <?xml version="1.0"?>
# <data>
#     <book title="The Little Prince">
#         <author>Antoine de Saint-Exupéry</author>
#         <year>1943</year>
#     </book>
#     <book title="Hamlet">
#         <author>William Shakespeare</author>
#         <year>1603</year>
#     </book>
# </data>
# """

# root = ET.fromstring(test)

for child in root:
    child.tag = 'movie'

    child.remove(child.find('author'))
    child.remove(child.find('year'))

    child.set('rate', '5')

    print(child.tag, child.attrib)

    for sub_child in child:
        print(sub_child.tag, ':', sub_child.text)

tree.write('movies.xml', 'UTF-8', True)

# Building a XML File 
root = ET.Element('data')
movie_1 = ET.SubElement(root, 'movie', {'title': 'The Little Prince', 'rate': '5'})
movie_2 = ET.SubElement(root, 'movie', {'title': 'Hamlet', 'rate': '5'})
ET.dump(root)

