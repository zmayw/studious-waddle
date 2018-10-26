#coding=utf-8

from urllib import urlretrieve

#
# urlretrieve('http://ichart.yahoo.com/table.csv?s=600000.SS&a=08&b=25&c=2010&d=09&e=8&f=2010&g=d','pingan.csv')

import csv



with open("pingan.csv","rb") as rf:
    reader = csv.reader(rf)
    with open("pingan2.csv","wb") as wf:
        writer = csv.writer(wf)
        headers = reader.next()
        print headers
        writer.writerow(headers)
        for row in reader:
            print row
            if row[0]< '2017-01-01':
                break
            if int(row[6])>= 50000000:
                writer.writerow(row)
print "end"
from xml.etree.ElementTree import Element,ElementTree


def pretty(e,level=0):
    if len(e) >0:
        e.text = '\n' + '\t'*(level+1)
        for child in e:
            pretty(child,level+1)
        child.tail = child.tail[:-1]
    e.tail = '\n'+'\t'*level

def csvToXML(fname):
    with open(fname,'rb') as f:
        reader = csv.reader(f)
        headers = reader.next()
        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag,text in zip(headers,row):
                e = Element(tag)
                e.text = text
                eRow.append(e)
    pretty(root)
    return ElementTree(root)

et = csvToXML("pingan.csv")
et.write("pingan.xml")



