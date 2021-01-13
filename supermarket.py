#coding=utf-8
#qitade
#超市管理系统

import unittest
import base
import time
import datetime



#添加

class TestMarket(unittest.TestCase):

#新增供应商
    def test_ab_add_supplier(self):
        test_add_suuplier = base.add_supplier(base.supplier1,u"供商5",u'彭女士','17301000000','123445958',u'法人彭女士',u'大渡河')
        #执行新增供应商操作
        time.sleep(3)
        base.driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(base.supplier1) #在列表中搜索该供应商
        base.driver.find_element_by_xpath('//*[@id="btnSearch"]').click() #点击搜索按钮
        text=base.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td[2]').text #获取搜索出来的供应商名称
        #断言：新增的供应商是否存在
        try:
            assert text==base.supplier1
            print " test_ab_add_supplier test pass"
        except:
            print "test_ab_add_supplier test fail"
        time.sleep(3)

#编辑供应商
    def test_b_edit_supplier(self):
        test_edit_supplier = base.edit_supplier(base.supplier1, '17300023', u"供商3") #执行编辑供应商操作
        time.sleep(2)
        text=base.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[3]').text #获取联系人信息
        #断言：联系人是否是改过之后的
        try:
            assert text=="17300023"
            print " test_b_edit_supplier test pass"
        except:
            print "test_b_edit_supplier test fail"
        time.sleep(3)

#删除供应商
    def test_l_delete_supplier(self):
        test_delete_supplier =base.delete_supplier(base.supplier1) #执行删除供应商操作
        time.sleep(2)
        # 断言："没有找到匹配的记录"元素是否存在
        try:
            base.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td')
            print "test_l_delete_supplier test pass"
        except:
            print "test_l_delete_supplier test fail"
        time.sleep(3)


#新增产品
    def test_d_add_goods(self):
        test_add_goods = base.add_goods(base.sku,u'大毛豆',u'毛豆',u"大品牌",'1823849','180',base.supplier1,u"企业名称","180",'23')
        #新增产品操作
        time.sleep(2)
        text=base.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text #获取新增产品sku
        #断言：该sku的新增产品是否存在
        try:
            assert text==base.sku
            print " test_d_add_goods test pass"
        except:
            print "test_d_add_goods test fail"
        time.sleep(3)

#编辑产品
    def test_e_edit_goods(self):
        test_eidt_goods = base.edit_goods(base.sku, u'新名') #编辑产品操作
        text=base.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text #获取该产品更改后的产品名
        #断言该产品名是否是更改后的
        try:
            assert text == u"新名"
            print " test_e_edit_goods test pass"
        except:
            print "test_e_edit_goods test fail"
        time.sleep(3)

#下架产品
    def test_f_sold_out_goods(self):
        test_sold_out_goods = base.sold_out_goods(base.sku) #下架产品操作
        #断言是否看到"上架"按钮
        try:
            base.driver.find_element_by_xpath('//*[@class="btn btn-onSale btn-onSale-up"]').text
            print "test_f_sold_out_goods test pass"
        except:
            print "test_f_sold_out_goodst fail"
        time.sleep(3)

#上架产品
    def test_ga_putaway_goods(self):
        test_putaway_goods = base.putaway_goods(base.sku) #上架产品操作
        #断言是否看到"下架"按钮
        try:
            base.driver.find_element_by_xpath('//*[@class="btn btn-onSale btn-onSale-down"]').text
            print "test_ga_putaway_goods test pass"
        except:
            print "test_ga_putaway_goods fail"
        time.sleep(3)

#删除商品
    def test_gb_delete_goods(self):
        test_delete_goods = base.delete_goods(base.sku)
        try:
            base.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td') #是否出现"没有找到匹配的记录"字段
            print "test_gb_delete_goods test pass"
        except:
            print "test_gb_delete_goods fail"
        time.sleep(3)

#批量导入产品
    def test_gc_import_goods(self):
        test_import_goods =base.import_goods()
        try:
            goods1=base.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text
            goods2=base.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text
            goods3=base.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[4]').text
            assert u"导入的商品" in goods1 and u"导入的商品" in goods2 and u"导入的商品" in goods3
            print 'test_gc_import_goods test pass'
        except:
            print "test_gc_import_goods test fail"
        time.sleep(3)


