from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import WebDriverException
url:str = 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb?ptopid=sC02BA3DA781B42B48996C4B63E4E3186&amp;sid=221118125401162747&amp;fun2='
url:str = 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first6?ptopid=s554AE54B6FB74A959900B649458E3DF2&sid=221118095111746531&fun2=&id8='
button_1_xpath = "//*[@id='bak_0']/div[11]/div[3]/div[4]" #本人填报 //*[@id="bak_0"]/div[11]/div[3]/div[4]
button_2_id = 'btn416a'#提交表格
final_text_xpath = "//*[@id='bak_0']/div[2]/div[2]/div[2]/div[2]"

user_name = '202207070604'
password = 'Dwb.20040216'

def log_in(url) -> str :
    edge_options = Options()
    edge_options.add_argument('--headless')
    driver = webdriver.Edge(options=edge_options)
    try:
        driver.get(url)
    except WebDriverException as value:
        print(value)
    except:
        print('unexcepted erro')
    else:
        driver.implicitly_wait(20)
        driver.execute_script('window.location=\'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0\'')
        driver.implicitly_wait(5)
        driver.find_element(By.NAME,'uid').send_keys(user_name)
        driver.find_element(By.NAME,'upw').send_keys(password)
        driver.find_element(By.NAME,'smbtn').click()
        driver.implicitly_wait(5)
        #iframe
        iframe = driver.find_element(By.ID,'zzj_top_6s')
        driver.switch_to.frame(iframe)
        driver.find_element(By.XPATH,button_1_xpath).click()
        #等待定位
        sleep(15)
        driver.find_element(By.ID,button_2_id).click()
        text=  driver.find_element(By.XPATH,final_text_xpath).text
        driver.close()
        return text
# selenium.common.exceptions.WebDriverException
if __name__ == '__main__':
    print(log_in(url))