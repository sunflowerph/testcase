#coding=utf-8

#超市管理系统

from selenium import  webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import datetime



driver=webdriver.Chrome(executable_path='/Users/ph/Documents/chromedriver')
driver.get('http://118.25.66.69:8080/supermarket/login') #预发环境
#driver.get('http://saas.zhuisuyun.net/supermarket/login')  #线上
driver.implicitly_wait(5)

picture1='/Users/ph/Desktop/SAASproject/file/1.png'
picture2='/Users/ph/Desktop/SAASproject/file/2.png'
picture3='/Users/ph/Desktop/SAASproject/file/3.png'

#登录系统
def login(count,password): #参数：用户名、密码
    driver.find_element_by_xpath('//*[@id="form1"]/div[1]/input').send_keys(count) #输入账号
    driver.find_element_by_xpath('//*[@id="form1"]/div[2]/input').send_keys(password) #输入密码
    driver.find_element_by_xpath('//*[@id="form1"]/div[3]/div/button').click() #点击登录
 #time.sleep(3)

login("ddcs","1qazxsw2")  #预发环境
#login('ddcs','1qazxsw2') #线上



supplier1=u'供应商00001' #设置供应商名称
#添加供应商
def add_supplier(name,shortname,linkman,phonenumber,bizRegNumber,LawPerson,address):
    #参数：供应商名称、企业简称、联系人、联系方式、供商注册号、法人代表、地址
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[8]/a/span[1]').click() #点击供应商管理
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/aside/section/ul/li[8]/ul/li/a").click() #点击供应商管理子菜单
    driver.find_element_by_xpath('//*[@id="btnAdd"]').click()  #点击新增
    driver.find_element_by_xpath('//*[@id="entpName"]').send_keys(name)  #输入企业名称
    driver.find_element_by_xpath('//*[@id="entpShortName"]').send_keys(shortname) #输入简称
    driver.find_element_by_xpath('//*[@id="contactPerson"]').send_keys(linkman) #输入联系人
    driver.find_element_by_xpath('//*[@id="permanent"]').click() #证件有效期选择永久
    driver.find_element_by_xpath('//*[@id="contactDetail"]').send_keys(phonenumber) #输入联系方式
    driver.find_element_by_xpath('//*[@id="bizRegNumber"]').send_keys(bizRegNumber) #输入工商注册号
    driver.find_element_by_xpath('//*[@id="select2-entpType-container"]').click() #点击经营类型下拉框
    time.sleep(2)
  #  s1=Select(driver.find_element_by_id("select2-entpType-results"))
  #  s1.select_by_id('select2-entpType-result-7dcb-101')
    driver.find_element_by_xpath('//*[@class="select2-results__option"]').click() #选择其中一种经营类型
    driver.find_element_by_xpath('//*[@id="legalRepresentative"]').send_keys(LawPerson) #填写法人代表
    driver.find_element_by_xpath('//*[@id="select2-entpNature-container"]').click() #点击经营者性质下拉框
    time.sleep(3)
    driver.find_element_by_xpath('//*[@class="select2-results__option"]').click() #选择一种经营性质
    # driver.find_element_by_xpath('//*[@id="addEntpImg"]').click() #点击添加企业图片
    #time.sleep(3)
    # driver.switch_to.window('${win4943}')
    # driver.find_element_by_xpath('//*[@id="fileUpload"]').click()
    # driver.find_element_by_xpath('//*[@id="formFileUpload"]/div/div[1]/div[3]/div[1]').send_keys('QQ20190919_094243.png')
    # #上传企业图片
    # #点击上传按钮

    driver.find_element_by_xpath('//*[@id="baseForm"]/div/div[1]/div[2]/div[3]/div/div/div/div[4]/div/span/button').click()
    #点击地图
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="suggestId"]').send_keys(address) #输入地址
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="tangram-suggestion--TANGRAM__1m-item0"]/i').click() #选择定位到的地址
    driver.find_element_by_xpath('//*[@id="adressButton"]').click() #点击确认
    time.sleep(3)
    # driver.find_element_by_css_selector('html').send_keys(u'这是一段简介')
    driver.find_element_by_xpath('//*[@id="btnSave"]').click() #点击保存
    #time.sleep(4)


#add_supplier(supplier1,u"供商5",u"彭女士",'17301000000','123445958',u'法人彭女士',u'大渡河')
#add_supplier(supplier1,u"供商5",u'彭女士','17301000000','123445958',u'法人彭女士',u'大渡河')

#编辑供应商
def edit_supplier(supplier,linkerman1,short_name):
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[8]/a/span[1]').click()  # 点击供应商管理
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div/aside/section/ul/li[8]/ul/li/a").click()  # 点击供应商管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').clear()
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(supplier) #在搜索中填入要编辑的供应商名称
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[6]/button[1]').click() #点击编辑按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="contactPerson"]').clear()  # 清除原来的联系人信息
    driver.find_element_by_xpath('//*[@id="contactPerson"]').send_keys(linkerman1) #填写新的联系人信息
    driver.find_element_by_xpath('//*[@id="entpShortName"]').clear()  # 清除原来的企业简称
    driver.find_element_by_xpath('//*[@id="entpShortName"]').send_keys(short_name) #填写新的企业简称
    driver.find_element_by_xpath('//*[@id="btnSave"]').click() #点击保存按钮
    time.sleep(3)


#edit_supplier(supplier1,'17300023',u"供商3")



