#!/usr/bin/python3
# -*- coding:utf-8 -*-

import configparser

def config(filename='/usr/lib/cgi-bin/database.ini', section='postgresql'):
	# create a parser
	parser = configparser.ConfigParser()
	# read the config file
	parser.read('/usr/lib/cgi-bin/database.ini')
	db={}
	#get section, default to postgres
	if parser.has_section(section):
		params = parser.items(section)
		for param in params:
			db[param[0]] = param[1]
	else:
		raise Exception('Section {0} not found in the {1} file'.format(section, filename))
	return db
