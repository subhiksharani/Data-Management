import xml.etree.ElementTree as ET
import sys

def read_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    return root

def search(term, root):
    words = term.lower().split()
    output = []
    i = 0
    for word in words:
        for child in root:
            if word == root[i][0].text:
                for item in child.findall('accounts/number'):
                    output.append(item.text)
            i = i+1
        i=0
    result = []
    for item in output:
        if item not in result:
            result.append(item)
    print('The Account Numbers associated with <',term,'> is ', result)


if __name__=="__main__":   
    root = read_xml(sys.argv[1])   
    search(sys.argv[2],root)
