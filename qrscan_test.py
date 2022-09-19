import qrcode
import cv2 
from pyzbar.pyzbar import decode
import webbrowser

# for generating qr codes (text)
# img = qrcode.make('Hello this is Gaeeee')
# img.save ('qrcodenigae.png')



img = 'qr_samples/sample.png'

qrcode = cv2.imread(img)

for code in decode(qrcode):
    url = code.data.decode('utf-8')
    text = print(url)
    webbrowser.open(url)    #for auto opening of urls if text, it will auto search
    # with open("./outputs/"+img.lstrip('qr_samples').rstrip('.png' or '.jpg')+'.txt', 'w') as f:
    #     f.write(url)
    #     f.write('\n')




