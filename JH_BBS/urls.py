"""JH_BBS URL Configuration"""
import xadmin
from django.conf.urls import url
from django.urls import path, include, re_path
from .settings import STATIC_ROOT, MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


from users.views import LoginView, AuthView
router = DefaultRouter()


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', include(router.urls)),
    # 登录 get  post
    path('login/', LoginView.as_view()),
    # 验证
    path('auth/', AuthView.as_view()),


    # 图片文件存储地址
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # 文档接口
    re_path(r'docs/', include_docs_urls(title='校园生活')),
    re_path(r'^', include(router.urls)),
    # 富文本
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
