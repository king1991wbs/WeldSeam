#-*- coding:utf-8 -*-
"""
version: python 2.7.8 win8 x64
author:  wilson
email:   wison_91@foxmail.com
date:    20140928

Descriptionl:
This python program is aimming at read data from a Excel file,and then plot those data
in diagram.
copyright reserved by CAD Center of Tongji University
"""
import xlrd
import matplotlib.pyplot as plt

#data_file_name = raw_input('input your data file name with full path:')
def plotdata(data_file_name):
	#data_file_name = 'C:\\Users\\KING\\Desktop\\data_v_i\\20141016_ban1\\数据日志 0 (18).xls'
	path = unicode(data_file_name, 'utf-8')
	#path = u'C:\\Users\\KING\\Desktop\\测试.txt'

	data = xlrd.open_workbook(path)

	#read data from Excel and save it in tables
	table = data.sheets()[0]
	#get value of time,voltage and electricity
	time = range(1, len(table.col_values(0)))
	#time = [int(table.col_values(0)[t]) for t in range(1, len(table.col_values(0)))]
	voltage = [int(table.col_values(1)[v]) for v in range(1, len(table.col_values(1)))]#这样得到的数据是逆序的
	voltage.reverse()
	#voltage = [int(v) for v in table.col_values(1)]
	electricity = [int(table.col_values(2)[e]) for e in range(1, len(table.col_values(2)))]
	electricity.reverse()

	fig1 = plt.figure('1')
	#plt.scatter(voltage, electricity, color='red', marker='.')
	plt.plot(voltage, label = 'voltage')
	plt.plot(electricity, label = 'electrictiy')
	#plt.xlabel('voltage')
	#plt.ylabel('electricity')
	plt.xticks(range(0, len(voltage), 5))
	plt.yticks(range(0, 110, 5))
	plt.xlim(0,350)#限制x轴的区间
	plt.grid(True)#绘制背景格子
	plt.legend(loc = 'upper left')#设置图例标签显示位置
	plt.title('relatioship of v & e')
	fig1.autofmt_xdate()
	#plt.savefig('C:\\Users\\KING\\Desktop\\data_v_i\\1.png')
	plt.show()

	'''
	plt.figure('2')
	plt.plot(voltage, electricity)
	plt.xlabel('voltage')
	plt.ylabel('electricity')
	plt.title('t & v')

	plt.figure('3')
	plt.scatter(time, electricity, color='red', marker='*')
	plt.xlabel('time')
	plt.ylabel('electricity')
	plt.title('t & e')
	plt.show()
	'''