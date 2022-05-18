import io
import xml.dom.minidom as mDom


def createxmlFile(ordersList, filename):
    strSum = "<zOrders>"
    for i in range(len(ordersList)):
        strSum += "<order>"
        strSum += "<fio>" + str(ordersList[i][1]).encode('utf-8').decode('utf-8') + "</fio>"
        strSum += "<email>" + str(ordersList[i][2]) + "</email>"
        strSum += "<product>" + str(ordersList[i][3]) + "</product>"
        strSum += "<service>" + str(ordersList[i][4]) + "</service>"
        strSum += "</order>"
    strSum += "</zOrders>"
    myfile = open(filename, "w")
    myfile.write(mDom.parseString(strSum).toprettyxml().encode('utf-8').decode('utf-8'))
