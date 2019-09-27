from django.shortcuts import render, redirect, HttpResponse
from app01 import models
import json


# Create your views here.
def p_add(request):
    error_msg = ''
    if request.method == 'POST':
        p_name = request.POST.get('p_name')
        if p_name:
            models.Pushier.objects.create(name=p_name)
            return redirect('/p_select/')
        else:
            error_msg = '404 random not be null'
    return render(request, 'p_add.html', {'error': error_msg})


def p_delete(request):
    p_id = request.GET.get('id')
    ret = models.Pushier.objects.get(id=p_id)
    ret.delete()
    return redirect('/p_select/')


def p_edit(request):
    if request.method == 'POST':
        p_name = request.POST.get('p_name')
        if p_name:
            id = request.POST.get('id')
            reb = models.Pushier.objects.get(id=id)
            reb.name = p_name
            reb.save()
            return redirect('/p_select/')
    p_id = request.GET.get('id')
    print('=' * 30)
    print(p_id)
    k = models.Pushier.objects.get(id=p_id)
    return render(request, 'p_edit.html', {'ret': k.name, 'id': p_id})


def p_select(request):
    ret = models.Pushier.objects.all().order_by('id')
    return render(request, 'p_select.html', {'ret': ret})


def b_add(request):
    error_msg = ''
    if request.method == 'POST':
        b_name = request.POST.get('b_name')
        b_id = request.POST.get('select')
        print('*' * 60)
        print(b_name, b_id)
        if b_name and b_id:
            models.Book.objects.create(name=b_name, pushier_id=b_id)
            return redirect('/b_select/')
        else:
            error_msg = 'ERROR 404'

    res = models.Pushier.objects.all()
    return render(request, 'b_add.html', {'res': res}, {'error': error_msg})


def b_delete(request):
    b_id = request.GET.get('id')
    b_obj = models.Book.objects.get(id=b_id)
    b_obj.delete()
    return redirect('/b_select/')


def b_edit(request):
    if request.method == 'POST':
        b_id01 = request.POST.get('id')
        b_name = request.POST.get('b_name')
        select = request.POST.get('select')
        b_obj1 = models.Book.objects.get(id=b_id01)
        b_obj1.name = b_name
        b_obj1.pushier_id = select
        b_obj1.save()
        return redirect('/b_select/')
    b_id = request.GET.get('id')
    p_obj = models.Pushier.objects.all()
    b_obj = models.Book.objects.get(id=b_id)
    return render(request, 'b_edit.html', {'b_id': b_obj.id,
                                           'b_ret': b_obj.name, 'p_res': p_obj, 'b_push': b_obj.pushier_id})


def b_select(request):
    t = request.get_signed_cookie(key='k', salt='mascom')
    # t = request.COOKIES.get('k1')
    print(t)
    if t != '77':
        return redirect('/ck/asf.html')
    ret = models.Book.objects.all()
    p_obj = models.Pushier.objects.all()
    return render(request, 'b_select.html', {'ret': ret, 'p_obj': p_obj})


def a_select(request):
    t = request.COOKIES.get('k1')
    print(t)
    if t != '123123':
        return redirect('/ck/asf.html')
    obj = models.Auther.objects.all().order_by('id')
    b_obj = models.Book.objects.all().order_by('id')
    return render(request, 'a_select.html', {'ret': obj, 'b_obj': b_obj})


def a_add(request):
    if request.method == 'POST':
        name = request.POST.get('a_name')
        b_id = request.POST.getlist('select')
        ret = models.Auther.objects.create(name=name)
        ret.book.set(b_id)
        return redirect('/a_select/')
    b_obj = models.Book.objects.all()
    return render(request, 'a_add.html', {'ret': b_obj})


def a_delete(request):
    a_id = request.GET.get('id')
    a_obj = models.Auther.objects.get(id=a_id)
    a_obj.delete()
    return redirect("/a_select/")


def a_edit(request):
    if request.method == 'POST':
        name = request.POST.get('b_name')
        id1 = request.POST.get('a_id')
        id2 = request.POST.getlist('select')
        print(id2)
        ret = models.Auther.objects.get(id=id1)
        ret.name = name
        ret.book.set(id2)
        ret.save()
        return redirect('/a_select/')

    b_id = request.GET.get('id')
    a_obj = models.Auther.objects.get(id=b_id)
    b_obj = models.Book.objects.all()
    return render(request, 'a_edit.html', {'name': a_obj.name, 'ret': b_obj, 'a_id': a_obj.id, 'res': a_obj})


def model(request):
    name = request.POST.get('title')
    print('*' * 60)
    print(name)
    if name:
        models.Pushier.objects.create(name=name)
        return HttpResponse('ok')
    else:
        return HttpResponse('用户或密码不能为空')


def edit(request):
    req = {'status': True, 'Error': None}
    name = request.POST.get('name')
    id = request.POST.get('id')
    print('id' + id, 'name' + name)
    if name and id:
        p_obj = models.Pushier.objects.get(id=id)
        p_obj.name = name
        p_obj.save()
    else:
        req['status'] = False
        req['ERROR'] = '用户名不能为空'
    return HttpResponse(json.dumps(req))


def b_myadd(request):
    req = {'status': True, 'ERROR': None}
    b_name = request.POST.get('name')
    id = request.POST.get('id')
    print(b_name, id)
    if b_name and id:
        models.Book.objects.create(name=b_name, pushier_id=id)
    else:
        req['status'] = False
        req['ERROR'] = '内容不能为空'
    return HttpResponse(json.dumps(req))


def b_myedit(request):
    req = {'status': True, 'ERROR': None}
    name = request.POST.get('name')
    b_id = request.POST.get('b_id')
    p_id = request.POST.get('p_id')
    print(name, id)
    if name and id:
        b_obj = models.Book.objects.get(id=b_id)
        b_obj.name = name
        b_obj.pushier_id = p_id
        b_obj.save()
    else:
        req['status'] = False
        req['ERROR'] = '内容不能为空'

    return HttpResponse(json.dumps(req))


def ajax_add(request):
    import json
    req = {'status': True, 'errpr': None}
    name = request.POST.get('name')
    sid = request.POST.getlist('sid')
    if name and sid:
        obj = models.Auther.objects.create(name=name)
        obj.book.set(sid)
    else:
        req['status'] = False
        req['error'] = '404 not found'
    return HttpResponse(json.dumps(req))


from ofen import mymodel1


def student(request, a1):
    current_page = request.GET.get('page')
    count = models.Student.objects.all().count()
    page_info = mymodel1.Page(current_page, 10, count, 11)
    current_list = models.Student.objects.all()[page_info.start():page_info.last()]
    return render(request, 'student.html', {'current_list': current_list, 'page_info': page_info})


def ck(request, a1):
    print(a1)
    if request.method == 'GET':
        return render(request, 'ck.html')
    else:
        name = request.POST.get('c_name')
        pwd = request.POST.get('c_pwd')
        print(name, pwd)
        if name and pwd:
            obj = redirect('/a_select/')
            # obj.set_cookie('k1', '77',max_age=10,path='/b_select/')
            obj.set_cookie('k1', value='123123', max_age=10)
            return obj
        else:
            return redirect('/ck/asf.html')


def ck1(request):
    pass









# class MyModel2:
    # def __init__(self,count,per_page,):























































