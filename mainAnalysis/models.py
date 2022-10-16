from django.db import models

# Create your models here.

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
    c1 = models.IntegerField(db_column='C1', primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(blank=True, null=True)
    course_name = models.TextField(blank=True, null=True)
    subject_score = models.FloatField(blank=True, null=True)
    student_score = models.IntegerField(blank=True, null=True)
    c6 = models.IntegerField(db_column='C6', blank=True, null=True)  # Field name made lowercase.
    c7 = models.IntegerField(db_column='C7', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'studentgraph_test1'
