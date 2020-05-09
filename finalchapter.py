# def f1():
#     return 5
#
#
# a=f1()
# print(a)
#
#
# def f2():
#     return 5
#     return 6
#
# b=f2()
# print(b)
#
#
#
# def f3():
#     return 5,6
#
# c=f3()
# print(c)
#
#
# def f4():
#     yield 5
#     yield 6
#
# x,y=f4()
# print(x)
# print(y)
#
#
# def f5():
#     yield 5
#     yield 6
#
#
# z=f5()
# print(z)
# a=iter(next(z))
#
#
# def f1():
#     yield 5
#     yield 6
#
#
# a=f1()
# print(a)
# print(next(a))
# print(next(a))
#
#
# def f2():
#     yield 5
#     yield 6
#
# c=f2()
#
# for i in c:
#     print(i)
#
#

# Lambda function are anonymous function. Lambda function will not have a name

#
#
# def sum(a,b):
#     c=a+b
#     return c
#
# x=sum(2,3)
# print(x)
#
#
# def sum(a,b):
#     c=a+b
#     print(c)
#
#
# x=sum(2,3)
# print(x)
#
#
# z=lambda x,y:x+y
# print(z(2,3))
#
#
# a=lambda x:x%2==0
# print(a(2))
# print(a(3))
# print(a(4))
#
#
# l=[1,2,3,4,5,6,7,8]
#
# k1=list(filter(lambda x:x%2==0,l))
# print(k1)
#
#
#
# for i in k1:
#     print(i)
#
#
#
# l=[1,2,3,5,6,7,8]
#
# o1=list(filter(lambda x:x<6,l))
# print(o1)
#
#
# def f1():
#     x=20
#     return x
#
# a=f1()
# print(a)
#
#
# def f2():
#     def f3():
#         x=20
#         return f3()
#
# a=f2()
# print(a)
#
#
# def smart_tv():
#     print("Smart tv")
#
# def tv():
#     print("tv")
#
#
# tv()
# smart_tv()
#
# def smart_tv():
#     print("Smart tv")
#
# @tv
# def tv():
#     print("tv")
#
#
# tv()
# smart_tv()
#
#
#
# def smart_tv():
#     print("smart tv")
#
# @smart_tv
# def tv():
#     print("tv")
#
#
# tv()
# smart_tv()
#
# def smart_tv(tv):
#     print("smart tv")
#
# @smart_tv
# def tv():
#     print("Normal tv")
#
#
# tv()
# smart_tv()
#
#
# def smart_tv(tv2009):
#     def waterproof_tv(tv2009):
#         print("inside waterproof tv")
#         return waterproof_tv()
#
# def tv():
#     print("inside tv")
#
# tv()
# smart_tv()
#
#
# def smart_tv(tv):
#     print("Inside  smart tv")
#
# @smart_tv
# def tv():
#     print("inside tv")
#
#
# tv()
#
#
#
# def smart_tv(tv):
#     def waterproof_tv(tv):
#         print("inside waterproof")
#         return waterproof_tv()
#
# @smart_tv
# def tv():
#     print("inside tv")
#
#
# tv()
#
#
#
# def waterproof_tv(smart_tv):
#     print("waterproof tv")
#
# @waterproof_tv
# def smart_tv(tv):
#     print("smart tv")
#
# @smart_tv
# def tv():
#     print("inside tv")
#
#
# tv()

#
#
# Return keyword is optional by default functiio will return not none



#
# def f1(a,b):
#     print("inside f1")
#     c=a+b
#     return a+b
#     return c
#
# a=f1(2,3)
# print(a)

#
# def enhanced_login(func):
#     def login_withforgot():
#         print("login with forgot")
#         func()
#         return login_withforgot()
#
#
#
# @enhanced_login
# def login():
#     print("login with un and password")
#
#
# login()


#
# def smarttv(jspider):
#     def smartimplementation():
#         print("smart tv")
#         jspider()
#         return smartimplementation
#
#
#
# @smarttv
# def colortv(qspider):
#     def newimp():
#         print("color tv implementation")
#         qspider()
#         return newimp
#
#
#
# @colortv
# def black_whhitetv():
#     print("black and white tv")
#
#
# black_whhitetv()


#
# def loginenhaced_login(func1):
#     def captcha():
#         print("cpatcha")
#         func1()
#         captcha()
#
#
#
# @loginenhaced_login
# def enhancedlogin(func):
#     def login_with_forgot():
#         print("login with forgot")
#         func()
#         return login_with_forgot()
#
# @enhancedlogin
# def login():
#     print("login with un and pwd")
#
#
#
# login()


# l=[1,2,3,"qspiders"]
# l[0]=10
# print(l)
# print(l[3])
# print(l[10])


# for i in l:
#     print(i)


# l=[1,2,3,"qspiders"]
# l1=l.insert(0,"jspiders")
# print(l)
# print(l[0])
# print(l[1])
#
# for var in l1:
#     print(var)


# for var in l:
#     print(var)
# l.insert(100,"puneeth")
# print(l)