#删除供应商
def delete_supplier(supplier):
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[8]/a/span[1]').click()  # 点击供应商管理
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/aside/section/ul/li[8]/ul/li/a").click()  # 点击供应商管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').clear()
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(supplier)  # 在搜索中填入要删除的供应商名称
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()  # 点击搜索按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[6]/button[2]').click() #点击删除按钮
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]').click() #点击二次确认按钮
    time.sleep(3)

#delete_supplier(supplier1)



sku='sku00003' #产品sku

#新增产品(手动输入)

def add_goods(sku,name,brand,code,durabilityDay,supplier,entname,shelfLifeDay,price):
    #参数：sku、品名、品类、品牌、产品编码、保质期、供应商、生产企业名称、最佳口感期，单价
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/a/span[1]').click()#点击产品管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li/a').click() #点击产品管理子菜单
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="addProduct"]').click() #点击新增

    driver.find_element_by_xpath('//*[@id="productNo"]').send_keys(sku) #输入产品sku
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="productName"]').send_keys(name) #输入品名
    driver.find_element_by_xpath('//*[@id="selectInput"]/input[1]').click()  # 点击品类下拉框
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="choice"]/li[1]/span').click()  # 选择蔬菜
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="01231215"]').click()  # 扁豆种子
    driver.find_element_by_xpath('//*[@id="selectInput"]/input[1]').click()  # 点击品类下拉框
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="choice"]/li[1]/span').click()  # 选择蔬菜
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="01231215"]').click()  # 扁豆种子
    driver.find_element_by_xpath('//*[@id="productBrand"]').send_keys(brand) #输入品牌
    driver.find_element_by_xpath('//*[@id="productBrandCode"]').send_keys(code) # 输入品牌编码
    driver.find_element_by_xpath('//*[@id="durabilityDay"]').send_keys(durabilityDay) #输入保质期
    driver.find_element_by_xpath('//*[@id="product"]/div[1]/div/div/div[2]/div[1]/div[2]/div[5]/span/span[1]/span').click()
    #点击选择供应商下拉框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(supplier) #输入要选择的供应商
    driver.find_element_by_xpath('//*[@class="select2-results__option select2-results__option--highlighted"]').click() #选择输入的供应商
    driver.find_element_by_xpath('//*[@id="entpName"]').send_keys(entname) #输入生产企业名称
    driver.find_element_by_xpath('//*[@id="shelfLifeDay"]').send_keys(shelfLifeDay) #输入最佳口感期
    driver.find_element_by_xpath('//*[@id="product"]/div[1]/div/div/div[2]/div[1]/div[1]/div[10]/div[2]/div/span/span[1]/span').click()
    #点击选择单位输入框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(u'只')
    driver.find_element_by_xpath('//*[@class="select2-results__option select2-results__option--highlighted"]').click() #选择"只"
    driver.find_element_by_xpath('//*[@id="productPrice"]').send_keys(price) #输入价格
    driver.find_element_by_xpath('//*[@id="product"]/div[1]/div/div/div[2]/div[1]/div[1]/div[11]/div/span/span[1]/span').click()
    #点击选择产品等级输入框
    driver.find_element_by_xpath('//*[@class="select2-results__option select2-results__option--highlighted"]').click()
    #点击选择一等品
    '''
    driver.find_element_by_xpath('//*[@id="addPdtImg"]').click()# 点击产品图片添加按钮
    #切换到上传图片窗口
    handles=driver.window_handles
    for handle in handles:
        if handle != driver.current_window_handle:
            driver.switch_to.window(handle)
    driver.find_element_by_xpath('//*[@id="fileUpload"]').send_keys(picture1) #选择要上传的图片
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="formFileUpload"]/div/div[1]/div[3]/div[2]/a').click() #点击上传按钮
    time.sleep(3)
    handles1=driver.window_handles
    for handle in handles1:
        if handle != driver.current_window_handle:
            driver.switch_to.window(handle)

    driver.find_element_by_xpath('//*[@id="btnAddRow"]').click() #点击新增产品认证
    '''
    

    driver.find_element_by_xpath('//*[@id="Submit"]').click() #点击保存
    time.sleep(4)

#add_goods(sku,u'大西瓜',u"大品牌",'1823849','180',u"供应商03",u"企业名称","180",'23')


#编辑产品
def edit_goods(sku,productname):
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/a/span[1]').click()  # 点击产品管理
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li/a').click()  # 点击产品管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(sku) #输入要编辑商品的sku
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[10]/button[2]').click() #点击编辑按钮
    time.sleep(4)
    handles=driver.window_handles #获取当前两个窗口的句柄
    #切换到编辑窗口
    for handle in handles:
        if handle != driver.current_window_handle:
            driver.switch_to.window(handle)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="productName"]').clear() #清除原来的产品名称
    driver.find_element_by_xpath('//*[@id="productName"]').send_keys(productname) #填写新的产品名称
    driver.find_element_by_xpath('//*[@id="Submit"]').click() #点击保存按钮
    time.sleep(3)


#edit_goods(sku,u'新名')


#下架产品
def sold_out_goods(sku): #参数：sku
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/a/span[1]').click()  # 点击产品管理
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li/a').click()  # 点击产品管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(sku)  # 输入要编辑商品的sku
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()  # 点击搜索按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@class="btn btn-onSale btn-onSale-down"]').click() #点击下架按钮
    time.sleep(3)

#sold_out_goods(sku)

#上架产品
def putaway_goods(sku): #参数：sku
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/a/span[1]').click()  # 点击产品管理
    # time.sleep(3)
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li/a').click()  # 点击产品管理子菜单
    # driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(sku)  # 输入要编辑商品的sku
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()  # 点击搜索按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@class="btn btn-onSale btn-onSale-up"]').click()  # 点击上架按钮
    time.sleep(3)

