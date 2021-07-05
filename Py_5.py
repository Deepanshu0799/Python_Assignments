#PRIME OR NOT#

n = int(input("Enter a number: "))
if (n<=1):
    print("Not a prime number.")
else:
    for i in range(2,n):
        if(n%i==0):
            print("Not a prime number.")
            break
    else:
        print("Yes, it is a prime number.")


#OUTPUT
#Enter a number: 7
#Yes, it is a prime number.
#Enter a number: 8
#Not a prime number.



####################################################################################################################################################################################



#Download from youtbe through python
#pip install pytube

from pytube import YouTube

vid = YouTube(input("Enter the link of the video that you want to download : "))

print(vid.title)

print(vid.thumbnail_url)

print(vid.length)

print(vid.views)  

print(vid.rating)

streams = vid.streams

for i in streams:
    print(i)

i = vid.streams.get_by_itag(input("Enter the itag number of the quality that you want to download : "))


file_size = i.filesize

print(round(file_size/(1024*1024)), " MB")

print("Download Started,wait till it gets downloaded...")

i.download('C:/Users/Asus/Desktop/') 

print("Download Completed ")


