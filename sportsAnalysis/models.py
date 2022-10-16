from django.db import models

# Create your models here.
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