# l=[1,2,3,"qspiders"]
# l.insert(-10,'btm')
#
#
# for var in l:
#     print(var)
#
# l=[1,2,3,'qspiders']
# l.remove('qspiders')
#
# for var in l:
#     print(var)


#
# l=[1,2,3,"qpsiders"]
# l.remove(300)
#
# for var in l:
#     print(var)


# l=[1,2,3,"qspiders","jspiders"]
# print(l.count(3))
# print(l.count("jspiders"))
# print(l.count("qspiders"))


# l=["python","Java","selenium","python","ruby","python"]
# print(l.count("python"))
#
#
# l=["python","Java","selenium","python","ruby"]
# s=set(l)
# print(s)

# l=[1,2,3,"q","qspiders"]
# l1=l.append("100")
#
# for var in l:
#     print(var)

#
# l1=[1,2,"q","qspiders"]
# l2=[10,20,"30","40"]
# l3=l1.append(l2)
#
# for var in l1:
#     print(var)
#


# for var in range(0,101,2):
#     print(var)


# for var in range(2,11,1):
#     j=var**2
#     l.append(j)
#
#
# print(l)
#
#
# for var in range(2,11,1):
#     j=var**2
#     l.append(j)
#
# print(l)
import select

l=[1,2,3,3,4,4,5]
l1=[]

# for i in l:
#     if i not in l1:
#         l1.append(i)
#
#
# print(l1)


l=[1,2,3,3,4,4,5]
l1=[]
l2=[]

# for i in l:
#     if i not in l1:
#         l1.append(i)
#     else:
#         l2.append(i)
#
#
# print(l1)
# print(l2)

#
#
# s=set(l)
# print(s)


# l=[10,20,30,40,50]
# print(max(l))


#
# l=[10,20,30,40,50]
# l1=[]
# max_val=0
#
# for i in l:
#     if i>max_val:
#         max_val=i
#         l1.append(max_val)

#
# l=[10,20,30,40,50]
# l1=[]
# max_val=0
#
# for i in l:
#     if i>max_val:
#         max_val=i
#         l1.append(max_val)
#
#
# print(l1)

# d={'a':1,'b':2,'c':3,'d':4}

# print(d.get('b'))

# for i in d.keys():
#     print(i)
#
# for j in d.values():
#     print(j)


# for k in d.items():
#     print(k)

#
#
# for i in d.values():
#     print(i)

#
# import xlrd
#
# path="G:/My Drive/Partners/FY 20-21/1. April'20/Mid Month/April 20 Payable Mid month.xlsx"
# wb=xlrd.open_workbook(path)
# ws=wb.sheet_by_name("Sheet1")
# val=ws.cell_value(1,1)
# print(val)


# import xlrd
# path="G:/My Drive/Partners/FY 20-21/1. April'20/Mid Month/April 20 Payable Mid month.xlsx"
# wb=xlrd.open_workbook(path)
# ws=wb.sheet_by_name("Sheet1")
# val=ws.cell_value(1,1)
# print(val)
#
# row_count=ws.nrows
# col_count=ws.ncols
#
# for i in range(row_count):
#     for j in range(col_count):
#         print(ws.cell_value(i,j))


#
# import xlrd
#
# path="G:/My Drive/Partners/FY 20-21/1. April'20/Mid Month/April 20 Payable Mid month.xlsx"
# wb=xlrd.open_workbook(path)
# ws=wb.sheet_by_name("Sheet1")
# val=ws.cell_value(1,1)
# print(val)

# import xlrd
#
# path="G:/My Drive/Partners/FY 20-21/1. April'20/Mid Month/April 20 Payable Mid month.xlsx"
# wb=xlrd.open_workbook(path)
# ws=wb.sheet_by_name("Sheet1")
#
# row_count=ws.nrows
# col_count=ws.ncols
#
# for i in range(row_count):
#     for j in range(col_count):
#         print(ws.cell_value(i,j))



# import xlrd
#
# path="G:/My Drive/Partners/FY 20-21/1. April'20/Mid Month/April 20 Payable Mid month.xlsx"
# wb=xlrd.open_workbook(path)
# ws=wb.sheet_by_name("Sheet1")
#
#
# row_count=ws.nrows
# col_count=ws.ncols
#
#
# def read_xl_data(input_val):
#     for i in range(row_count):
#         for j in range(col_count):
#             if (ws.cell_value(i,j)==input_val):
#                 print(ws.cell_value(i,j+1))
#
# read_xl_data("Treebo Daffodil Suites")


#
# The central location where in entire source code artifacts
# not placed
#
#
# x=200
# def f1():
#     global x
#     x=100
#     print("function1",x)
#
#
# a=f1()
#


# import logging
#
#
# logging.basicConfig(filename=)
#
#
# a=100
#
# def f1():
#     print("inside f1")

#
# f1()
#
#
# import re
#
# s=input("Enter mail Id")
# m=re.fullmatch("[a-zA-Z0-9_.]*@gmail.com",s)
# if m!=None:
#     print("Valid email Id")
# else:
#     print("Invalid email Id")

