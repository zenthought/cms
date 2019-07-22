from django.db import models
class_type_choices = (('fulltime', '脱产班',),
                      ('online', '网络班'),
                      ('weekend', '周末班',),)
course_choices = (('Linux', 'Linux中高级'),
                  ('PythonFullStack', 'Python高级全栈开发'),)


class Campus(models.Model):
    """
    校区表
    """
    name = models.CharField(verbose_name='校区', max_length=64)
    address = models.CharField(verbose_name='详细地址', max_length=512, blank=True, null=True)

    def __str__(self):
        return self.name


# 学院表
class College(models.Model):
    """
    学院表
    """
    title = models.CharField(verbose_name='学院', max_length=64)

    def __str__(self):
        return self.title


# 课程表
class Course(models.Model):
    """课程表"""

    title = models.CharField('标题', max_length=64, blank=True, )

    image = models.CharField('缩略图', max_length=64, blank=True, null=True)
    avg_salary = models.IntegerField('学完平均薪资', max_length=500, blank=True, null=True)
    period = models.CharField('周期', max_length=300, blank=True, null=True)


    def __str__(self):
        return self.title



# 班级表
class ClassList(models.Model):
    """
    班级表
    """
    name = models.CharField("班级名称", max_length=64, choices=course_choices)
    semester = models.IntegerField("学期")
    campuses = models.ForeignKey('Campus', verbose_name="校区")
    price = models.IntegerField("学费", default=10000)
    memo = models.CharField('开班详情', blank=True, null=True, max_length=100)
    start_date = models.DateField("开班日期")
    graduate_date = models.DateField("结业日期", blank=True, null=True)
    teachers = models.ManyToManyField('Teacher', verbose_name="老师",blank=True,)
    class_type = models.CharField(choices=class_type_choices, max_length=64, verbose_name='班额及类型', blank=True,
                                  null=True)
    status=models.CharField(choices=(
        ('0','报名中'),
        ('1','已开班')
    ))


# 导师表
class Teacher(models.Model):
    name=models.CharField()


  	position #职位 choice
  	photo  #头像img文件路径
  	introduction# 简介


# 视频表
class  Video(models.Model):
    av-type=   #公开课 职场窍门   IT百科     # 	av-type 视频分类 用于自学课程页面
    # 	study_num 学习人数
    # 	upload_date 上传日期   用于:最新上传排序
    # 	title  视频名字
    # 	teacher 关联导师表
    # college  关联到学院表



class VideoInfo(models.Model):
    # 视频详情表
    # 	title 分支课程名
    # 	src 链接
     video=models.ForeignKey(Video)




# 书籍表
class Book(models.Model):
# 	book_name
# 	book_type
# 	author
# 	publisher
# 	pub_time
# 	initial_price  原价
# 	discount_price 优惠价
# 	book_size 16开
# 	book_package  #线装 胶装
# 	is_taozhuang  boolean  是否是套装
# 	book_ISBN 书号
# 	book_page_num 页数
# 	image 图片



# 书籍详情表
class BookInfo(models.Model):
# 	content_info 内容简介
# 	author_info 作者简介
# 	category 目录  存成列表
# 	pre_introduction 前言 longstring类型


# 客户表 Customer
class Customer(models.Model):
    """
    客户表
    """

    name = models.CharField('姓名', max_length=32, blank=True, null=True, help_text='学员报名后，请改为真实姓名')
    sex_type = (('male', '男'), ('female', '女'))
    sex = models.CharField("性别", choices=sex_type, max_length=16, default='male', blank=True, null=True)
    birthday = models.DateField('出生日期', default=None, help_text="格式yyyy-mm-dd", blank=True, null=True)
    phone = models.BigIntegerField('手机号', blank=True, null=True)
    password = models.CharField('密码', )
    is_admin = models.BooleanField('管理员', default=0)

    def __str__(self):
        return  self.name



# 学生表
class Student(models.Model):


# name
# position #职位
# company  #就职公司
# sign_date 报名日期
# reason 报名原因
# why_us  为什么选老男孩
# wishes  学习后的期待


# 同学说的内容
class classmate_resource(models.Model):
    # url  图片路径  或 视频路径
    # type  choices类型  commont评价  offer  note比较  video



class Job(models.Model):
    # 招聘表   页面底部--加入我们
    name
    职位名称
    type
    职位分类
    city
    外键到所在城市
    edu
    学历
    salary
    薪资


# 文章表  热点新闻 行业新闻等
class article(models.Model):
    title  # 标题
    content  # 内容
    date  # 日期
    author  # 作者
    read_num  # 阅读数
    comment_num  # 评论数
    choices
            行业新闻
            最新技术
            问答专区
            专题讲座
