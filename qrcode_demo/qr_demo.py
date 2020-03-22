import qrcode

# # 二维码内容
# data = 'https://www.baidu.com/'
# # 生成二维码
# img = qrcode.make(data=data)
# # 显示二维码
# img.show()
# # 保存二维码
# # img.save('qr.jpg')

'''
version：二维码的格子矩阵大小，可以是 1 到 40，1 最小为 21*21，40 是 177*177
error_correction：二维码错误容许率，默认 ERROR_CORRECT_M，容许小于 15% 的错误率
box_size：二维码每个小格子包含的像素数量
border：二维码到图片边框的小格子数，默认值为 4
'''
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=3,
)
# 二维码内容
data = 'https://www.baidu.com/'
qr.add_data(data=data)
# 启用二维码颜色设置
qr.make(fit=True)
img = qr.make_image(fill_color='blue', back_color='white')
# 显示二维码
img.show()