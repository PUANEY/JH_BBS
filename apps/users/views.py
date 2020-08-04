import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings
from .serializers import UsersSerializers
from lxml import html
Users = get_user_model()
etree = html.etree


class LoginView(APIView):
    """
    登陆逻辑
    """

    # formdata字典
    payload = {
        '__VIEWSTATE': '',
        'txtUserName': '',
        'Textbox1': '',
        'TextBox2': '',
        'txtSecretCode': '',
        'RadioButtonList1': '学生',
        'Button1': '',
        'lbLanguage': '',
        'hidPdrs': '',
        'hidsc': ''
    }

    # headers
    headers = {
        'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 '
                     'Safari/537.36 '
    }

    # 请求
    url = 'http://jwxt.ahujhc.cn/'
    s = requests.Session()

    def get(self, request):
        img = self.s.get(self.url + 'CheckCode.aspx', stream=True, headers=self.headers)
        # 保存验证码图片在当前文件夹下: checkcode.gif
        with open('media/checkcode.gif', 'wb') as f:
            f.write(img.content)
        # path = 'http://39.96.72.145/media/checkcode.gif'
        path = 'http://127.0.0.1:8000/media/checkcode.gif'
        return Response(path)

    def post(self, request):
        # 前端post学号密码到后端，后端到江淮学院教务系统认证
        stu_code = str(request.data['stu_code'])
        password = str(request.data['password'])
        check_code = str(request.data['check_code'])
        print(stu_code + "-" + password + "-" + check_code)
        # 保存用户信息，需要先判断数据库中有没有这个用户
        user = Users.objects.filter(stu_code=stu_code).first()

        if not user:
            self.payload['txtUserName'] = stu_code
            self.payload['TextBox2'] = password
            # 输入验证码
            self.payload['txtSecretCode'] = check_code
            # 返回html
            ht = self.s.get(self.url, headers=self.headers)

            # 解析
            # 获取VIEWSTATE
            index = etree.HTML(ht.text)
            table = index.xpath('//input[@name="__VIEWSTATE"]/@value')
            self.payload['__VIEWSTATE'] = table
            pst = self.s.post(self.url, data=self.payload, headers=self.headers)

            refer_url = 'http://jwxt.ahujhc.cn/xs_main.aspx?xh={}'.format(stu_code)
            name_page = self.s.get(url=refer_url, headers=self.headers)
            name_page = etree.HTML(name_page.text)
            try:
                name = name_page.xpath('//div[@class="info"]//em//text()')[1].replace('同学', '')
            except:
                return Response({"msg": "用户认证失败,请重新输入", "code": 400})
            user = Users.objects.create(stu_code=stu_code, password=password, username=name)
        else:
            if user.password != password:
                return Response({"msg": "密码错误", "code": 400})
        # 手动签发jwt
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token
        user.save()

        resp_data = {
            "token": token,
            "code": 200
        }
        return Response(resp_data)


class AuthView(APIView):
    def post(self, request):
        token = request.data['token']
        user = Users.objects.get(token=token)
        if not user:
            return Response({'msg': 'token不存在', "code": 400})

        return Response({'msg': '登陆成功', "user": UsersSerializers(user).data, "code": 200})