#标品导入
    def test_gd_import_bp(self):
        test_import_bp = base.import_bp()
        try:
            goods=base.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text
            assert  goods==u"导入的商品标品"
            print "test_gd_import_bp test pass"
        except:
            print "test_gd_import_bp test fail"



#全选删除产品
    def test_ge_alldelete_goods(self):
        test_alldelete_goods =base.alldelete_goods(u"导入的商品")
        time.sleep(3)
        try:
            text=base.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text
            assert text == u"没有找到匹配的记录"
            print "test_ge_alldelete_goods test pass"
        except:
            print "test_ge_alldelete_goods test fail"
        time.sleep(3)

#下载产品二维码-下载链接-下载全部

    def test_gf_download_RQ1(self):
        try:
            test_download_RQ1 = base.download_RQ1()
            print "test_gf_download_RQ1 test pass"
        except:
            print "test_gf_download_RQ1 test fail"
        time.sleep(3)

#下载产品二维码-下载链接-下载勾选数据
    def test_gg_download_RQ2(self):
        try:
            test_download_RQ2 =base.download_RQ2()
            print "test_gg_download_RQ2 test pass"
        except:
            print "test_gg_download_RQ2 test fail"
        time.sleep(3)


#下载产品二维码-下载图片-下载全部
    def test_gh_download_RQ3(self):
        try:
            test_download_RQ3 =base.download_RQ3()
            print "test_gh_download_RQ3 test pass"
        except:
            print "test_gh_download_RQ3 test fail"
        time.sleep(3)

#下载产品二维码-下载图片-下载勾选数据
    def test_gi_download_RQ4(self):
        try:
            test_download_RQ4 = base.download_RQ4()
            print "test_gi_download_RQ4 test pass"
        except:
            print "test_gi_download_RQ4 test fail"
        time.sleep(3)

# 通过产品链接查看产品H5信息
    def test_gj_goods_information(self):
        try:
            base.goods_information()
        except:
            print 'test_gj_goods_information test fail'



#手动添加进货登记
    def test_h_stock_registration(self):
        try:
            test_stock_registration = base.stock_registration('供应商03', 'test')
            print "test_h_stock_registration test pass"
        except:
            print "test_h_stock_registration test fail"
        time.sleep(4)

#编辑进货登记
    def test_i_edit_stock_registration(self):
        try:
            test_edit_Stock_registration = base.edit_stock_registration(100)
            print 'test_i_edit_stock_registration test pass'
        except:
            print "test_i_edit_stock_registration test fail"
        time.sleep(3)


#删除进货登记
    def test_j_delete_stock_registration(self):
        try:
            test_delete_stock_registration = base.delete_stock_registration()
            print "test_j_delete_stock_registration test pass"
        except:
            print "test_j_delete_stock_registration test fail"
        time.sleep(3)

#查看批次管理
    def test_k_preview_rq(self):
        try:
            test_preview_rq =base.preview_rq()
        except:
            print "test_k_preview_rq fail"
        time.sleep(3)

#新增检测报告
    def test_m_add_testreport(self):
        test_add_testreport = base.add_testreport(u"检测名字啊", '112121', 'test')
        text=base.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]').text
        try:
            assert text==u"检测名字啊"
            print "test_m_add_testreport test pass"
        except:
            print "test_m_add_testreport test fail"
        time.sleep(3)

#编辑检测报告
    def test_n_edit_report(self):
        try:
            test_edit_testreport=base.edit_report(u"检测名字啊")
            print "test_n_edit_report test pass"
        except:
            print "test_n_edit_report test fail"
        time.sleep(3)

#删除检测报告
    def test_o_delete_report(self):
        test_delete_report = base.delete_report(u"检测名字啊")
        time.sleep(2)
        base.driver.find_element_by_xpath('//*[@id="searchbox"]').clear()
        base.driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys(u"检测名字啊")
        base.driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
        time.sleep(2)
        try:
            base.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td')
            print "test_o_delete_report test pass"
        except:
            print "test_o_delete_report test fail"
        time.sleep(3)

