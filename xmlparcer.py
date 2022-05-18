# -*- coding: utf-8 -*-
import xml.dom.minidom
import urllib.request
import sqlite3
import main

class OrderParser(object):

    def __init__(self, url, flag='url'):
        self.list = []
        self.order_list = []
        self.flag = flag
        self.rem_value = 0
        xml = self.getXml(url)
        self.handleXml(xml)

    def getXml(self, url):
        try:
            print(url)
            f = urllib.request.urlopen(url)
        except:
            f = url

        doc = xml.dom.minidom.parse(f)
        node = doc.documentElement

        return node

    def handleXml(self, xml):
        rem = xml.getElementsByTagName('zOrders')
        order = xml.getElementsByTagName("order")
        self.handleOrders(order)

    def getElement(self, element):
        return self.getText(element.childNodes)

    def handleOrders(self, orders):
        for order in orders:
            self.handleOrder(order)
            self.list = []

    def handleOrder(self, order):
        fio = self.getElement(order.getElementsByTagName("fio")[0])
        email = self.getElement(order.getElementsByTagName("email")[0])
        product = self.getElement(order.getElementsByTagName("product")[0])
        service = self.getElement(order.getElementsByTagName("service")[0])

        self.list.append(fio)
        self.list.append(email)
        self.list.append(product)
        self.list.append(service)

        self.order_list.append(self.list)

    def getText(self, nodelist):
        rc = ""
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc = rc + node.data
        return rc
