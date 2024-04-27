####Author: https://github.com/Aochen-Sun/
####Version: 1.0
####Date: 04/27/2024

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd


####基于chrome driver
mobile_emulation = {"deviceName": "iPhone 6"}
options = Options()
options.add_experimental_option("mobileEmulation", mobile_emulation)

driver =webdriver.Chrome(options = options)
driver.get('https://dorm.xmu.edu.cn/zsgl/student/web/#/home')

username = input("请输入用户名:")
password = input("请输入密码:")
driver.find_element(by=By.XPATH, value= '//*[@id="username"]').send_keys(username)
driver.find_element(by=By.XPATH, value= '//*[@id="password"]').send_keys(password)
driver.find_element(by=By.XPATH, value= '//*[@id="login_submit"]').click()
driver.get('https://dorm.xmu.edu.cn/zsgl/student/web/#/home')
time.sleep(0.3)
if driver.find_elements(By.CLASS_NAME, "van-grid-item__text"):
    print("登陆成功")
else:
    print("登陆失败，请重试")

####在block_list中配置目标楼栋，以海韵1~海韵17为例
block_list = ['0901','0902','0903','0904','0905','0906','0907','0908',
              '0809','0810','0811','0812','0813','0814','0815','0816','0817']
dfs=[]
for i in block_list:
    for j in range(1,8):
        url= f"https://dorm.xmu.edu.cn/zsgl/student/web/#/mark/markroom?sslid={i}&floor={j}&batchid=1"
        driver.get(url)
        driver.refresh()
        time.sleep(0.5)
        room_title = driver.find_elements(by=By.CLASS_NAME, value='mark_0')
        room_status = driver.find_elements(by=By.TAG_NAME, value='span')
        title_list = [element.text for element in room_status]
        status_list = [element.text for element in room_status]
        title_list = title_list[1::2][:-1]
        status_list = status_list[2::2]
        df = pd.DataFrame({'title': title_list,'blockID': i, 'status': status_list})
        dfs.append(df)
aggregate_df = pd.concat(dfs, ignore_index=True)
new_df = aggregate_df['title'].str.split('-', expand=True)
new_df.columns = ['Block', 'Room']
aggregate_df = pd.concat([new_df, aggregate_df], axis=1)
aggregate_df.drop(columns=['title'], inplace=True)
aggregate_df = aggregate_df[aggregate_df['status'] != '空房']
aggregate_df.drop(columns=['status'], inplace=True)
del df, dfs, i, j, block_list, new_df, room_status, room_title, status_list, title_list, url, username, password

for Room, blockID in zip(aggregate_df['Room'], aggregate_df['blockID']):
    url=f"https://dorm.xmu.edu.cn/zsgl/student/web/#/mark/marking?batchid=1&fjh={blockID}0{Room}&ismark=1"
    driver.get(url)
    ####send_keys()中修改分数
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[1]/div[2]/div/div[2]/div[2]/div/input').clear() #这一步是根据xpath找到元素并清空
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[1]/div[2]/div/div[2]/div[2]/div/input').send_keys('10')
    
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[1]/div[15]/div/div[2]/div/div[2]/div[1]/input').clear() #这一步是根据xpath找到元素并清空
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[1]/div[15]/div/div[2]/div/div[2]/div[1]/input').send_keys('10')
    
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[2]/div[3]/div/div/div/div/div/div[2]/div[1]').click()
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[2]/div[4]/div/div/div/div/div/div[2]/div[1]').click()
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[2]/div[5]/div/div/div/div/div/div[2]/div[1]').click()
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[2]/div[6]/div/div/div/div/div/div[2]/div[1]').click()
    
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[3]/div[7]/div/div[2]/div/div[2]/div[1]/input').clear() #这一步是根据xpath找到元素并清空
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[3]/div[7]/div/div[2]/div/div[2]/div[1]/input').send_keys('10')
    
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[3]/div[8]/div/div[2]/div/div[2]/div[1]/input').clear() #这一步是根据xpath找到元素并清空
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[3]/div[8]/div/div[2]/div/div[2]/div[1]/input').send_keys('5')
    
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[3]/div[9]/div/div[2]/div/div[2]/div[1]/input').clear() #这一步是根据xpath找到元素并清空
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[3]/div[9]/div/div[2]/div/div[2]/div[1]/input').send_keys('9')
    
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[3]/div[10]/div/div[2]/div/div[2]/div[1]/input').clear() #这一步是根据xpath找到元素并清空
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[3]/div[10]/div/div[2]/div/div[2]/div[1]/input').send_keys('9')
    
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[3]/div[11]/div/div[2]/div/div[2]/div[1]/input').clear() #这一步是根据xpath找到元素并清空
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[3]/div[11]/div/div[2]/div/div[2]/div[1]/input').send_keys('1')
    
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[3]/div[12]/div/div[2]/div/div[2]/div[1]/input').clear() #这一步是根据xpath找到元素并清空
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[3]/div[12]/div/div[2]/div/div[2]/div[1]/input').send_keys('5')
    
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[3]/div[13]/div/div[2]/div/div[2]/div[1]/input').clear() #这一步是根据xpath找到元素并清空
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[3]/div[13]/div/div[2]/div/div[2]/div[1]/input').send_keys('5')
    
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[4]/div[2]/div[4]/div[2]/div[1]/textarea').send_keys('宿舍整体卫生状况良好，大部分区域保持清洁。地面和桌面定期打扫，床铺整洁。但部分角落可能存在灰尘积累，需要加强细节处理。')
    
    driver.find_element(by=By.XPATH, value= '//*[@id="app"]/div/div[3]/form/div[6]').click()

driver.quit()