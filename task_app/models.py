from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# 定义优先级选项
PRIORITY_CHOICES = (
    ('Low', '普通'),
    ('Medium', '紧急'),
    ('High', '非常紧急'),
)

# 定义预制分类
PREDEFINED_CATEGORIES = [
    ('工作', '工作'),
    ('学习', '学习'),
    ('生活', '生活'),
    ('娱乐', '娱乐'),
]

# 新增任务分类模型
'''
class TaskCategory(models.Model):
    name = models.CharField(max_length=50)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
'''
        
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=False)
    manager = models.ForeignKey(User,on_delete=models.CASCADE)
    #记录任务完成时间
    completed_at = models.DateTimeField(null=True, blank=True)

    #定义优先级选项
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Low',
    )
    # 定义任务分类
    category = models.CharField(
        max_length=50,
        choices=PREDEFINED_CATEGORIES,
        default='工作',
    )
    #category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f'{self.title}'
    
    #当任务状态变为完成时，记录完成时间
    def save(self, *args, **kwargs):
        if self.complete and not self.completed_at:
            self.completed_at = timezone.now()
        elif not self.complete:
            self.completed_at = None
        super(Task, self).save(*args, **kwargs)

# 定义预制任务分类函数
'''
def create_predefined_categories(user):
    predefined_categories = ['工作', '学习', '生活', '娱乐']
    for category_name in predefined_categories:
        TaskCategory.objects.get_or_create(name=category_name, manager=user)
'''