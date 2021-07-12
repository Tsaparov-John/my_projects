from openpyxl.reader.excel import load_workbook
from openpyxl.utils import cell
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import xlsxwriter


#C:\Program Files (x86)\Google\Chrome\Application
#command:  chrome.exe --remote-debugging-port=8989 --user-data-dir=C:\Program Files\selenium\botuser
opt=Options()
opt.add_experimental_option("debuggerAddress","localhost:8989")
driver=webdriver.Chrome(executable_path="C:\Program Files\selenium\chromedriver.exe",options=opt)


path="playlist.xlsx"
file=load_workbook(path)
sheet=file.active
counter=1


save=[]

for i in range(2,5000):
    #youtube playlits unto 5k songs
    cellsheet="A"+str(i)
    url=sheet[cellsheet].value

    

    driver.get(url)
    sleep(3)
    save.clear()
    save=driver.find_elements_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-button-renderer[2]/a/yt-formatted-string')
    print(i)
    if not save:
        print("broken link: ",url )

    else:
        save[0].click()

        sleep(1)
        add=driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-add-to-playlist-renderer/div[2]/ytd-playlist-add-to-option-renderer[2]/tp-yt-paper-checkbox/div[2]/div/div/yt-formatted-string[1]')
        add.click()
        counter+=1
        #  if (counter==5000):
        #      break
    
     
