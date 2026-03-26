import qrcode
x = qrcode.QRCode() 
msg = "hi im thiya"
x.add_data(msg)
x.make(fit=True)
res = x.make_image(fill_color="black", back_color="white")
res.save("myqr.png")
print("QR code created!!")