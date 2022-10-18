import json

from django.shortcuts import render
import pymysql

pymysql.install_as_MySQLdb()
from django.utils.safestring import mark_safe
from mainAnalysis.models import StudentAnalysisMain
from mainAnalysis.models import StudentInfo
from mainAnalysis.models import StudentgraphTest1


# Create your views here.

def index1(request):
    ans = {}  # 创建一个字典
    ans['head'] = 'hello world111'  # 赋值
    return render(request, 'mainAnalysis/firstpage.html', ans)  # 输出字典


# 五育总分析图——柱状图
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

    return render(request, 'mainAnalysis/1_mainAnalysis.html',
                  {'data': data, 'studentId': studentId, 'studentName': studentName})


# 五育总分析图——极坐标图
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

    return render(request, 'mainAnalysis/1-1_mainAnalysis.html',
                  {'data': data, 'studentId': studentId, 'studentName': studentName})


# 五育总分析图——与班级/年级平均值直观对比图
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
    # 处理每项的班级/年级平均值
    average_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    for i in range(count):
        average_list[0] += objects[i].overall_score
        average_list[1] += objects[i].ch_de_score
        average_list[2] += objects[i].ch_zhi_score
        average_list[3] += objects[i].ch_ti_score
        average_list[4] += objects[i].ch_mei_score
        average_list[5] += objects[i].ch_lao_score

    # 将处理后的正负差直接写入list：data中
    data[0] -= average_list[0] / count
    data[1] -= average_list[1] / count
    data[2] -= average_list[2] / count
    data[3] -= average_list[3] / count
    data[4] -= average_list[4] / count
    data[5] -= average_list[5] / count

    return render(request, 'mainAnalysis/1-2_mainAnalysis.html',
                  {'data': data, 'studentId': studentId, 'studentName': studentName})


# 五育总分析图——与班级/年级平均值直观对比图
def mainStuGraph1_3(request):
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
    # 处理每项的班级/年级平均值
    average_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    for i in range(count):
        average_list[0] += objects[i].overall_score
        average_list[1] += objects[i].ch_de_score
        average_list[2] += objects[i].ch_zhi_score
        average_list[3] += objects[i].ch_ti_score
        average_list[4] += objects[i].ch_mei_score
        average_list[5] += objects[i].ch_lao_score

    # 将处理后的正负差直接写入list：data中
    data[0] -= average_list[0] / count
    data[1] -= average_list[1] / count
    data[2] -= average_list[2] / count
    data[3] -= average_list[3] / count
    data[4] -= average_list[4] / count
    data[5] -= average_list[5] / count

    return render(request, 'mainAnalysis/1-2_mainAnalysis.html',
                  {'data': data, 'studentId': studentId, 'studentName': studentName})


def mainStuGraph2(request):
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

    return render(request, 'mainAnalysis/4_1specialAnalysis.html',
                  {'data': data, 'studentId': studentId, 'studentName': studentName})


# 打卡气泡图——按教学周
def mainStuGraph3(request):
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

    return render(request, 'mainAnalysis/3_mainAnalysis.html',
                  {'data': data, 'studentId': studentId, 'studentName': studentName})


# 打卡气泡图——每周更精确
def mainStuGraph3_1(request):
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

    return render(request, 'mainAnalysis/3_1Analysis.html',
                  {'data': data, 'studentId': studentId, 'studentName': studentName})


# 打卡气泡图——按年为单位
def mainStuGraph3_2(request):
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

    return render(request, 'mainAnalysis/3_2Analysis.html',
                  {'data': data, 'studentId': studentId, 'studentName': studentName})


def mainGradeAnalysis1(request):
    studentId = request.GET.get('id')
    studentName = list(StudentInfo.objects.filter(student_id=studentId))[0].student_name
    year = request.GET.get('year')

    if (year == '1'):
        temp = StudentgraphTest1.objects.all()
    else:
        temp = StudentgraphTest1.objects.filter(year=year)

    data = []
    count = temp.count()
    temp = list(temp)
    for i in range(count):
        data.append({'value': temp[i].subject_score, 'name': temp[i].course_name})

    return render(request, 'mainAnalysis/1_gradeAnalysis.html',
                  {'data': data, 'studentId': studentId, 'studentName': studentName, 'year': year})


