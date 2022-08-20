# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException    #导入NoSuchElementException

browser = webdriver.Chrome()

browser.get("https://portal.gdc.cancer.gov/exploration?cases_size=100&filters=%7B%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22breast%22%5D%7D%2C%22op%22%3A%22in%22%7D%2C%7B%22content%22%3A%7B%22field%22%3A%22cases.diagnoses.tissue_or_organ_of_origin%22%2C%22value%22%3A%5B%22axillary%20tail%20of%20breast%22%2C%22breast%2C%20nos%22%2C%22central%20portion%20of%20breast%22%2C%22lower-inner%20quadrant%20of%20breast%22%2C%22lower-outer%20quadrant%20of%20breast%22%2C%22nipple%22%2C%22overlapping%20lesion%20of%20breast%22%2C%22upper-inner%20quadrant%20of%20breast%22%2C%22upper-outer%20quadrant%20of%20breast%22%5D%7D%2C%22op%22%3A%22in%22%7D%5D%2C%22op%22%3A%22and%22%7D")
time.sleep(3)

accept = browser.find_element_by_xpath( '/html/body/div[4]/div/div/div/div[2]/button')

accept.click()

trlist = browser.find_elements_by_tag_name("tr")

url_list = []

for i in range(0,len(trlist)-2):
    ID_num = "row-" + str(i) + "-case-link"
    ID_link = browser.find_element_by_id(ID_num).get_attribute("href")  
    url_list.append(ID_link)
    
k = 0        
    
for url in url_list:
    
    browser.get(url)
    time.sleep(3)
    
    k+=1
    
    print("k=",k)
    
    try:
        table=browser.find_element_by_xpath('//*[@id="biospecimen"]/div/div/div[3]/div/table')#定位网页表格位置
    except NoSuchElementException:
        print(url)
        
    else: 
        table_rows=table.find_elements_by_tag_name('tr')# table包含行数的集合，包含标题
        vrows=len(table_rows)#将总行数赋给变量
        
        m = 0
        
        for table_num in range(2, vrows):
            data_format = table_rows[table_num].find_elements_by_tag_name('td')[1]
            table_text=data_format.get_attribute('textContent')#遍历每行第2列获取单元格的值。
            if table_text == "BCR SSF XML":
                m+=1
                btn_download = table_rows[table_num].find_elements_by_tag_name('button')[1]
                time.sleep(2)
                btn_download.click()
                time.sleep(8)
                
        print("m=",m)       
