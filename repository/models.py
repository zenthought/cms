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
    avg_salary = models.IntegerField('学完平均薪资',  blank=True, null=True)
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
    teachers = models.ManyToManyField('Teacher', verbose_name="老师", blank=True, )
    class_type = models.CharField(choices=class_type_choices, max_length=64, verbose_name='班额及类型', blank=True,
                                  null=True)
    status = models.CharField(choices=(
        ('0', '报名中'),
        ('1', '已开班')
    ), max_length=32)


# 导师表
class Teacher(models.Model):
    name = models.CharField(max_length=32)

    position = models.CharField(max_length=32)  # 职位 choice
    photo = models.CharField(max_length=128)  # 头像img文件路径
    introduction = models.CharField(max_length=64)  # 简介


# 视频表
class Video(models.Model):
    av_type = models.CharField(choices=(
        ('0', '公开课'),
        ('1', '职场窍门'),
        ('2', 'IT百科')
    ),max_length=32)  # 公开课 职场窍门   IT百科     # 	av-type 视频分类 用于自学课程页面
    study_num = models.IntegerField()  # 学习人数
    upload_date = models.DateField(max_length=32)  # 上传日期   用于:最新上传排序
    title = models.CharField(max_length=32)  # 视频名字
    teacher = models.ForeignKey(Teacher)  # 关联导师表

    college = models.ForeignKey(College)  # 关联到学院表


class VideoInfo(models.Model):
    # 视频详情表
    title = models.CharField(max_length=32)  # 分支课程名
    src = models.CharField(max_length=128)  # 文件路径链接
    video = models.ForeignKey(Video)


# 书籍表
class Book(models.Model):
    book_name = models.CharField(max_length=32)
    book_type = models.CharField(choices=((0, '跟老男孩学linux'), (1, '跟老男孩学python')),max_length=32 )
    author = models.CharField(max_length=32)  # 作者
    publisher = models.CharField(max_length=32)
    pub_time = models.DateField()
    initial_price = models.IntegerField()  # 原价
    discount_price = models.IntegerField()  # 优惠价
    book_size = models.IntegerField()  # 16开
    book_package = models.CharField(max_length=32)  # 线装 胶装
    is_taozhuang = models.BooleanField()  # boolean  是否是套装
    book_ISBN = models.CharField(max_length=32)  # 书号
    book_page_num = models.IntegerField()  # 页数
    image = models.CharField(max_length=128)  # 图片文件路径链接


# 书籍详情表
class BookInfo(models.Model):
    content_info = models.TextField(max_length=64)  # 内容简介
    author_info = models.TextField(max_length=64)  # 作者简介
    category = models.TextField()  # 目录
    pre_introduction = models.CharField(max_length=32)  # 前言 longstring类型


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
    password = models.CharField('密码',  max_length=32 )
    is_admin = models.BooleanField('管理员', default=0)

    def __str__(self):
        return self.name


# 学生表
class Student(models.Model):
    name = models.CharField(max_length=32)
    position = models.CharField(max_length=32)  # 职位
    company = models.CharField(max_length=32)  # 就职公司
    sign_date = models.DateField()  # 报名日期
    reason = models.CharField(max_length=64)  # 报名原因
    why_us = models.CharField(max_length=64)  # 为什么选老男孩
    wishes = models.CharField(max_length=64)  # 学习后的期待


# 同学说的内容
class classmate_resource(models.Model):
    url = models.CharField(max_length=128)  # 图片路径  或 视频路径

    type = models.CharField(choices=(
        (0, '评价'),
        (1, 'offer'),
        (2, '笔记'),
        (3, '视频'),
    ),max_length=32)  # choices类型  commont评价  offer  note笔记  video


class Job(models.Model):
    # 招聘表   页面底部--加入我们
    name = models.CharField(max_length=32)  # 职位名称
    type = models.CharField(choices=((0, 'python讲师'), (1, 'linux讲师')),max_length=32)  # 职位分类
    city = models.ForeignKey(Campus)  # 外键到所在校区
    edu = models.CharField(max_length=32)  # 学历
    salary = models.IntegerField()  # 薪资


# 文章表  热点新闻 行业新闻等
class article(models.Model):
    title = models.CharField(max_length=32)  # 标题
    content = models.CharField(max_length=256)  # 内容
    date = models.DateField()  # 日期
    author = models.CharField(max_length=32)  # 作者
    read_num = models.IntegerField()  # 阅读数
    comment_num = models.IntegerField()  # 评论数
    choices = models.CharField(choices=(
        ('0', '行业新闻'),
        ('1', '最新技术'),
        ('2', ' 行业新闻'),
        ('3', '专题讲座'),
    ),max_length=32)