#新增销售记录
    def test_p_add_SalesRecord(self):
        try:
            add_salesrecord = base.add_SalesRecord('test')
            print "test_p_add_SalesRecord test pass"
        except:
            print "test_p_add_SalesRecord test fail"
        time.sleep(3)


#编辑销售记录
    def test_q_edit_SalesRecord(self):
        # text=base.driver.find_element_by_css_selector('#tables tr:nth-child(1) > td:nth-child(6)').text
        # print text
        try:
            test_edit_SalesRecord = base.edit_SalesRecord('17300000000')
            print "test_q_edit_SalesRecord test pass"
        except:
            print "test_q_edit_SalesRecord test fail"
        time.sleep(3)


#删除销售记录
    def  test_ra_delete_SalesRecord(self):
        try:
            test_delete_SalesRecord =base. delete_SalesRecord()
            print "test_ra_delete_SalesRecord test pass"
        except:
            print "test_ra_delete_SalesRecord test fail"
        time.sleep(3)


#添加销售记录-文档导入
    def test_rb_import_txt(self):
        try:
            test_import_txt=base.import_txt()
            print "test_rb_import_txt test pass"
        except:
            print "test_rb_import_txt test fail"


# 查找出库记录，自定义搜索时间范围
    def test_rc_search_SalesRecord1(self):
        base.search_SalesRecord1('2019-08-13', '2019-10-13')
        try:
            time0=base.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[3]').text #获取搜索结果的出库时间
            time0 = datetime.datetime.strptime(time0, '%Y-%m-%d')
            time1=datetime.datetime.strptime('2019-08-13', '%Y-%m-%d')
            time2=datetime.datetime.strptime('2019-10-13', '%Y-%m-%d')
            assert time1<=time0<=time2
            print 'test_rc_search_SalesRecord test pass'
        except:
            try:
                base.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td')
                print 'test_rc_search_SalesRecord test pass'
            except:
                print 'test_rc_search_SalesRecord test fail'

        time.sleep(3)



#根据出库单号搜索销售记录
    def test_rd_search_SalesRecord2(self):
        try:
            base.search_SalesRecord2()
            print 'test_rd_search_SalesRecord2 test pass'
        except:
            print 'test_rd_search_SalesRecord2 test fail'


#打印后找不到原窗口
# # 打印销售记录（产品出库记录）
#     def test_rc_print_SalesRecord(self):
#         test_print_SalesRecord =base.print_SalesRecord()
#         time.sleep(3)
#         try:
#             base.driver.find_element_by_xpath('//*[@id="plugin"]')
#             print 'test_rc_print_SalesRecord test pass'
#         except:
#             print 'test_rc_print_SalesRecord test fail'
#         handles = base.driver.window_handles
#         for handle in handles:
#             if handle != base.driver.current_window_handle:
#                 base.driver.switch_to.window(handle)
#         time.sleep(3)



#修改企业基本信息 #参数：企业简称、联系人、联系方式、法人代表、地址
    def test_s_edit_base_information(self):
        try:
            test_edit_base_information = base.edit_base_information\
                (u"中信信息",u"张先生","17309902930",u'刘先生',u"迪士尼",base.picture3,base.picture2,base.picture1)
            print "test_s_edit_base_information test pass"
        except:
            print "test_s_edit_base_information test fail"
        time.sleep(2)

#新增员工
    def test_t_add_staff(self):
        test_add_staff = base.add_staff(base.name, "11740392922", u"一般文员", "1qazxsw2")
        text=base.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[2]').text
        try:
            assert text=="ph"
            print "test_t_add_staff test pass"
        except:
            print "test_t_add_staff test fail"
        time.sleep(2)

#编辑员工信息
    def test_u_edit_staff(self):
        test_edit_staff =base.edit_staff(base.name, u"助理")
        time.sleep(2)
        text=base.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr[1]/td[4]').text
        try:
            assert text==u"助理"
            print "test_t_edit_staff test pass"
        except:
            print "test_t_edit_staff test fail"

        time.sleep(2)