#putaway_goods(sku)

#删除产品
def delete_goods(sku):
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/a/span[1]').click()  # 点击产品管理
    # time.sleep(3)
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li/a').click()  # 点击产品管理子菜单
    # driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(sku)  # 输入要编辑商品的sku
    # driver.find_element_by_xpath('//*[@id="btnSearch"]').click()  # 点击搜索按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="del"]').click() #点击删除按钮
    time.sleep(3)
    driver.find_element_by_css_selector('.modal-footer:nth-child(2) > .btn-primary').click() #二次确认
    time.sleep(3)

#delete_goods('sku')


#批量导入产品
def import_goods():
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/a/span[1]').click()  # 点击产品管理
    # time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li/a').click()  # 点击产品管理子菜单
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div/div[3]/div/button[2]').click()
    #点击excl批量导入
    handles=driver.window_handles
    for handle in handles:
        if handle !=driver.current_window_handle:
            driver.switch_to.window(handle)
    driver.find_element_by_xpath('//*[@id="fileUpload"]').send_keys('/Users/ph/Desktop/SAASproject/file/goods.xlsx')
    #导入模板
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="excelModal"]/div/div/div[2]/form/div/div[1]/div[3]/div[2]/a/i').click()
    #点击上传
    time.sleep(3)



#import_goods()

#标品导入
def import_bp():
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/a/span[1]').click()  # 点击产品管理
    # time.sleep(3)
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li/a').click()  # 点击产品管理子菜单
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div/div[3]/div/button[3]').click()
    #点击标品导入按钮
    handles = driver.window_handles
    #切换句柄
    for handle in handles:
        if handle != driver.current_window_handle:
            driver.switch_to.window(handle)
    driver.find_element_by_xpath('//*[@id="fileUploadBP"]').send_keys('/Users/ph/Desktop/SAASproject/file/templateBP.xlsx')
    #传入标品导入模板
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="excelModalBP"]/div/div/div[2]/form/div/div/div[3]/div[2]/a/span').click()
    #点击上传按钮
    time.sleep(3)

#import_bp()



#全选删除商品
def alldelete_goods(goods):
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/a/span[1]').click()  # 点击产品管理
    # time.sleep(3)
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li/a').click()  # 点击产品管理子菜单
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(goods) #输入要搜索的内容
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="table"]/thead/tr/th[1]/div[1]/input').click() #点击全选按钮
    driver.find_element_by_xpath('//*[@id="delect"]').click() #点击删除
    time.sleep(2)
    driver.find_element_by_css_selector(".modal-footer:nth-child(2) > .btn-primary").click() #点击二次确认按钮
    time.sleep(3)


#alldelete_goods(u"导入的商品")


#下载产品二维码-下载链接-下载全部

def download_RQ1():
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/a/span[1]').click()  # 点击产品管理
    # time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li/a').click()  # 点击产品管理子菜单
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="downloadProductQrCode"]').click() #点击下载产品二维码
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="downloadAll"]').click() #点击下载全部
    time.sleep(2)

#download_RQ1()



#下载产品二维码-下载链接-下载勾选数据
def download_RQ2():
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/a/span[1]').click()  # 点击产品管理
    # time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li/a').click()  # 点击产品管理子菜单
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[1]/input').click() #选择需要下载链接的数据
    driver.find_element_by_xpath('//*[@id="downloadProductQrCode"]').click() #点击下载产品二维码
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="downloadSelect"]').click() #点击下载勾选数据
    time.sleep(2)

#download_RQ2()

#下载产品二维码-下载图片-下载全部
def download_RQ3():
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/a/span[1]').click()  # 点击产品管理
    # time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li/a').click()  # 点击产品管理子菜单
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="downloadProductQrCode"]').click() #点击下载产品二维码
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="optionsRadios2"]').click() #点击下载图片
    driver.find_element_by_xpath('//*[@id="downloadAll"]').click() #点击下载全部
    time.sleep(2)

#download_RQ3()



#下载产品二维码-下载图片-下载勾选数据

def download_RQ4():
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/a/span[1]').click()  # 点击产品管理
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li/a').click()  # 点击产品管理子菜单
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[1]/input').click() #选择需要下载图片的数据
    driver.find_element_by_xpath('//*[@id="downloadProductQrCode"]').click() #点击下载产品二维码
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="optionsRadios2"]').click()  # 点击下载图片
    driver.find_element_by_xpath('//*[@id="downloadSelect"]').click() #点击下载勾选数据
    time.sleep(2)

#download_RQ4()



#通过产品链接查看产品H5信息
def goods_information():
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/a/span[1]').click()  # 点击产品管理
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[7]/ul/li/a').click()  # 点击产品管理子菜单
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys('sku000001') #输入要编辑商品的sku
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[10]/button[1]').click() #点击预览二维码
    time.sleep(3)
    text=driver.find_element_by_xpath('//*[@id="qrcode"]').get_attribute("value") #获取产品链接
    driver.get(text)
    time.sleep(10)
    text1=driver.find_element_by_xpath('//*[@id="productName"]/span').text
    if text1==u'毛豆zi' :
        print 'test_gj_goods_information test pass'
    else:
        print 'test_gj_goods_information test fail'
    driver.get('http://118.25.66.69:8080/supermarket/login')

#goods_information()








