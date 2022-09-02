from django.shortcuts import render
import pymysql
pymysql.install_as_MySQLdb()
from mainAnalysis.models import StudentAnalysisMain
# Create your views here.

def index1(request):
    ans = {}  # 创建一个字典
    ans['head'] = 'hello world111'  # 赋值
    return render(request, 'mainAnalysis/firstpage.html', ans)  # 输出字典

#五育总分析图——柱状图
def mainStuGraph1(request):
    studentId = request.GET.get('id')
    temp = StudentAnalysisMain.objects.filter(student_id=studentId)
    data = []

    student = list(temp)[0]
    data.append(student.ch_de_score)
    data.append(student.ch_zhi_score)
    data.append(student.ch_mei_score)
    data.append(student.ch_lao_score)

    return render(request, 'mainAnalysis/Graph11.html',{'data':data})