from pytube import YouTube
# by Bekir Bostancı
print("*****************************************")
print('Youtube Video Bilgi Alma Uygulamasına Hoşgeldiniz')
print('*****************************************')

def video_bilgi_göster():
    link_al = YouTube(input('Lütfen YouTube Linkini Giriniz: '))
    print("*"*20)
    print('Video İsmi:', link_al.title)
    print('Video Sahibi:', link_al.author)
    print('Video İzlenme Sayısı:', link_al.views)
    print('Video Açıklama:', link_al.description)      
    print('Video Uzunluğu:', link_al.length, 'Saniye')
    print("*"*20)

def video_indir():
    link_al = YouTube(input('Lütfen YouTube Linkini Giriniz: '))
    url_bağlantısı = link_al.streams.filter(progressive=True).first()
    url_bağlantısı.download()
    print("Video İndirildi..")

def video_ses_indir():
    link_al = YouTube(input('Lütfen YouTube Linkini Giriniz: '))
    url_bağlantısı = link_al.streams.filter(only_audio=True).first()
    print("video inddirildi..")
    url_bağlantısı.download()
    print("Ses İndirildi..")

while True:
    print("Lütfen Seçim Yapınız:")
    print("1- Video Bilgilerini Göster")
    print("2- Videoyu İndir")
    print("3- Video Sesini İndir")
    print("4- Çıkış")
    
    seçim_yap = input("Ne yapmak istersiniz? (1/2/3/4): ")

    if seçim_yap == "1":
        video_bilgi_göster()
    elif seçim_yap == "2":
        video_indir()
    elif seçim_yap == "3":
        video_ses_indir()
    elif seçim_yap == "4":
        break
    else:
        print("Geçersiz seçenek! Lütfen geçerli bir seçenek giriniz.")