#
#
# from selenium import webdriver
#
# qspider=webdriver.Chrome()
# qspider.get("file:///C:/Users/Admin/Desktop/login.html")
#
#
#
# from selenium import webdriver
#
# qspider=webdriver.Chrome()
# qspider.get("file:///C:/Users/Admin/Desktop/login.html")



# path to identify the elemant
#
# //*[@id='email']
# //input[@id='email']
#
# //*[@id='pass']
# //*[@id='u_o_j']


#
# //input[@name='ur']
# # //input(@qsp='sel1')
# //input[@id='1234']
# //input[@type='text']

#
# //a[text()='forgotten account?']
# //a[contains(text(),'forgotten')]
# //a[contains(text(),'forgotten')]
#
# //input[contains(@id,'123')]
# //input[@name='un']
# //input(contains(@name,'un'))
# //input[contains(@name,'se1')]


# from selenium import webdriver
#
# browser='ff'
#
# if browser=='chrome':
#     driver=webdriver.Chrome()
#     driver.get("file:///C:/Users/Admin/Desktop/login.html")
# elif (browser=='ff'):
#     driver=webdriver.Firefox()
#     driver.get("file:///C:/Users/Admin/Desktop/login.html")
# elif (browser=='ie'):
#     driver=webdriver.Ie()
#     driver.get("file:///C:/Users/Admin/Desktop/login.html")
# driver.implicitly_wait(30)

# from selenium import webdriver
#
# day=driver.find_element_by_name("birthday_day")
# s1=select(day)
# s1.select_by_vislbe_text("5")

#
# from selenium import webdriver
#
# month=driver.find_element_by_id("month")
# s2=select(month)
# s2.select_by_value("2")
#
# year=driver.find_element_by_id("Year")
# s3=select(year)
# s3.select_by_index("5")

#
# from selenium import webdriver
# import select
#
# driver=webdriver.Chrome()
# driver.get("https://jqueryui.com/")
# driver.implicitly_wait(30)
# driver.find_element_by_xpath("//a[text()='Datepicker']").click()
# framewar=driver.find_element_by_xpath("//iframe[@class='demo-frame']")
# driver.switch_to_frame(framewar)
#
# driver.find_element_by_id("datepicker").click()
#
# month=driver.find_element_by_class_name("ui-datepicker-month")
# s1=select(month)
# s1.select_by_visible_text("Mar")
#
# year=driver.find_element_by_class_name("ui-datepicker-year")
# s2=select(year)
# s2.select_by_value("2010")
#
# driver.find_element_by_xpath("//a[text()='1']").click()





#
# from selenium import webdriver
# import select
#
# driver=webdriver.Chrome()
# driver.get("https://jqueryui.com/")
# driver.find_element_by_xpath("//a[text()='Datepicker']").click()
#
# framewar=driver.find_element_by_xpath("//iframe[@class='demo-frame']")
# driver.switch_to_frame(framewar)
#
# driver.find_element_by_id("datepicker").click()
#
# month=driver.find_element_by_class_name("ui-datepicker-month")
# s1=select(month)
# s1.select_by_visible_text("Mar")
#
# Year=driver.find_element_by_class_name("ui-datepicker-year")
# s2=select(year)
# s2.select_by_visible_value("2020")
#
# driver.find_element_by_xpath("//a[text()='1']").click()

#
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# driver=webdriver.Chrome()
# driver.get("https://jqueryui.com/")
# driver.find_element_by_xpath("//a[@href='https://jqueryui.com/droppable/']").click()
#
# frame_val=driver.find_element_by_xpath("//iframe[@class='demo-frame']")
# driver.switch_to_frame(frame_val)
#
# src_drag=driver.find_element_by_id("draggable")
#
# dest_drag=driver.find_element_by_id("droppable")
#
# a=ActionChains(driver)
# a.drag_and_drop(src_drag,dest_drag).perform()




# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# driver=webdriver.Chrome()
# driver.get("https://jqueryui.com/")
# driver.find_element_by_xpath("//a[text()='Droppable']").click()
# frame_val=driver.find_element_by_xpath("//iframe[@class='demo-frame']")
# driver.switch_to_frame(frame_val)
#
# src_drag=driver.find_element_by_id("draggable")
# dest_drag=driver.find_element_by_id("droppable")
#
# a=ActionChains(driver)
# a.drag_and_drop(src_drag,dest_drag).perform()


#
# from selenium import webdriver
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://phptravels.com/")
# time.sleep(30)
#
# driver.find_element_by_xpath("//span[text()='Login']").click()
#
# c_w=driver.current_window_handle
# w_h=driver.window_handles
#
# for i in w_h:
#     if i!=c_w:
#         driver.switch_to_window(i)
#
# driver.find_element_by_id("inputEmail").send_keys("Puneeth")

#
#
# from selenium import webdriver
# import time
#
# driver=webdriver.Chrome()
# driver.get("https://phptravels.com/")
# time.sleep(30)
#
# driver.find_element_by_xpath("//span[text()='Login']").click()
#
# c_w=driver.current_window_handle
# w_h=driver.window_handles
#
# for i in w_h:
#     if i!=c_w:
#         driver.switch_to_window(i)