#修改企业基本信息
def edit_base_information(shortname,linkman,phone,law_person,address,picture1,picture2,picture3): #参数：企业简称、联系人、联系方式、法人代表、地址
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[9]/a/span[1]').click() #点击基础信息管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[9]/ul/li[1]/a').click() #点击基本信息管理
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="entpShortName"]').clear() #清除企业简称里的内容
    driver.find_element_by_xpath('//*[@id="entpShortName"]').send_keys(shortname) #输入新的企业简称
    driver.find_element_by_xpath('//*[@id="contactPerson"]').clear() #清除原来的联系人
    driver.find_element_by_xpath('//*[@id="contactPerson"]').send_keys(linkman) # 输入新的联系人
    driver.find_element_by_xpath('//*[@id="contactDetail"]').clear() #清除原来的联系方式
    driver.find_element_by_xpath('//*[@id="contactDetail"]').send_keys(phone) #输入新的联系方式
    driver.find_element_by_xpath('//*[@id="select2-entpType-container"]').click() #点击选择经营类型选择框
    driver.find_element_by_xpath('//*[@class="select2-results__option"]').click() #选择经营类型
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="select2-entpNature-container"]').click() #点击经营者性质栏
    time.sleep(2)
    driver.find_element_by_xpath('//*[@class="select2-results__option"]').click() #选择经营者性质
    driver.find_element_by_xpath('//*[@id="legalRepresentative"]').clear() #清除原来的法人代表
    driver.find_element_by_xpath('//*[@id="legalRepresentative"]').send_keys(law_person) #输入法人代表
    driver.find_element_by_xpath('//*[@id="baseForm"]/div/div[1]/div[2]/div[3]/div/div/div/div[4]/div/span/button').click()
    #点击地图按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="suggestId"]').send_keys(address) #输入地址
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="tangram-suggestion--TANGRAM__1m-item0"]/i/b').click() #选择匹配出的结果
    driver.find_element_by_xpath('//*[@id="adressButton"]').click() #点击确认
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="datetimepicker1"]/span/span').click()  # 点击备案日期选择框
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div[3]/table/tbody/tr[2]/td[5]')  # 选择备案日期
    driver.find_element_by_xpath('/html/body/div[2]/div[3]/table/tbody/tr[5]/td[5]').click() #点击保存按钮
    time.sleep(3)


    # driver.find_element_by_xpath('//*[@id="divProImg1088a4db71b5f844eedaca5d452f916b7251"]/div').click() #清除原来的企业图片
    # driver.find_element_by_xpath('//*[@id="addEntpImg"]').click()  #点击上传企业图片入口
    # time.sleep(2)
    # handles = driver.window_handles #切换句柄到当前窗口
    # for handle in handles:
    #     if handle !=driver.current_window_handle:
    #         driver.switch_to.window(handle)
    # time.sleep(3)
    # driver.find_element_by_xpath('//*[@id="fileUpload"]').send_keys(picture1) #选择上传图片
    # time.sleep(2)
    # driver.find_element_by_xpath('//*[@id="formFileUpload"]/div/div[1]/div[3]/div[2]/a/i').click() #点击上传
    # handles = driver.window_handles  # 切换句柄到当前窗口
    # for handle in handles:
    #     if handle != driver.current_window_handle:
    #         driver.switch_to.window(handle)
    # time.sleep(2)


    driver.find_element_by_xpath('//*[@id="btnSave"]').click() #点击保存按钮

#edit_base_information(u"信息发展",u"陈先生",'17300000001',u"法人代表",u"天安门",picture1,picture2,picture3)




name="ph" #设置员工姓名
#新增员工 (确认密码输入框未定位到)

def add_staff(name,mobile,post,psw): #参数：姓名、联系方式、岗位、密码
    #driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[9]/a/span[1]').click() #点击基础数据管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[9]/ul/li[2]/a').click() #点击员工信息管理
    driver.find_element_by_xpath('//*[@id="btnAdd"]').click() #点击添加
    driver.find_element_by_xpath('//*[@id="fullName"]').send_keys(name) #输如姓名
    driver.find_element_by_xpath('//*[@id="mobilePhone"]').send_keys(mobile) #输入手机号
    driver.find_element_by_xpath('//*[@id="post"]').send_keys(post) #输入岗位

    driver.find_element_by_xpath('//*[@id="employeepwd"]').send_keys(psw) #输入密码
    driver.find_element_by_css_selector('.form-group > #confirmaPssword').send_keys(psw) # 输入确认密码


    driver.find_element_by_xpath('//*[@id="btnSave"]').click() #点击保存按钮
    time.sleep(3)


#add_staff(name,"1212",u"一般文员","1qazxsw2")

#编辑员工信息
def edit_staff(name,post):
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[9]/a/span[1]').click()  # 点击基础数据管理
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[9]/ul/li[2]/a').click()  # 点击员工信息管理
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(name)
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[7]/button[1]').click()
    driver.find_element_by_xpath('//*[@id="post"]').clear()
    driver.find_element_by_xpath('//*[@id="post"]').send_keys(post)
    driver.find_element_by_xpath('//*[@id="btnSave"]').click()

#edit_staff(name,u"助理")

#删除员工
def delete_staff(name):
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[9]/a/span[1]').click()  # 点击基础数据管理
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[9]/ul/li[2]/a').click()  # 点击员工信息管理
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(name)
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
    time.sleep(3)
    driver.find_element_by_css_selector('tr:nth-child(1) .btn-danger').click()
    time.sleep(2)
    driver.find_element_by_css_selector('.btn-primary').click()

#delete_staff(name)



