# coding=utf-8# python练习import android_capsfrom time import sleepimport sysreload(sys)sys.setdefaultencoding('utf-8')print "< 登录流程end,进入圈子start >"android_caps.self.find_element_by_id("maintab_layout_profile").click()  # 点击个人帧# check 圈子通知数量try:    android_caps.self.find_element_by_id("new_quanzi_bubble").is_displayed()    quanzi_bubble = android_caps.self.find_element_by_id("new_quanzi_bubble").text    print "$ 圈子通知数:" + quanzi_bubble    android_caps.self.find_element_by_id("quanzi_layout").click()  # 点击圈子入口    sleep(15)    btn_bubble = android_caps.self.find_element_by_id("group_btn_bubble").text    if btn_bubble == quanzi_bubble:        print "$ 个人帧圈子通知数量与圈子内通知数量相同"        sleep(5)        android_caps.self.find_element_by_id("group_btn_bubble").click()        sleep(5)        try:            android_caps.self.find_element_by_id("item_layout").is_displayed()            print "$ 圈子通知展示正确"            android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()            sleep(3)        except:            print "$ 圈子通知展示不正确.."            android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()            sleep(3)    else:        print "$ 个人帧圈子通知数量与圈子内通知数量不相同!!..."except:    print "$ 没有圈子通知"    android_caps.self.find_element_by_id("quanzi_layout").click()  # 点击圈子入口    sleep(15)