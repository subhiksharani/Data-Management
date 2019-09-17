import json, ast
import sys
import xml.etree.ElementTree as ET

def generate_xml(json_file,xml_file):
    with open(json_file, 'r') as f:
        data = [json.loads(line) for line in f]
        cleandata = ast.literal_eval(json.dumps(data)) 
        root = ET.Element('accounts')
        for i in range(len(cleandata)):
            for key,value in sorted(cleandata[i].items()):
                if key not in 'index':
                    if key == 'account_number':
                        acc = ET.SubElement(root, 'account', number=str(value))
                    else:
                        ET.SubElement(acc, key).text = str(value)
        tree = ET.ElementTree(root)
        tree.write(xml_file)


if __name__=="__main__":
    generate_xml(sys.argv[1],sys.argv[2])