#手动添加进货登记
def stock_registration(supplier,registrant): #参数：供应商、登记人
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click() #点击进货登记
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click() #点击进货登记子菜单
    driver.find_element_by_xpath('//*[@id="add_new"]').click() #点击手动登记
    time.sleep(3)
    try:
        driver.find_element_by_xpath('//*[@id="konwit"]').click()
    except:
        pass
    driver.find_element_by_xpath('//*[@id="select2-supplierEntpId-container"]').click() #点击供应商下拉框
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(supplier) #输入要选择的供应商
    driver.find_element_by_xpath('//*[@class="select2-results__option select2-results__option--highlighted"]').click()
    #点击选择的供应商
    driver.find_element_by_xpath('//*[@id="select2-employeeId-container"]').click() #点击登记人下拉选择框
   # driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(registrant) #输入登记人
    driver.find_element_by_xpath('//*[@class="select2-results__option select2-results__option--highlighted"]').click()
    #选择输入的登记人
    driver.find_element_by_xpath('//*[@id="openProSelect"]').click()  #点击选择产品
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="addAllProduct"]').click()  #点击全部添加
    driver.find_element_by_xpath('//*[@id="sure"]').click() #点击选择产品中的保存按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="submit"]').click() #点击保存
    time.sleep(3)


#stock_registration(u"供应商03",'test')


#编辑进货登记
def edit_stock_registration(number):
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click()  # 点击进货登记
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click()  # 点击进货登记子菜单
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[7]/button[1]').click() #点击编辑按钮
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[10]/a').click()
    time.sleep(3)
    driver.find_element_by_css_selector('.input-sm').clear()
    driver.find_element_by_css_selector('.input-sm').send_keys(number)
    #填写产品数量
    driver.find_element_by_css_selector('.btn-primary').click()
    driver.find_element_by_xpath('//*[@id="submit"]').click()



#edit_stock_registration(100)


#删除进货登记
def delete_stock_registration():
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/a/span[1]').click()  # 点击进货登记
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[4]/ul/li/a').click()  # 点击进货登记子菜单
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[7]/button[2]').click() #点击删除按钮
    time.sleep(2)
    driver.find_element_by_css_selector('.btn-primary:nth-child(2)').click() #二次确认


#delete_stock_registration()

#通过二维码查看批次H5信息
def preview_rq():
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/a/span[1]').click() #点击批次管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[5]/ul/li/a').click() #点击批次管理子菜单
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="searchParam"]').send_keys('sku000001') #输入要搜索的批次产品的sku
    driver.find_element_by_xpath('//*[@id="searchBtn"]').click()#点击搜索按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[10]/button[1]').click()  # 点击预览二维码按钮
    time.sleep(3)
    text = driver.find_element_by_xpath('//*[@id="qrcode"]').get_attribute("value")  # 获取批次链接
    driver.get(text)
    time.sleep(10)
    text1 = driver.find_element_by_xpath('//*[@id="productName"]/span').text
    if text1 == u'毛豆zi':
        print 'test_k_goods_information test pass'
    else:
        print 'test_k_goods_information test fail'
    driver.get('http://118.25.66.69:8080/supermarket/login')

#preview_rq()

#新增检测报告
def add_testreport(testname,testnumber,tester):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/a/span[1]').click() #点击检测管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/ul/li/a').click() #点击检测报告管理
    driver.find_element_by_xpath('//*[@id="add"]').click() #点击新增
    driver.find_element_by_xpath('//*[@id="select2-detectionType-container"]').click() #点击检测类型下拉框
    driver.find_element_by_xpath('//*[@class="select2-results__option"]').click() #选择型式检测
    driver.find_element_by_xpath('//*[@id="detectionName"]').send_keys(testname) #输入检测名称
    driver.find_element_by_xpath('//*[@id="detectionNo"]').send_keys(testnumber) #输入检测编号

    time.sleep(3)
    #driver.find_element_by_xpath('//*[@class="select2-results__option select2-results__option--highlighted"]').click()
    #点击选择的检测员
    driver.find_element_by_xpath('//*[@id="openProSelect"]').click() #点击选择产品
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="pro000dc7b5-5a3a-40bb-9258-59b807e84abb"]/a/span').click() #点击添加
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sure"]').click() #点击选择产品里的保存
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="select2-employeeId-container"]').click()  # 点击检测员下拉框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(tester)  # 输入要选择的检测员
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="submit"]').click()# 点击保存
    time.sleep(3)


#add_testreport(u"检测名字啊",'112121','test')

#编辑检测报告
def edit_report(testname):#登记人没显示
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/a/span[1]').click()  # 点击检测管理
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/ul/li/a').click()  # 点击检测报告管理
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(testname) #输入要编辑的检测报告名称
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[7]/button[1]').click() #点击编辑按钮
    driver.find_element_by_xpath('//*[@id="detectionNo"]').clear()
    driver.find_element_by_xpath('//*[@id="detectionNo"]').send_keys('1343534232') #输入新的检测编号
    driver.find_element_by_xpath('//*[@id="submit"]').click() #点击保存


#edit_report(u"检测名字啊")


#删除检测报告
def delete_report(testname):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/a/span[1]').click()  # 点击检测管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[6]/ul/li/a').click()  # 点击检测报告管理
    driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(testname)  # 输入要编辑的检测报告名称
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[7]/button[2]').click() #点击删除按钮
    time.sleep(2)
    driver.find_element_by_css_selector('.btn-primary').click() #点击二次确认按钮

#delete_report(u"检测名字啊")



