import uuid
import os
from django.db import models

# Create your models here.

def get_case_path(instance, filename):
    # 上传的文件保存在tests/<uuid>/<filename>
    return os.path.join('tests', str(instance.id), filename)

class TestTask(models.Model):
    """
    测试任务
    将用例文件上传至指定目录，并在该目录执行用例
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=255, verbose_name='任务名称')
    case = models.FileField(upload_to=get_case_path, verbose_name='用例文件')
    status = models.IntegerField(
        choices=((0, '未开始'),
                 (-1, '初始化'),
                 (-2, '出现错误'),
                 (1, '进行中'),
                 (2, '生成报告'),
                 (3, '执行结束')
                 ),
        default=-1, verbose_name='任务状态')

    is_processing = models.BooleanField(default=False, verbose_name='是否正在执行',editable=False)
    is_pass = models.BooleanField(default=False, verbose_name='是否通过',editable=False)
    has_report = models.BooleanField(default=False, verbose_name='是否生成报告',editable=False)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name_plural = verbose_name ='测试任务'

    def __str__(self):
        return self.name