#删除员工
    def test_v_delete_staff(self):
        test_delete_staff = base.delete_staff(base.name)
        time.sleep(2)
        base.driver.find_element_by_xpath('//*[@id="searchbox"]').clear()
        base.driver.find_element_by_xpath('//*[@id="searchbox"]').send_keys('ph')
        base.driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
        try:
            base.driver.find_element_by_xpath('//*[@id="tables"]/tbody/tr/td')
            print 'test_v_delete_staff test pass'
        except:
            print 'test_v_delete_staff test fail'
        time.sleep(3)

#查看预警信息(营业执照过期）
    def test_w_warning_query1(self):
        try:
            test_warning_query1 = base.warning_query1()
            print "test_w_warning_query1 test pass"
        except:
            print 'test_w_warning_query1 test fail'

        time.sleep(2)


#查看预警信息（食品经营许可证过期）
    def test_xa_warning_query2(self):
        try:
            test_warning_query1 = base.warning_query2()
            print "test_w_warning_query2 test pass"
        except:
            print 'test_w_warning_query2 test fail'
        time.sleep(2)

#预警信息按时间从大到小排序
    def test_xb_orderby_time1(self):
        test_orderby_time = base.orderby_time1()
        time.sleep(2)



#预警信息按时间从小到大排序
    def test_xc_orderby_time2(self):
        test_orderby_time = base.orderby_time2()
        time.sleep(2)

#查看营业执照过期的全部供应商
    def test_xd_warning_view0(self):
        try:
            test_warning_view0 =base.warning_view0()
            print 'test_xd_warning_view0 test pass'
        except:
            print 'test_xd_warning_view0 test fail'
        time.sleep(2)

#查看营业执照即将在一个月内过期的供应商
    def test_xe_warning_view1(self):
        try:
            test_warning_view1 =base.warning_view1()
            print 'test_xe_warning_view1 test pass'
        except:
            print 'test_xe_warning_view1 test fail'
        time.sleep(2)



#查看营业执照即将在两个月内过期的供应商
    def test_xf_warning_view2(self):
        try:
            test_warning_view2 =base.warning_view2()
            print 'test_xf_warning_view2 test pass'
        except:
            print 'test_xf_warning_view2 test fail'
        time.sleep(2)

#查看营业执照即将在三个月内过期的供应商
    def test_xg_warning_view3(self):
        try:
            test_warning_view3 =base.warning_view3()
            print 'test_xg_warning_view3 test pass'
        except:
            print 'test_xg_warning_view3 test fail'
        time.sleep(2)

#查看食品经营许可证的全部供应商
    def test_xh_warning_view4(self):
        try:
            test_warning_view4 =base.warning_view4()
            print 'test_xh_warning_view4 test pass'
        except:
            print 'test_xh_warning_view4 test fail'
        time.sleep(2)

#查看食品经营许可证即将在一个月内过期的供应商
    def test_xi_warning_view5(self):
        try:
            test_warning_view5 =base.warning_view5()
            print 'test_xi_warning_view5 test pass'
        except:
            print 'test_xi_warning_view5 test fail'
        time.sleep(2)

#查看食品经营许可证即将在两个月内过期的供应商
    def test_xj_warning_view6(self):
        try:
            test_warning_view6 =base.warning_view6()
            print 'test_xj_warning_view6 test pass'
        except:
            print 'test_xj_warning_view6 test fail'
        time.sleep(2)

#查看食品经营许可证即将在三个月内过期的供应商
    def test_xk_warning_view7(self):
        try:
            test_warning_view7 =base.warning_view7()
            print 'test_xk_warning_view7 test pass'
        except:
            print 'test_xk_warning_view7 test fail'
        time.sleep(2)

#预览产品二维码
    def test_y_preview_goodsrq(self):
        test_preview_goodsrq =base. preview_goodsrq()
        try:
            base.driver.find_element_by_xpath('//*[@id="qrcodes"]/canvas') #定位二维码元素
            base.driver.find_element_by_xpath('//*[@id="qrcodeModal"]/div/div/div[1]/button').click() #点击右上角取消
            print 'test_y_preview_goodsrq test pass'
        except:
            print 'test_y_preview_goodsrq test fail'
        time.sleep(3)

