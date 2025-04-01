import uuid
import os
from pathlib import Path

import pytest
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
        choices=((-2, '出现错误'),
                 (-1, '初始化'),
                 (0, '等待执行'),
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

    def save(self, *args, **kwargs):
        # model 保存时进行自动调用
        super().save(*args, **kwargs)
        # 用例执行逻辑
        # first 前置判断
        if self.status == 0 and self.is_processing is False:
            self.status = 1
            self.is_processing = True
            self.save()

        # second 用例目录
        test_dir = Path(str(self.case.path)).parent

        # third call pytest
        ret = pytest.main(test_dir)

        # fourth 更新状态
        if ret == pytest.ExitCode.OK:
            self.is_pass = True
        else:
            self.is_pass = False
        self.status = 2
        self.is_processing = True
        self.save()
        # fifth 生成报告
        ret = os.system(f"allure generate -c -o {test_dir / 'report'} {test_dir / '.allure_results'}")

        if ret == 0:
            self.has_report = True
        else:
            self.has_report = False

        self.status = 3
        self.is_processing = False
        self.save()