# Generated by Django 2.2 on 2020-12-08 23:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GradeClassModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('mod_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False)),
                ('s_grade', models.SmallIntegerField(verbose_name='年级')),
                ('s_class', models.SmallIntegerField(verbose_name='班级')),
                ('cnt', models.SmallIntegerField(default=-1, verbose_name='班级人数')),
            ],
            options={
                'verbose_name': '班级信息表',
                'verbose_name_plural': '班级信息表',
                'ordering': ['s_grade', 's_class'],
            },
        ),
        migrations.CreateModel(
            name='SchoolModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('mod_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=256, verbose_name='学校名称')),
            ],
            options={
                'verbose_name': '学校信息表',
                'verbose_name_plural': '学校信息表',
            },
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('mod_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False)),
                ('uuid', models.CharField(help_text='系统级别的唯一身份', max_length=128, primary_key=True, serialize=False, verbose_name='系统级别的唯一身份')),
                ('name', models.CharField(max_length=64, verbose_name='学生姓名')),
                ('status', models.CharField(choices=[('0', '在班'), ('1', '已转班'), ('2', '已转学')], default='0', max_length=16)),
                ('in_class', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.GradeClassModel')),
            ],
            options={
                'verbose_name': '学生信息表',
                'verbose_name_plural': '学生信息表',
                'ordering': ['uuid'],
            },
        ),
        migrations.CreateModel(
            name='StudentDetailsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('mod_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False)),
                ('gender', models.CharField(choices=[('0', '女'), ('1', '男')], default=0, max_length=16, verbose_name='性别')),
                ('address', models.CharField(max_length=256, verbose_name='家庭地址')),
                ('card_num', models.CharField(max_length=24, verbose_name='身份证号码')),
                ('telephone', models.CharField(max_length=18, verbose_name='电话号码')),
                ('uuid', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='student.StudentModel')),
            ],
            options={
                'verbose_name': '学生详情表',
                'verbose_name_plural': '学生详情表',
                'ordering': ['uuid'],
            },
        ),
    ]
