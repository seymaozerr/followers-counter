import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

# Takipçi sayısını alma işlemini gerçekleştiren fonksiyon
def get_followers():
    kullaniciAdi = entry.get() # Kullanıcı adını al

    driver = webdriver.Chrome() # Selenium WebDriver'ı başlat
    driver.get("https://letterboxd.com/{}/".format(kullaniciAdi)) # Kullanıcının profil sayfasını aç

    time.sleep(2) # 2 saniye bekle

    # Takipçi sayısını bul ve etiket metnini güncelle
    followersLink = driver.find_element(By.XPATH, '//*[@id="profile-header"]/div/div[4]/div[1]/h4[4]/a/span[1]').text
    followersLabel.config(text="Takipçi Sayisi: " + followersLink)

    driver.close() # WebDriver'ı kapat

window = tk.Tk() # Tkinter penceresi oluştur
window.title("LETTERBOXD TAKİPÇİ SAYİSİ")
window.geometry("150x150")

label = tk.Label(window, text="Kullanici Adi:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Takipçi Sayisini Al", command=get_followers)
button.pack()

followersLabel = tk.Label(window, text="")
followersLabel.pack()

window.mainloop()  # Pencereyi aç ve döngüyü başlat