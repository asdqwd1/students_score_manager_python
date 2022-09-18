
import re
import os
filename='students.txt'
def menu():
    print('==============================================学生管理系统======================================================')
    print('===============================================功能菜单=======================================================')
    print('\t\t\t\t\t 1.录入学生信息')
    print('\t\t\t\t\t 2.查找学生信息')
    print('\t\t\t\t\t 3.删除学生信息')
    print('\t\t\t\t\t 4.修改学生信息')
    print('\t\t\t\t\t 5.排序')
    print('\t\t\t\t\t 6.统计学生总人数')
    print('\t\t\t\t\t 7.显示所有学生信息')
    print('\t\t\t\t\t 0.退出系统')
    print('===================================================================================================================')

def insert():
    stu_list=[]
    while True:
        try:
            id=int(input('学生学号（如1）；'))
            if not id:
                break
            name=input('学生姓名：')
            if not id:
                break
            eg=int(input('请输入英语成绩:'))
            py=int(input('请输入python成绩:'))
            jv=int(input('请输入java成绩:'))
        except Exception as e:
            print(e)
            print('输入错误，重新输入')
            continue
        student={'id':id,'name':name,'eg':eg,'py':py,'jv':jv}
        stu_list.append(student)
        answer=input('录入完毕，是否继续添加y/n:')
        if answer=='y':
            continue
        if answer=='n':
            print('\n')
            break
    save(stu_list)

def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
        pass
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def search():
    data=False
    query=[]
    s1='学生学号'
    s2='学生姓名'
    s3='英语成绩'
    s4='python成绩'
    s5='java成绩'
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            answer=int(input('请选择查询类型（1：学号，2：姓名）：'))
            if answer==2:
                name=input('请输入学生姓名:')
                with open(filename, 'r', encoding='utf-8') as rfile:
                    list1 = rfile.readlines()
                    for item in list1:
                        d=dict(eval(item))
                        try:
                            if d['name']==name:
                                 print('%-8s%-8s%-8s%-8s%-8s' % (s1, s2, s3, s4, s5))
                                 print('%-10d%-10s%-10d%-10d%-10d' % (d['id'], d['name'], d['eg'], d['py'], d['jv']))
                                 data=True
                        except Exception as e:
                            print('发生错误')
                            print(e)
            elif answer==1:
                id=int(input('请输入学生学号:'))
                with open(filename, 'r', encoding='utf-8') as rfile:
                    list1=rfile.readlines()
                    for item in list1:
                        d=dict(eval(item))
                        try:
                            if d['id']==id:
                                print('%-8s%-8s%-8s%-8s%-8s' % (s1, s2, s3, s4, s5))
                                print('%-10d%-10s%-10d%-10d%-10d' % (d['id'], d['name'], d['eg'], d['py'], d['jv']))
                                data=True
                        except Exception as e:
                            print('发生错误')
                            print(e)
            else:
                print('类型输入错误，重新输入')
                continue
            if data==False:
                print('未查找到该学生信息')
            break
        else:
            print('当前无学生信息\n')
    answer = input('是否继续查找y/n:')
    if answer == 'y':
        search()
    else:
        return

def delete():
    while True:
        id=int(input('请输入需要删除学生信息的学号（如1）：'))
        if id!='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    data=file.readlines()
            else:
                data=[]
            flag=False
            if data:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d={}
                    for item in data:
                        d=dict(eval(item))
                        try:
                            if d['id']!=id:
                                 wfile.write(str(d)+'\n')
                            else:
                                 flag=True
                        except:
                            wfile.write(str(d) + '\n')
                    if flag:
                         print(f'id为{id}的学生信息已被删除')
                    else:
                          print(f'不存在id为{id}的学生')
            else:
                print('系统中未有任何数据')
        else:
            print('输入错误，重新输入')
            continue
        print('操作完成，返回', end='\n')
        print('\n')
        answer=input('是否继续删除y/n:')
        if answer=='y':
            continue
        else:
            return

def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            old=rfile.readlines()
    else:
        return '数据暂不存在'
    id = int(input('请输入需要修改学生信息的学号（如1）：'))
    if id != '':
        with open(filename, 'w', encoding='utf-8') as wfile:
            data=False
            for item in old:
                d = dict(eval(item))
                if d['id'] == id:
                    answer=input('找到学生信息，是否修改y/n:')
                    if answer == 'y':
                        while True:
                            try:
                                id = int(input('学生学号（如1）；'))
                                if not id:
                                    break
                                name = input('学生姓名：')
                                if not id:
                                    break
                                eg = int(input('请输入英语成绩:'))
                                py = int(input('请输入python成绩:'))
                                jv = int(input('请输入java成绩:'))
                            except Exception as e:
                                print(e)
                                print('输入错误，重新输入')
                                continue
                            d={'id':id,'name':name,'eg':eg,'py':py,'jv':jv}
                            wfile.write(str(d)+'\n')
                            print('修改成功')
                            data=True
                            break
                else:
                    wfile.write(str(d) + '\n')
            if data==True:
                pass
            else:
                print('未找到学生信息')
    answer = input('是否继续修改y/n:')
    if answer == 'y':
        modify()
    else:
        return

