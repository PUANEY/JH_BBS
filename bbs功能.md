# BBS
## 话题

### 话题表创建TopicModel (table_name = topic) 分页
#### 列表返回数据(1-6、8、10) 详情返回全部信息
-------------------------------------------
1. id:   primary=true, auto
2. category: foreign->category 一个话题多个类别
3. author: foreign->users 一个作者多个话题（avatar, username）点击头像跳转该用户信息
4. title:   varchar(100) 话题标题
5. visit:  int:default=0 点击量
6. pub_time: time(auto_now_add=True)
------------------------------------------
7. content: 富文本编辑器
8. require_password: default=false
9. password: default=null 如果require_password是false，则不展示密码输入框
10. require_jifen: default=false
11. jifen: int:default=0 如果require_jifen是false，则不展示积分输入框
12. hidden_content: 隐藏内容


### 话题功能api
1. 发布话题(post) (是否登录) （加经验） 
* 话题详情是否需要输入密码可见
* 话题详情是否需要支付积分可见
* 话题内的文件（百度网盘或其他）是否需要支付积分才可查看分享密码

2. 编辑话题(patch) （权限：是否是当前用户发布的话题）
3. 删除话题(delete)（权限：是不是当前用户发布的话题）
4. 审核话题(post) （后端调用api自动验证是否符合内容安全，审核完成后自动发布，且通知发布的用户已发布成功）
5. 搜索话题（post) (搜索框查询话题关键字)

## 评论

### 评论表 CommentModel (table_name=comment)
1. id:  primary=true auto
2. com_type:    
3. pub_time: time auto_now_add=True
4. pub_user: foreign->users
5. article: foreign->topic
6. content: 富文本内容

### 评论功能api
1. 发布评论(post) (是否登录) （加经验） 
2. 删除评论(delete)（权限：是不是当前用户发布的评论）
2. 审核评论(post) （后端调用api自动验证是否符合内容安全，审核完成后自动发布，且通知发布的用户已发布成功）


## 问答（Q&A）
### 问 (question)
1. 发布问题(post) (是否登录) （加经验） 
* 问题是否悬赏积分
* 问题是否有时间限制（超过截止时间如若没有最佳答案管理员可退还积分（截止时间后需管理员审核是否评论没有最佳答案，如果是用户为了不付积分而不设置最佳答案，一经查到，后果自负。））
* 是否着急（着急可追加积分置顶（根据追加积分置顶排序））

2. 删除问题(delete)（权限：是不是当前用户发布的问题）
3. 编辑问题(patch)（权限：是否是当前用户发布的问题）
4. 审核问题（后端调用api自动验证是否符合内容安全，审核完成后自动发布，且通知发布的用户已发布成功）
5. 搜索问题(post) (搜索框查询话题关键字)

### 答 (answer)
1. 发布答案(post) (是否登录) （加经验） 
* 如果被设置成最佳答案，2天后或者截止时间结束即可获取问题悬赏的全部积分，最多3个最佳答案，时间到了平分积分，由发布用户设置。
2. 删除答案(delete) （权限：是不是当前用户发布的答案）
3. 审核答案(post)（后端调用api自动验证是否符合内容安全，审核完成后自动发布，且通知发布的用户已发布成功）



## 用户设置 (目前面对江淮学院学生)
### 用户表设计Users(table_name = users)
1. id           primary     auto
2. stu_code（学号） unique varchar(20)
3. password    varchar(30)
4. avatar      varchar(100)
5. date_joined   user自带
6. last_login    user自带
7. is_superuser  user自带
8. is_staff      user自带
9. username    user自带
10. qq          varchar(10)
11. gitHub      varchar(20)
12. telephone   varchar(20)
13. vip         bool:default=false
14. svip        bool:defaylt=false
15. jiFen       int:default=0 连续签到送积分，等级提升送积分（等级越高积分越多）
16. level       int:default=1
17. signin(签到) int:default=0
18. email       user自带
19. is_active   user自带
20. signature(个性签名): varchar(255)
21. fans(粉丝)   foreign->self
22. cares(关注)  foreign->self

## 普通用户权限
1. 我的点赞
2. 收藏话题
3. 收藏问答
4. 我的话题
5. 我的问答
6. 回收站
7. 我的回复
8. 我的关注
9. 我的粉丝
10. 我的博客
11. 修改资料


## vip用户权限
1. 一月内可免费下载5个需要积分的文件
2. 购买即送100积分
3. 等级加速(每天获得积分更多)
4. 每个月可免费补卡3次

## svip用户权限（未定）

## 系统通知管理

## 全站设置

## 支付管理

## 短信管理
sentry监控