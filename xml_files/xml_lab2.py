import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET

class XmlTreeHelper:
    def add_tags_with_text(self, parent, tags): 
        for tag, value in tags.items(): 
            new_tag = ET.SubElement(parent, tag)
            
            new_tag.text = value


root = ET.Element("shop")

category = ET.SubElement(root, "category", {"name": "Vegan Products"})

product_1 = ET.SubElement(category, "product", {"name": "Good Morning Sunshine"})
product_2 = ET.SubElement(category, "product", {"name": "Spaghetti Veganietto"})
product_3 = ET.SubElement(category, "product", {"name": "Fantastic Almond Milk"})

xml_tree_helper = XmlTreeHelper()

xml_tree_helper.add_tags_with_text(product_1, {
    "type": "cereals",
    "producer": "OpenEDG Testing Service",
    "price": "9.90",
    "currency": "USD"
})

xml_tree_helper.add_tags_with_text(product_2, {
    "type": "pasta",
    "producer": "Programmers Eat Pasta",
    "price": "15.49",
    "currency": "EUR"
})

xml_tree_helper.add_tags_with_text(product_3, {
    "type": "beverages",
    "producer": "Drinks4Coders Inc.",
    "price": "19.75",
    "currency": "USD"
})

ET.dump(root)

# tree = ET.ElementTree(root)
# tree.write('shop.xml', 'UTF-8', True)

xml_str = ET.tostring(root, 'utf-8')

pretty_xml = minidom.parseString(xml_str).toprettyxml(indent="    ")

# Write the prettified XML to a file
with open("shop.xml", "w", encoding="utf-8") as f:
    f.write(pretty_xml)