def sort():
    s1 = '学生学号'
    s2 = '学生姓名'
    s3 = '英语成绩'
    s4 = 'python成绩'
    s5 = 'java成绩'
    if os.path.exists(filename):
        answer1=input('请选择升序降序（升1降2）:')
        answer2=input('请选择排序目标（英语1，python2，java3）:')
        list1=[]
        list2=[]
        answer1=int(answer1)
        answer2=int(answer2)
        if answer2 and answer1 :
            with open(filename, 'r', encoding='utf-8') as rfile:
                dut=rfile.readlines()
                if answer1==2:
                    if answer2==1:
                        for item in dut:
                            data = dict(eval(item))
                            list1.append(data['eg'])
                            list2.append(data['id'])
                    if answer2==2:
                        for item in dut:
                            data = dict(eval(item))
                            list1.append(data['py'])
                            list2.append(data['id'])
                    if answer2==3:
                        for item in dut:
                            data = dict(eval(item))
                            list1.append(data['jv'])
                            list2.append(data['id'])
                    dict2=dict(zip(list2,list1))
                    list1 = list(dict2.keys())
                    list2 = list(dict2.values())
                    a = len(list1)
                    for i in range(0, a):
                        for s in range(0, a - i - 1):
                            if list2[s] < list2[s + 1]:
                                b = list2[s]
                                list2[s] = list2[s + 1]
                                list2[s + 1] = b
                                b = list1[s]
                                list1[s] = list1[s + 1]
                                list1[s + 1] = b
                    dict1=dict(zip(list1, list2))
                    for i in range(0,a):
                        for items in dut:
                            d=dict(eval(items))
                            if list1[i]==d['id']:
                                print('%-8s%-8s%-8s%-8s%-8s' % (s1, s2, s3, s4, s5))
                                print('%-10d%-10s%-10d%-10d%-10d' % (d['id'], d['name'], d['eg'], d['py'], d['jv']))
                if answer1==1:
                    if answer2 == 1:
                        for item in dut:
                            data = dict(eval(item))
                            list1.append(data['eg'])
                            list2.append(data['id'])
                    if answer2 == 2:
                        for item in dut:
                            data = dict(eval(item))
                            list1.append(data['py'])
                            list2.append(data['id'])
                    if answer2 == 3:
                        for item in dut:
                            data = dict(eval(item))
                            list1.append(data['jv'])
                            list2.append(data['id'])
                    dict2 = dict(zip(list2, list1))
                    list1 = list(dict2.keys())
                    list2 = list(dict2.values())
                    a = len(list1)
                    for i in range(0, a):
                        for s in range(0, a - i - 1):
                            if list2[s] > list2[s + 1]:
                                b = list2[s]
                                list2[s] = list2[s + 1]
                                list2[s + 1] = b
                                b = list1[s]
                                list1[s] = list1[s + 1]
                                list1[s + 1] = b
                    dict1 = dict(zip(list1, list2))
                    for i in range(0, a):
                        for items in dut:
                            d = dict(eval(items))
                            if list1[i] == d['id']:
                                print('%-8s%-8s%-8s%-8s%-8s' % (s1, s2, s3, s4, s5))
                                print('%-10d%-10s%-10d%-10d%-10d' % (d['id'], d['name'], d['eg'], d['py'], d['jv']))
        else:
            print('输入错误')

    answer3= input('是否再次排序y/n:')
    if answer3== 'y':
        sort()
    else:
        return
def total():
    number = 0
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            list1 = rfile.readlines()
            for item in list1:
                number += 1
    print((f'系统总有{number}名学生'))

def show():
    s1 = '学生学号'
    s2 = '学生姓名'
    s3 = '英语成绩'
    s4 = 'python成绩'
    s5 = 'java成绩'
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            list1 = rfile.readlines()
            for item in list1:
                d=dict(eval(item))
                print('%-8s%-8s%-8s%-8s%-8s' % (s1, s2, s3, s4, s5))
                print('%-10d%-10s%-10d%-10d%-10d' % (d['id'], d['name'], d['eg'], d['py'], d['jv']))
    print('输出完成')

def main():
    while True:
        try:
            menu()
            choice=int(input('请选择功能：'))
            if choice in [0,1,2,3,4,5,6,7]:
                if choice==0:
                    answer=input('是否确定退出系统y/n:')
                    if answer=='y':
                        break
                    if answer=='n':
                        print('\n')
                        continue
                if choice==1:
                     insert()
                if choice ==2:
                    search()
                if choice ==3:
                    delete()
                if choice ==4:
                    modify()
                if choice ==5:
                    sort()
                if choice ==6:
                    total()
                if choice ==7:
                    show()
        except Exception as e:
            print(e)
            print('发生错误，重新运行')
            print('\n')
    print('退出成功')
    print('感谢您的使用')
main()
