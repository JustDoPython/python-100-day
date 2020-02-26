# encoding:utf-8
import requests
import base64
import cv2

ak = 'ak'
sk = 'sk'

def getPhoto():
    '''
    调用摄像头拍摄照片
    :return: 照片路径
    '''
    print("准备拍摄照片，请保持颜值在线...")
    photoSrc = '自拍路径'
    cap = cv2.VideoCapture(0)
    while (1):
        ret, frame = cap.read()
        # 显示图像
        cv2.imshow("photo", frame)
        # 按 q 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite(photoSrc, frame)
            print("照片已经拍摄完成！")
            break
    cap.release()
    cv2.destroyAllWindows()
    return photoSrc

def getAccessToken():
    '''
    获取百度 AI 开放平台的 access_token
    :return: access_token
    '''
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + ak + '&client_secret=' + sk
    response = requests.get(host)
    if response:
        print(response.json())
        return response.json()['access_token']


def faceFusion(templateBase64, targetBase64, access_token):
    '''
    换脸术
    :param templateBase64: 模板图片
    :param targetBase64: 目标图片
    :param access_token: access_token
    :return: 换脸后的 base64
    '''
    request_url = "https://aip.baidubce.com/rest/2.0/face/v1/merge"

    params = "{\"image_template\":{\"image\":\"" + templateBase64 + "\",\"image_type\":\"BASE64\",\"quality_control\":\"NONE\"},\"image_target\":{\"image\":\"" + targetBase64 + "\",\"image_type\":\"BASE64\",\"quality_control\":\"NONE\"}}"

    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())
    return response.json()['result']['merge_image']


def image2base64(imagePath):
    '''
    图片转base64
    :param image_path: 图片地址
    :return: base64
    '''
    with open(imagePath, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
        return s

def base642image(base64str):
    '''
    base64转图片
    :param base64str: base64
    '''
    imgdata = base64.b64decode(base64str)
    with open('换脸后路径', 'wb') as f:
        f.write(imgdata)
    print('successful')

def main():
    photoSrc = getPhoto()
    target = image2base64(photoSrc)
    template = image2base64('模板图片路径')
    print(target)
    access_token = getAccessToken()
    image_base64 = faceFusion(template, target, access_token)
    base642image(image_base64)

if __name__ == '__main__':
    main()
