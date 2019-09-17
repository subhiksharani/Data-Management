import xml.etree.ElementTree as ET
import sys


def inverted_index(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    inv_index = {}
    i = 0
    for child in root:
        for word in root[i][0].text.split():
            if word in inv_index:
                inv_index[str(word)].insert(len(inv_index),str(child.get('number')))
            else:
                inv_index[str(word)]=[str(child.get('number'))]
        i = i+1
    return inv_index

def to_xml(inv_index, xml_file):
    root = ET.Element('index')
    for key,values in inv_index.iteritems():
        entry = ET.SubElement(root, 'entry')
        ET.SubElement(entry, 'keyword').text = key.lower()
        accounts = ET.SubElement(entry,'accounts')
        for value in values:
            ET.SubElement(accounts, 'number').text = value.lower()
    tree = ET.ElementTree(root)
    tree.write(xml_file)

if __name__=="__main__":
    invert = inverted_index(sys.argv[1])
    to_xml(invert, sys.argv[2])
