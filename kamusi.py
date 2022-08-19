import qrcode

# qr = qrcode.make('Hi Edwin')
# qr.save('myQR.png')

qr = qrcode.QRCode(
    version=1,
    # error_correction=qrcode.constants.ERROR_CORRECT_M
    box_size=15,
    border=5
 )   

#data = ('harooo')
data = "https://www.google.com/search?q=qr+code&client=ubuntu&hs=gzI&channel=fs&ei=ueX9YtHyG46-adrBqbAK&ved=0ahUKEwiRs8TU6s_5AhUOXxoKHdpgCqYQ4dUDCA0&uact=5&oq=qr+code&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAELEDEEMyCggAELEDEIMBEEMyBQgAEJECMgcIABCxAxBDMgoIABCxAxCDARBDMgQIABBDMgQIABBDMgQIABBDMgUIABCABDIFCAAQgAQ6CAgAEI8BEOoCOggILhCPARDqAjoRCC4QgAQQsQMQgwEQxwEQ0QM6BAgAEAM6CwguEIAEELEDEIMBOggIABCxAxCDAToOCC4QgAQQsQMQgwEQ1AI6CAgAEIAEELEDSgQIQRgBSgQIRhgAUIK8lQFY0siVAWDzy5UBaANwAHgAgAG5AogB3Q6SAQUyLTYuMZgBAKABAbABCsABAQ&sclient=gws-wiz"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('My_QR_code.png')