#添加销售记录
def add_SalesRecord(tester):
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/a/span[1]').click()  #点击销售记录
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/ul/li/a').click()  # 点击销售记录子菜单
    driver.find_element_by_xpath('//*[@id="add_new"]').click() #点击新增
    driver.find_element_by_xpath('//*[@id="openProSelect"]').click() #点击"批次出库"按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="pro00e14de7-b1af-4b42-8e09-823ec4fd7963"]/a/span').click() #选择一种产品

    driver.find_element_by_xpath('//*[@id="sure"]').click() #点击确认按钮
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="select2-employeeId-container"]').click() #点击选择登记人下拉框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(tester) #输入登记人
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER) #点击电脑enter建
    driver.find_element_by_xpath('//*[@id="submit"]').click() #点击保存按钮
    time.sleep(3)

#add_SalesRecord('test')

#编辑销售记录
def edit_SalesRecord(phonenumber):
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/a/span[1]').click()  # 点击销售记录
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/ul/li/a').click()  # 点击销售记录子菜单
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[7]/button[2]').click()
    driver.find_element_by_xpath('//*[@id="contactDetail"]').clear()
    driver.find_element_by_xpath('//*[@id="contactDetail"]').send_keys(phonenumber)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="submit"]').click()
    time.sleep(3)

#edit_SalesRecord('12344555')

#删除销售记录
def delete_SalesRecord():
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/a/span[1]').click()  # 点击销售记录
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/ul/li/a').click()  # 点击销售记录子菜单
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[7]/button[3]').click() #点击删除按钮
    time.sleep(2)
    driver.find_element_by_css_selector('.btn-primary:nth-child(2)').click()  # 点击二次确认按钮

#delete_SalesRecord()

#添加销售记录-文档导入
def import_txt():
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/a/span[1]').click()  # 点击销售记录
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/ul/li/a').click()  # 点击销售记录子菜单
    driver.find_element_by_xpath('//*[@id="toolbar"]/div/button[2]').click() #点击文档导入按钮
    handles = driver.window_handles
    for handle in handles:
        if handle != driver.current_window_handle:
            driver.switch_to.window(handle)
    driver.find_element_by_xpath('//*[@id="fileUpload"]').send_keys('/Users/ph/Desktop/SAASproject/file/outstock.xlsx')
    #选择导入的文件
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="excelModal"]/div/div/div[2]/form/div/div[1]/div[3]/div[2]/a/i').click()
    #点击上传按钮

#import_txt()

#查找出库记录，自定义搜索时间范围
def search_SalesRecord1(time1,time2):
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/a/span[1]').click()  # 点击销售记录
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/ul/li/a').click()  # 点击销售记录子菜单
    driver.find_element_by_xpath('//*[@id="whole"]/li[2]').click() #点击自定义按钮
    driver.find_element_by_xpath('//*[@id="dateStart"]').send_keys(time1) #输入开始时间
    driver.find_element_by_xpath('//*[@id="dateEnd"]').send_keys(time2) #输入结束时间
    driver.find_element_by_xpath('//*[@id="search"]').click() #点击搜索

#search_SalesRecord1('2019-08-13','2019-10-13')

#根据出库单号搜索销售记录
def search_SalesRecord2():
    #driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/a/span[1]').click()  # 点击销售记录
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/ul/li/a').click()  # 点击销售记录子菜单
    text=driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[2]').text
    driver.find_element_by_xpath('//*[@id="searchParam"]').send_keys(text)
    driver.find_element_by_xpath('//*[@id="search"]').click()
    time.sleep(2)
    text1=driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text



#search_SalesRecord2()







#打印销售记录（产品出库记录）
def print_SalesRecord():
    # driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/a/span[1]').click()  # 点击销售记录
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/aside/section/ul/li[3]/ul/li/a').click()  # 点击销售记录子菜单
    driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[7]/button[1]').click() #点击打印按钮
    time.sleep(2)
    handles=driver.window_handles
    for handle in handles:
        if handle!=driver.current_window_handle:
            driver.switch_to.window(handle)

#print_SalesRecord()



#预警信息导出（营业执照过期）
def warning_query1():
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/a/span[1]').click() #点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/ul/li/a').click() #点击预警查询
    time.sleep(3)
    driver.find_element_by_name('btSelectAll').click() #点击全选按钮
    driver.find_element_by_xpath('//*[@id="exportBtn"]').click() #点击导出按钮

#warning_query1()

#预警信息导出（食品经营许可证过期）
def warning_query2():
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/a/span[1]').click()  # 点击综合预警
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/ul/li/a').click()  # 点击预警查询
    driver.find_element_by_css_selector('#whole > .category_li:nth-child(3)').click() #选择食品经营许可证
    time.sleep(2)
    driver.find_element_by_name('btSelectAll').click()  #点击全选按钮  # 点击全选按钮
    driver.find_element_by_xpath('//*[@id="exportBtn"]').click()  # 点击导出按钮

#warning_query2()

