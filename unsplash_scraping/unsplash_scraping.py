import requests
import os
from tkinter import *
from requests.models import encode_multipart_formdata


root = Tk()
root.geometry('405x300')
root.configure(background='#171717')
root.iconbitmap('fav.ico')



root.title("Unsplash Scraper by Tsaparov John")


myLabel0=Label(root,text='Welcome to "Unsplash Scraper"',bg="#171717",fg="#ededed",font=('Cambria', 20,'bold'),pady=5)
myLabel1=Label(root,text='a python script made by Tsaparov John',bg="#171717",fg="#ededed",font=('Cambria', 14,'italic'), pady=5)
myLabel0.grid(row=0,column=0,columnspan=3)
myLabel1.grid(row=1,column=0,columnspan=3)

myLabel2=Label(root,text="Search term:",bg="#171717",fg="#ededed")
myLabel2.grid(row=2,column=0,pady=7)
search_term=Entry(root,width=30,bg="#444444",fg="#ededed")
search_term.grid(row=2,column=1,columnspan=2)
search_term.insert(0, " ")

myLabel3=Label(root,text="Quality of images",bg="#171717",fg="#ededed")
myLabel3.grid(row=3,column=0,pady=7)
quality=StringVar()
quality.set("small")
qualityOption=OptionMenu(root, quality,"thumb","small","regular","full","raw")
qualityOption.config(bg="#171717",fg="#ededed")
qualityOption.grid(row=3,column=1,columnspan=2)



myLabel4=Label(root,text="Num_per_pages",bg="#171717",fg="#ededed")
myLabel4.grid(row=4,column=0,pady=7)
perpages=IntVar()
perpages.set(20)
rb1=Radiobutton(root, text="20", variable=perpages, value=20,bg="#171717",fg="#ededed",selectcolor="black",activebackground="#171717",activeforeground="#ededed").grid(row=4,column=1)
rb2=Radiobutton(root, text="30", variable=perpages, value=30,bg="#171717",fg="#ededed",selectcolor="black",activebackground="#171717",activeforeground="#ededed").grid(row=4,column=2)

myLabel5=Label(root,text="Num_of_pages",bg="#171717",fg="#ededed",)
myLabel5.grid(row=5,column=0,pady=7)
pages=Entry(root,width=30,bg="#444444",fg="#ededed")
pages.grid(row=5,column=1,columnspan=2)

search_input=" "

pages_input=1
per_page_input=20

def myClick():
   
  
    search_input=search_term.get()
    quality_input=quality.get()
    per_page_input=int(perpages.get())
    pages_input= int(pages.get())
   
    scraper=Unsplash(search_input)
    scraper.Scrapper(pages_input)


myButton = Button(root,text="Start script!",padx=10,pady=5,command=myClick,fg="#ededed",bg="#444444")
myButton.grid(row=6,column=1,columnspan=2,pady=7)

myExit =Button(root,text="Quit Script",padx=10,pady=5,command=root.quit,fg="#ededed", bg="#DA0037")
myExit.grid(row=6,column=0)

class Unsplash:
    def __init__(self,search_term=search_input,per_page=per_page_input,quality=quality.get()):
        self.search_term = search_term
        self.per_page = per_page
        self.page = 0
        self.quality =quality
        
        
    def set_url(self):
        return f"https://unsplash.com/napi/search/photos?query={self.search_term}&per_page={self.per_page}&page={self.page}&xp="

    def make_request(self):
        url= self.set_url()
        return requests.request("GET",url) 

    def get_data(self):
        self.data = self.make_request().json()

    def save_path(self,name):
        unsplash_dir = "unsplash"
        if not os.path.exists(unsplash_dir):        
            os.mkdir(unsplash_dir)
        if not os.path.exists(os.path.join(os.getcwd(),unsplash_dir,self.search_term)):
            os.mkdir(os.path.join(os.getcwd(),unsplash_dir,self.search_term))
        return f"{os.path.join(os.getcwd(),unsplash_dir,self.search_term,name)}.jpg"

    def download(self,url,name):
        filepath = self.save_path(name)
        with open(filepath,"wb") as f:
            f.write(requests.request("GET",url).content) 

    def Scrapper(self,pages_input):
        for page in range(0,pages_input+1): 
            self.make_request()
            self.get_data()
            for item in self.data['results']:
                name = item['id']
                url = item['urls'][self.quality]
                self.download(url,name)
                
            self.page +=1


root.mainloop()


