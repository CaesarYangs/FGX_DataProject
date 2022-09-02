# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SportsdataAnalysisEndurance(models.Model):
    student_id = models.IntegerField(primary_key=True)
    endurance_average = models.FloatField(blank=True, null=True)
    endurance_freshman = models.FloatField(blank=True, null=True)
    endurance_sophomore = models.FloatField(blank=True, null=True)
    endurance_junior = models.FloatField(blank=True, null=True)
    endurance_senior = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sportsdata_analysis_endurance'


class SportsdataAnalysisFlexible(models.Model):
    student_id = models.IntegerField(primary_key=True)
    flexible_average = models.FloatField(blank=True, null=True)
    flexible_freshman = models.FloatField(blank=True, null=True)
    flexible_sophomore = models.FloatField(blank=True, null=True)
    flexible_junior = models.FloatField(blank=True, null=True)
    flexible_senior = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sportsdata_analysis_flexible'


class SportsdataAnalysisJump(models.Model):
    student_id = models.IntegerField(primary_key=True)
    jump_average = models.FloatField(blank=True, null=True)
    jump_freshman = models.FloatField(blank=True, null=True)
    jump_sophomore = models.FloatField(blank=True, null=True)
    jump_junior = models.FloatField(blank=True, null=True)
    jump_senior = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sportsdata_analysis_jump'


class SportsdataAnalysisLung(models.Model):
    student_id = models.IntegerField(primary_key=True)
    lung_average = models.FloatField(blank=True, null=True)
    lung_freshman = models.FloatField(blank=True, null=True)
    lung_sophomore = models.FloatField(blank=True, null=True)
    lung_junior = models.FloatField(blank=True, null=True)
    lung_senior = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sportsdata_analysis_lung'


class SportsdataAnalysisMain(models.Model):
    student_id = models.IntegerField(primary_key=True)
    speed_main = models.FloatField(blank=True, null=True)
    lung_main = models.FloatField(blank=True, null=True)
    strength_main = models.FloatField(blank=True, null=True)
    endurance_main = models.FloatField(blank=True, null=True)
    jump_main = models.FloatField(blank=True, null=True)
    flexible_main = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sportsdata_analysis_main'


class SportsdataAnalysisSpeed(models.Model):
    student_id = models.IntegerField(primary_key=True)
    speed_average = models.FloatField(blank=True, null=True)
    speed_freshman = models.FloatField(blank=True, null=True)
    speed_junior = models.FloatField(blank=True, null=True)
    speed_senior = models.FloatField(blank=True, null=True)
    speed_sophomore = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sportsdata_analysis_speed'


class SportsdataAnalysisStrength(models.Model):
    student_id = models.IntegerField(primary_key=True)
    strength_average = models.FloatField(blank=True, null=True)
    strength_freshman = models.FloatField(blank=True, null=True)
    strength_sophomore = models.FloatField(blank=True, null=True)
    strength_junior = models.FloatField(blank=True, null=True)
    strength_senior = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sportsdata_analysis_strength'


class StudentAnalysisMain(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=100, blank=True, null=True)
    overall_score = models.FloatField(blank=True, null=True)
    ch_de_score = models.FloatField(blank=True, null=True)
    ch_zhi_score = models.FloatField(blank=True, null=True)
    ch_ti_score = models.FloatField(blank=True, null=True)
    ch_mei_score = models.FloatField(blank=True, null=True)
    ch_lao_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_analysis_main'


class StudentInfo(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_info'


class StudentgraphTest1(models.Model):
    c1 = models.IntegerField(db_column='C1', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(blank=True, null=True)
    course_name = models.TextField(blank=True, null=True)
    subject_score = models.FloatField(blank=True, null=True)
    student_score = models.IntegerField(blank=True, null=True)
    c6 = models.IntegerField(db_column='C6', blank=True, null=True)  # Field name made lowercase.
    c7 = models.IntegerField(db_column='C7', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'studentgraph_test1'
