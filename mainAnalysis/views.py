from django.shortcuts import render
import pymysql
pymysql.install_as_MySQLdb()
from django.utils.safestring import mark_safe
from mainAnalysis.models import StudentAnalysisMain
from mainAnalysis.models import StudentInfo
# Create your views here.

def index1(request):
    ans = {}  # 创建一个字典
    ans['head'] = 'hello world111'  # 赋值
    return render(request, 'mainAnalysis/firstpage.html', ans)  # 输出字典

#五育总分析图——柱状图
def mainStuGraph1(request):
    studentId = request.GET.get('id')
    temp = StudentAnalysisMain.objects.filter(student_id=studentId)
    studentName = list(StudentInfo.objects.filter(student_id=studentId))[0].student_name
    data = []

    student = list(temp)[0]
    data.append(student.ch_de_score)
    data.append(student.ch_zhi_score)
    data.append(student.ch_ti_score)
    data.append(student.ch_mei_score)
    data.append(student.ch_lao_score)

    return render(request, 'mainAnalysis/1_mainAnalysis.html', {'data':data,'studentId':studentId,'studentName':studentName})

#五育总分析图——极坐标图
def mainStuGraph1_1(request):
    studentId = request.GET.get('id')
    temp = StudentAnalysisMain.objects.filter(student_id=studentId)
    studentName = list(StudentInfo.objects.filter(student_id=studentId))[0].student_name
    data = []

    student = list(temp)[0]
    data.append(student.ch_de_score)
    data.append(student.ch_zhi_score)
    data.append(student.ch_ti_score)
    data.append(student.ch_mei_score)
    data.append(student.ch_lao_score)

    return render(request, 'mainAnalysis/1-1_mainAnalysis.html', {'data':data,'studentId':studentId,'studentName':studentName})

#五育总分析图——与班级/年级平均值直观对比图
def mainStuGraph1_2(request):
    studentId = request.GET.get('id')
    temp = StudentAnalysisMain.objects.filter(student_id=studentId)
    studentName = list(StudentInfo.objects.filter(student_id=studentId))[0].student_name
    data = []

    student = list(temp)[0]
    data.append(student.overall_score)
    data.append(student.ch_de_score)
    data.append(student.ch_zhi_score)
    data.append(student.ch_ti_score)
    data.append(student.ch_mei_score)
    data.append(student.ch_lao_score)

    objects = StudentAnalysisMain.objects.all()
    count = objects.count()
    #处理每项的班级/年级平均值
    average_list = [0.0,0.0,0.0,0.0,0.0,0.0]

    for i in range(count):
        average_list[0] += objects[i].overall_score
        average_list[1] += objects[i].ch_de_score
        average_list[2] += objects[i].ch_zhi_score
        average_list[3] += objects[i].ch_ti_score
        average_list[4] += objects[i].ch_mei_score
        average_list[5] += objects[i].ch_lao_score

    #将处理后的正负差直接写入list：data中
    data[0] -= average_list[0]/count
    data[1] -= average_list[1] / count
    data[2] -= average_list[2] / count
    data[3] -= average_list[3] / count
    data[4] -= average_list[4] / count
    data[5] -= average_list[5] / count

    theme = [1]
    return render(request, 'mainAnalysis/1-2_mainAnalysis.html', {'theme':theme,'data':data,'studentId':studentId,'studentName':studentName})
