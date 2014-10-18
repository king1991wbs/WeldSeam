#-*- coding:utf-8 -*-
import plotwelddata_csv

path = raw_input('input your data file name with full path:')
'''
for path in range(2, 32):
	data_file_name = 'C:\\Users\\KING\\Desktop\\data_v_i\\20141016_ban1\\数据日志 0 (%d).xls' % int(path)
	plotwelddata.plotdata(data_file_name)
'''
data_file_name = 'C:\\Users\\KING\\Desktop\\data_v_i\\20141016_ban1\\数据日志 0 (%d).csv' % int(path)
plotwelddata_csv.plotdata(data_file_name)