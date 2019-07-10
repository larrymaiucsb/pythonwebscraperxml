import xml.etree.ElementTree as ET
import time

tree = ET.parse ('C:\\Users\\larry.mai\\Downloads\\aepedia.xml') 
root = tree.getroot()

root.tag
root.attrib

for child in root:
    print(child.tag, child.attrib)
for child in root:
    print(root.iter())


print("PRINTING TITLES")
time.sleep(3)

for title in root.iter('title'):
    print(title.text)

print("FINISHED PRINTING TITLES")
print("PRINTING THE LINKS")
time.sleep(3)
for link in root.iter('link'):
    print(link.text)
print("FINISHED PRINTING LINKS")
time.sleep(3)


for CDATA in root.iter('CDATA'):
    print(CDATA.text)

time.sleep(2)

for ce in root.iter('/content:encoded'):
    print(ce)
print("done")
for item in root.findall("Full Project Description"):
    print(item)





#print(ET.tostring(root, encoding='utf8').decode('utf8'))
#prints the whole xml file






'''
def CDATA(text=None):
    element = ET.Element(CDATA)
    element.text = text
    return element

class ElementTreeCDATA(ET.ElementTree):
    def _write(self, file, node, encoding, namespaces):
        if node.tag is CDATA:
            text = node.text.encode(encoding)
            file.write("\n<![CDATA[%s]]>\n" % text)
        else:
            ET.ElementTree._write(self, file, node, encoding, namespaces)

if __name__ == "__main__":
    import sys

    text = """
    <?xml version='1.0' encoding='utf-8'?>
    <text>
    This is just some sample text.
    </text>
    """

    e = ET.Element("data")
    cdata = CDATA(text)
    e.append(cdata)
    et = ElementTreeCDATA(e)
    et.write(sys.stdout, "utf-8")
'''