# 链接关系图
def linkAnalysis_1(request):
    studentId = request.GET.get('id')
    temp = StudentAnalysisMain.objects.filter(student_id=studentId)
    studentName = list(StudentInfo.objects.filter(student_id=studentId))[0].student_name
    data = []
    link = []
    categories = []

    data = [{
        "id": "0",
        "name": "大学物理",
        "symbolSize": 19.12381,
        "x": -266.82776,
        "y": 299.6904,
        "value": 28.685715,
        "category": 0
    },
        {
            "id": "1",
            "name": "高等工程数学",
            "symbolSize": 2.6666666666666665,
            "x": -418.08344,
            "y": 446.8853,
            "value": 4,
            "category": 0
        },
        {
            "id": "2",
            "name": "Capstone设计-1",
            "symbolSize": 6.323809333333333,
            "x": -212.76357,
            "y": 245.29176,
            "value": 9.485714,
            "category": 1
        },
        {
            "id": "3",
            "name": "交通规划",
            "symbolSize": 6.323809333333333,
            "x": -242.82404,
            "y": 235.26283,
            "value": 9.485714,
            "category": 1
        },
        {
            "id": "4",
            "name": "城市规划原理",
            "symbolSize": 2.6666666666666665,
            "x": -379.30386,
            "y": 429.06424,
            "value": 4,
            "category": 0
        },
        {
            "id": "5",
            "name": "暑期学校课程",
            "symbolSize": 4.6666666666666665,
            "x": -417.26337,
            "y": 406.03506,
            "value": 4,
            "category": 0
        },
        {
            "id": "6",
            "name": "运筹学",
            "symbolSize": 2.6666666666666665,
            "x": -332.6012,
            "y": 485.16974,
            "value": 4,
            "category": 0
        },
        {
            "id": "7",
            "name": "Keystone设计-1",
            "symbolSize": 2.6666666666666665,
            "x": -382.69568,
            "y": 475.09113,
            "value": 4,
            "category": 0
        },
        {
            "id": "8",
            "name": "动力学与流体力学",
            "symbolSize": 5.6666666666666665,
            "x": -320.384,
            "y": 387.17325,
            "value": 4,
            "category": 0
        },
        {
            "id": "9",
            "name": "道路勘测设计",
            "symbolSize": 2.6666666666666665,
            "x": -344.39832,
            "y": 451.16772,
            "value": 4,
            "category": 0
        },
        {
            "id": "10",
            "name": "静力学和材料力学",
            "symbolSize": 3.6666666666666665,
            "x": -89.34107,
            "y": 234.56128,
            "value": 4,
            "category": 1
        },
        {
            "id": "11",
            "name": "高等数学",
            "symbolSize": 66.66666666666667,
            "x": -87.93029,
            "y": -6.8120565,
            "value": 100,
            "category": 1
        },
        {
            "id": "12",
            "name": "交通工程导论",
            "symbolSize": 4.495239333333333,
            "x": -339.77908,
            "y": -184.69139,
            "value": 6.742859,
            "category": 1
        }]

    link = [{
        "source": "1",
        "target": "0"
    },
        {
            "source": "2",
            "target": "0"
        },
        {
            "source": "3",
            "target": "0"
        },
        {
            "source": "3",
            "target": "2"
        },
        {
            "source": "4",
            "target": "0"
        },
        {
            "source": "5",
            "target": "0"
        },
        {
            "source": "6",
            "target": "0"
        },
        {
            "source": "7",
            "target": "0"
        },
        {
            "source": "8",
            "target": "0"
        },
        {
            "source": "9",
            "target": "0"
        },
        {
            "source": "11",
            "target": "0"
        },
        {
            "source": "11",
            "target": "2"
        },
        {
            "source": "11",
            "target": "3"
        },
        {
            "source": "11",
            "target": "10"
        },
        {
            "source": "12",
            "target": "11"
        }]

    categories = [{
        "name": "A"
    },
        {
            "name": "B"
        }]

    return render(request, 'mainAnalysis/4_specialAnalysis.html',
                  {'data': data, 'link': link, 'categories': categories, 'studentId': studentId,
                   'studentName': studentName})


# 德育 劳育动效展示图
def otherAnalysis_1(request):
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

    return render(request, 'mainAnalysis/5_specialAnalysis.html',
                  {'data': data, 'studentId': studentId, 'studentName': studentName})


# 课程归属直观树状图
def mainGradeAnalysis2(request):
    studentId = request.GET.get('id')
    studentName = list(StudentInfo.objects.filter(student_id=studentId))[0].student_name
    data = {}
    gradeData = []

    for i in range(1, 6):
        temp = StudentgraphTest1.objects.filter(c6=i)
        count = temp.count()
        temp = list(temp)
        tempData = []
        for j in range(count):
            tempData.append({"name": temp[j].course_name, "value": temp[j].student_score})
        gradeData.append(tempData)
        # gradeData.append(json.dumps(tempData, ensure_ascii=False))

    print(gradeData[3])
    data = {
        "name": "汇总",
        "children": [
            {
                "name": "德",
                "children": gradeData[0]
            },
            {
                "name": "智",
                "children": gradeData[1]
            },
            {
                "name": "体",
                "children": gradeData[2]
            },
            {
                "name": "美",
                "children": gradeData[3]
            },
            {
                "name": "劳",
                "children": gradeData[4]
            }
        ]
    }


    return render(request, 'mainAnalysis/6_specialAnalysis.html',
                  {'data': data, 'studentId': studentId, 'studentName': studentName})