#预警信息按时间从大到小排序
def orderby_time1():
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/a/span[1]').click()  # 点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/ul/li/a').click()  # 点击预警查询
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="tables"]/thead/tr/th[6]/div[1]').click() #点击时间
    time.sleep(2)
    a=driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[6]').text
    b=driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[2]/td[6]').text
    d1 = datetime.datetime.strptime(a, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(b, '%Y-%m-%d')

    if d1>=d2:
        print 'test_xb_orderby_time1 test pass'
    else:
        print 'test_xb_orderby_time1 test fail'

#orderby_time1()


#预警信息按时间从小到大排序
def orderby_time2():
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/a/span[1]').click()  # 点击综合预警
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/ul/li/a').click()  # 点击预警查询
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="tables"]/thead/tr/th[6]/div[1]').click() #点击时间
    time.sleep(2)
    a=driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[6]').text
    b=driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[2]/td[6]').text
    d1 = datetime.datetime.strptime(a, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(b, '%Y-%m-%d')

    if d1<=d2:
        print "test_xc_orderby_time2 test pass"
    else:
        print "test_xc_orderby_time2 test fail"

#orderby_time2()


#查看营业执照过期的全部供应商
def warning_view0():
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/a/span[1]').click()  # 点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/ul/li/a').click()  # 点击预警查询
    driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div/div[3]/ul/li[1]').click() #点击全部按钮
    time.sleep(2)

#warning_view0()

#查看营业执照即将在一个月内过期的供应商
def warning_view1():
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/a/span[1]').click()  # 点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/ul/li/a').click()  # 点击预警查询
    driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div/div[3]/ul/li[3]').click() #点击一个月
    time.sleep(2)

#warning_view1()

#查看营业执照即将在两个月内过期的供应商
def warning_view2():
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/a/span[1]').click()  # 点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/ul/li/a').click()  # 点击预警查询
    driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div/div[3]/ul/li[4]').click() #点击两个月
    time.sleep(2)

#warning_view2()

#查看营业执照即将在三个月内过期的供应商
def warning_view3():
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/a/span[1]').click()  # 点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/ul/li/a').click()  # 点击预警查询
    driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div/div[3]/ul/li[5]').click() #点击三个月
    time.sleep(2)

#warning_view3()

#查看食品经营许可证的全部供应商
def warning_view4():
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/a/span[1]').click()  # 点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/ul/li/a').click()  # 点击预警查询
    driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div/div[3]/ul/li[1]').click() #点击全部按钮
    driver.find_element_by_css_selector('#whole > .category_li:nth-child(3)').click()  # 选择食品经营许可证
    time.sleep(2)

#warning_view4()

#查看食品经营许可证即将在一个月内过期的供应商
def warning_view5():
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/a/span[1]').click()  # 点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/ul/li/a').click()  # 点击预警查询
    driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div/div[3]/ul/li[3]').click() #点击一个月
    driver.find_element_by_css_selector('#whole > .category_li:nth-child(3)').click()  # 选择食品经营许可证
    time.sleep(2)

#warning_view5()

#查看食品经营许可证即将在两个月内过期的供应商
def warning_view6():
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/a/span[1]').click()  # 点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/ul/li/a').click()  # 点击预警查询
    driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div/div[3]/ul/li[4]').click() #点击两个月
    driver.find_element_by_css_selector('#whole > .category_li:nth-child(3)').click()  # 选择食品经营许可证
    time.sleep(2)

#warning_view6()

#查看食品经营许可证即将在三个月内过期的供应商
def warning_view7():
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/a/span[1]').click()  # 点击综合预警
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[2]/ul/li/a').click()  # 点击预警查询
    driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div/div/div/div[3]/ul/li[5]').click() #点击三个月
    driver.find_element_by_css_selector('#whole > .category_li:nth-child(3)').click()  # 选择食品经营许可证
    time.sleep(2)


#warning_view7()

#产品管理-预览产品二维码
def preview_goodsrq():
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/a/span[1]').click() #点击产品管理
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/ul/li/a').click() #点击产品管理子菜单
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[10]/button[1]').click() #点击预览二维码
    time.sleep(2)
    # driver.find_element_by_xpath('//*[@id="qrcode"]').click()
    # driver.find_element_by_xpath('//*[@id="qrcode"]').send_keys(Keys.COMMAND+"a")
    # text=driver.find_element_by_xpath('//*[@id="qrcode"]').text #获取产品url
    # print text

#preview_goodsrq()

#产品列表中筛选预包装类型的产品
def product_type_1(type):
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/a/span[1]').click()  # 点击产品管理
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/ul/li/a').click()  # 点击产品管理子菜单
    driver.find_element_by_xpath('//*[@id="select2-productType-container"]').click() #点击产品类型下拉框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(type)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@class="select2-results__option select2-results__option--highlighted"]').click()


#product_type_1(u"预包装")

#产品列表中筛选散货类型的产品
def product_type_2(type):
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/a/span[1]').click()  # 点击产品管理
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/ul/li/a').click()  # 点击产品管理子菜单
    driver.find_element_by_xpath('//*[@id="select2-productType-container"]').click() #点击产品类型下拉框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(type)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@class="select2-results__option select2-results__option--highlighted"]').click()

#product_type_2(u"散货")


#产品列表中筛选标品类型的产品
def product_type_3(type):
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/a/span[1]').click()  # 点击产品管理
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[7]/ul/li/a').click()  # 点击产品管理子菜单
    driver.find_element_by_xpath('//*[@id="select2-productType-container"]').click() #点击产品类型下拉框
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(type)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@class="select2-results__option select2-results__option--highlighted"]').click()

#product_type_3(u"标品")