#产品列表中筛选预包装类型的产品
    def test_z_product_type_1(self):
        test_product_type1 = base.product_type_1(u"预包装")
        time.sleep(3)
        text=base.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text #查看列表中产品的包装类型
        try:
            assert text==u'预包装'
            print 'test_z_product_type_1 test pass'
        except:
            print 'test_z_product_type_1 test fail'
        time.sleep(3)

#产品列表中筛选散货类型的产品
    def test_za_product_type_2(self):
        test_product_type2 = base.product_type_2(u"散货")
        time.sleep(3)
        text=base.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text #查看列表中产品的包装类型
        try:
            assert text==u'散货'
            print 'test_za_product_type_2 test pass'
        except:
            print 'test_za_product_type_2 test fail'
        time.sleep(3)


#产品列表中筛选标品类型的产品
    def test_zb_product_type_3(self):
        test_product_type3 =base.product_type_3(u"标品")
        time.sleep(3)
        text = base.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text #查看列表中产品的包装类型
        try:
            assert text==u'标品'
            print 'test_zb_product_type_3 test pass'
        except:
            print 'test_zb_product_type_3 test fail'
        time.sleep(3)

#查看首页批次数
    def test_zc_get_batch(self):
        try:
            test_get_batch_ = base.get_batch()
            print "test_zc_get_batch test pass"
        except:
            print "test_zc_get_batch test fail"
        time.sleep(3)

#查看首页赋码数
    def test_zd_get_coding(self):
        try:
            test_get_coding = base.get_coding()
            print "test_zd_get_coding test pass"
        except:
            print "test_zd_get_coding test fail"
        time.sleep(3)

#查看首页进货登记次数
    def test_ze_get_egistration(self):
        try:
            test_get_egistration = base.get_egistration()
            print "test_ze_get_egistration test pass"
        except:
            print "test_ze_get_egistration test"

        time.sleep(3)

#获取首页产品数
    def test_zf_get_goods_number(self):
        try:
            test_get_goods_numbe =base.get_goods_number()
            print "test_zf_get_goods_number test pass"
        except:
            print "test_zf_get_goods_number test fail"

        time.sleep(3)

#获取首页供应商数
    def test_zg_get_supplier(self):
        try:
            test_get_supplier =base.get_supplier()
            print "test_zg_get_supplier test pass"
        except:
            print "test_zg_get_supplier test fail"
        time.sleep(3)

#获取首页中散货数量
    def test_zh_get_bulk_cargo(self):
        try:
            test_get_bulk_cargo = base.get_bulk_cargo()
            print "test_zh_get_bulk_cargo test pass"
        except:
            print "test_zh_get_bulk_cargo test fail"
        time.sleep(3)

#获取首页中预包装货物数量
    def test_zi_get_prepackaging(self):
        try:
            test_get_prepackaging =base. get_prepackaging()
            print "test_zi_get_prepackaging test pass"
        except:
            print "test_zi_get_prepackaging test fail"
        time.sleep(3)


#菜单收起
    def test_zj_close_menu(self):
        test_close_menu = base.close_menu()
        time.sleep(3)
        try:
            assert base.driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[1]').text ==u"菜单"
            #如果能找到"菜单"这个元素说明菜单收起失败
            print "test_zj_close_menu test fail"
        except:
            print "test_zj_close_menu test pass"
        time.sleep(3)



#菜单展开
    def test_zk_open_menu(self):
        test_open_menu =base.open_menu()
        time.sleep(3)
        try:
            base.driver.find_element_by_xpath('/html/body/div/aside/section/ul/li[1]') #如果能找到"菜单"这个元素说明菜单打开成功
            print "test_zk_open_menu test pass"
        except:
            print "test_zk_open_menu test fail"
        time.sleep(3)



#登录账号验证
    def test_zl_check_account(self):
        time.sleep(2)
        account =base.driver.find_element_by_xpath('//*[@id="passwordFrom"]/div/ul/li[1]/a/span').text
        try:
            assert account==u"陈唯"
            print "test_zl_check_account test pass"
        except:
            print "test_zl_check_account test fail"


#用例执行完毕后退出浏览器
    # def test_zm_quit(self):
    #     base.driver.quit()


if __name__ =="__main__":
    unittest.main()

