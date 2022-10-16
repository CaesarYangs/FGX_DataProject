from django.shortcuts import render
import pymysql
pymysql.install_as_MySQLdb()
import json
from mainAnalysis.models import StudentInfo
from sportsAnalysis.models import SportsdataAnalysisMain
from sportsAnalysis.models import SportsdataAnalysisSpeed
from sportsAnalysis.models import SportsdataAnalysisLung
from sportsAnalysis.models import SportsdataAnalysisStrength
from sportsAnalysis.models import SportsdataAnalysisEndurance
from sportsAnalysis.models import SportsdataAnalysisJump
from sportsAnalysis.models import SportsdataAnalysisFlexible


# Create your views here.

#体育教育总分析图——柱状图
def sportsAnalysisGraph1(request):
    studentId = request.GET.get('id')
    temp = SportsdataAnalysisMain.objects.filter(student_id=studentId)
    studentName = list(StudentInfo.objects.filter(student_id=studentId))[0].student_name
    data = []

    student = list(temp)[0]
    data.append(student.speed_main)
    data.append(student.lung_main)
    data.append(student.strength_main)
    data.append(student.endurance_main)
    data.append(student.jump_main)
    data.append(student.flexible_main)

    return render(request, 'sportsAnalysis/1_sportsMainAnalysis.html', {'data':data,'studentId':studentId,'studentName':studentName})

#体育教育大学期间时间分析图——折线图
def sportsAnalysisGraphChronological(request):
    studentId = request.GET.get('id')
    studentName = list(StudentInfo.objects.filter(student_id=studentId))[0].student_name
    data = []

    speedChron = list(SportsdataAnalysisSpeed.objects.filter(student_id=studentId))[0]
    lungChron = list(SportsdataAnalysisLung.objects.filter(student_id=studentId))[0]
    strengthChron = list(SportsdataAnalysisStrength.objects.filter(student_id=studentId))[0]
    enduranceChron = list(SportsdataAnalysisEndurance.objects.filter(student_id=studentId))[0]
    jumpChron = list(SportsdataAnalysisJump.objects.filter(student_id=studentId))[0]
    flexChron = list(SportsdataAnalysisFlexible.objects.filter(student_id=studentId))[0]

    data.append(["Score","Item","Year"])
    data.append([speedChron.speed_freshman,"速度",2018])
    data.append([lungChron.lung_freshman,"肺活量",2018])
    data.append([strengthChron.strength_freshman,"力量",2018])
    data.append([enduranceChron.endurance_freshman,"耐力",2018])
    data.append([jumpChron.jump_freshman,"跳跃",2018])
    data.append([flexChron.flexible_freshman,"柔韧",2018])

    data.append([speedChron.speed_sophomore,"速度",2019])
    data.append([lungChron.lung_sophomore,"肺活量",2019])
    data.append([strengthChron.strength_sophomore,"力量",2019])
    data.append([enduranceChron.endurance_sophomore,"耐力",2019])
    data.append([jumpChron.jump_sophomore,"跳跃",2019])
    data.append([flexChron.flexible_sophomore,"柔韧",2019])

    data.append([speedChron.speed_junior,"速度",2020])
    data.append([lungChron.lung_junior,"肺活量",2020])
    data.append([strengthChron.strength_junior,"力量",2020])
    data.append([enduranceChron.endurance_junior,"耐力",2020])
    data.append([jumpChron.jump_junior,"跳跃",2020])
    data.append([flexChron.flexible_junior,"柔韧",2020])

    data.append([speedChron.speed_senior,"速度",2021])
    data.append([lungChron.lung_senior,"肺活量",2021])
    data.append([strengthChron.strength_senior,"力量",2021])
    data.append([enduranceChron.endurance_senior,"耐力",2021])
    data.append([jumpChron.jump_senior,"跳跃",2021])
    data.append([flexChron.flexible_senior,"柔韧",2021])

    # print(json.dumps(data))

    return render(request, 'sportsAnalysis/2_sportsChronAnalysis.html', {'data':json.dumps(data),'studentId':studentId,'studentName':studentName})