#查看首页批次数
def get_batch():
    driver.find_element_by_xpath('/html/body/div/header/a/span[2]/span').click() #点击首页logo
    time.sleep(3)
    batch_1=driver.find_element_by_xpath('//*[@id="batch"]/div/div[2]/div[2]/ul/li[1]').text #获取当天批次数
    batch_7=driver.find_element_by_xpath('//*[@id="batch"]/div/div[2]/div[2]/ul/li[2]').text #获取7天内批次数
    batch_30=driver.find_element_by_xpath('//*[@id="batch"]/div/div[2]/div[2]/ul/li[3]').text #获取首页30天批次数
    batch_365=driver.find_element_by_xpath('//*[@id="batch"]/div/div[2]/div[2]/ul/li[4]').text #获取整年内批次数
    batch_total=driver.find_element_by_xpath('//*[@id="batch"]/div/div[2]/div[2]/ul/li[5]').text #获取总批次数
    print batch_1,batch_7,batch_30,batch_365,batch_total


#get_batch()

#查看首页赋码数
def get_coding():
    driver.find_element_by_xpath('/html/body/div/header/a/span[2]/span').click()  # 点击首页logo
    time.sleep(3)
    coding_1=driver.find_element_by_xpath('//*[@id="coding"]/div/div[2]/div[1]/p').text #获取当天赋码数
    coding_7=driver.find_element_by_xpath('//*[@id="coding"]/div/div[2]/div[2]/ul/li[1]').text #获取7天内赋码数
    coding_30=driver.find_element_by_xpath('//*[@id="coding"]/div/div[2]/div[2]/ul/li[2]').text #获取30天内赋码数
    coding_365=driver.find_element_by_xpath('//*[@id="coding"]/div/div[2]/div[2]/ul/li[3]').text #获取整年内赋码数
    coding_total=driver.find_element_by_xpath('//*[@id="coding"]/div/div[2]/div[2]/ul/li[4]').text #获取总赋码数
    print coding_1,coding_7,coding_30,coding_365,coding_total

#get_coding()


#查看首页进货登记次数
def get_egistration():
    driver.find_element_by_xpath('/html/body/div/header/a/span[2]/span').click()  # 点击首页logo
    time.sleep(3)
    egistration_1=driver.find_element_by_xpath('//*[@id="purchaseRegistration"]/div/div[2]/div[2]/ul/li[1]').text
    egistration_7=driver.find_element_by_xpath('//*[@id="purchaseRegistration"]/div/div[2]/div[2]/ul/li[2]').text
    egistration_30=driver.find_element_by_xpath('//*[@id="purchaseRegistration"]/div/div[2]/div[2]/ul/li[3]').text
    egistration_365=driver.find_element_by_xpath('//*[@id="purchaseRegistration"]/div/div[2]/div[2]/ul/li[4]').text
    egistration_total=driver.find_element_by_xpath('//*[@id="purchaseRegistration"]/div/div[2]/div[2]/ul/li[5]').text
    print egistration_1,egistration_7,egistration_30,egistration_365,egistration_total

#get_egistration()

#获取首页产品数
def get_goods_number():
    driver.find_element_by_xpath('/html/body/div/header/a/span[2]/span').click()  # 点击首页logo
    time.sleep(3)
    goods_number_total=driver.find_element_by_xpath('//*[@id="product"]/div/div[2]/div[1]/p').text #获取总产品数
    goods_number_1=driver.find_element_by_xpath('//*[@id="product"]/div/div[2]/div[2]/ul/li[1]').text #获取top1产品数
    goods_number_2=driver.find_element_by_xpath('//*[@id="product"]/div/div[2]/div[2]/ul/li[2]').text #获取top2产品数
    goods_number_3=driver.find_element_by_xpath('//*[@id="product"]/div/div[2]/div[2]/ul/li[3]').text #获取top3产品数
    goods_number_4=driver.find_element_by_xpath('//*[@id="product"]/div/div[2]/div[2]/ul/li[4]').text #获取top4产品数
    goods_number_5=driver.find_element_by_xpath('//*[@id="product"]/div/div[2]/div[2]/ul/li[5]').text #获取top5产品数
    print goods_number_total,goods_number_1,goods_number_2,goods_number_3,goods_number_4,goods_number_5

#get_goods_number()

#获取首页供应商数
def get_supplier():
    driver.find_element_by_xpath('/html/body/div/header/a/span[2]/span').click()  # 点击首页logo
    time.sleep(3)
    supplier_number=driver.find_element_by_xpath('//*[@id="supplier"]/div/div[2]/div/p').text #获取供应商数
    print u"供应商数： "+supplier_number

#get_supplier()

#获取首页中散货数量
def get_bulk_cargo():
    driver.find_element_by_xpath('/html/body/div/header/a/span[2]/span').click()  # 点击首页logo
    time.sleep(3)
    bulk_cargo_number=driver.find_element_by_xpath('//*[@id="batch"]/div/div[2]/div[1]/div/span[1]').text #获取散货数量
    print u"散货数： "+bulk_cargo_number #打印散货数量
    time.sleep(3)

#get_bulk_cargo()

#获取首页中预包装货物数量
def get_prepackaging():
    driver.find_element_by_xpath('/html/body/div/header/a/span[2]/span').click()  # 点击首页logo
    time.sleep(3)
    prepackaging_number=driver.find_element_by_xpath('//*[@id="batch"]/div/div[2]/div[1]/div/span[2]').text #获取预包装数量
    print u"预包装数： "+prepackaging_number #打印预包装数量
    time.sleep(3)
#get_prepackaging()

#菜单收起
def close_menu():
    driver.find_element_by_xpath('/html/body/div/header/nav/a').click()
    time.sleep(3)

#close_menu()

#菜单展开
def open_menu():
    driver.find_element_by_xpath('/html/body/div/header/nav/a').click()
    time.sleep(3)

#open_menu()

