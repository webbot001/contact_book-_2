from django.shortcuts import render , redirect
from contact_app.models import user_data , contacts_data

# Create your views here.
def home(request):
    email = password = ''
    if 'user_name' in request.session:
        return redirect('/dashboard')
    else:
        if 'login' in request.POST:

            email = request.POST['em']
            password = request.POST['pss']

            if email == '' or password == '':
                msg = 'Empty Email or Password !'
                return render(request,'index.html',{'msg':msg})

            obj = user_data.objects.filter(email=email,password=password)

            msg = ''
            if obj.count() == 1:
                row = obj.get()
                request.session['user_id'] = row.id
                return redirect('dashboard/',{'user':row.username})
            else:
                msg = 'Invalid Email or Password !'
                return render(request,'index.html',{'msg':msg})
        else:
            return render(request,'index.html')

# Register page
def register(request):
    if 'register' in request.POST:
        
        a_username = request.POST['un']
        a_email = request.POST['em']
        a_password = request.POST['pss']

        obj = user_data(
            username = a_username,
            email = a_email,
            password = a_password
        )
        obj.save()
        return redirect('/')

    return render(request,'register_page.html')

# Dashboard page
def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        id = request.session['user_id']
        obj = contacts_data.objects.filter(added_by=id)
        obj2 = user_data.objects.filter(id=id)
        row = obj2.get() 
        return render(request,'dashboard.html',{'user':row.username,'email':row.email,'obj':obj})

def remove(request,del_id):
    print(del_id)
    user_data.objects.filter(id=del_id).delete()
    return redirect('/dashboard')

def logout(request):
    del request.session['user_name']
    del request.session['user_id']
    return redirect('/')

def edit_pro(request):
        
        data = user_data.objects.filter(id=request.session['user_id']).get()
        if 'update' in request.POST:
            a_name = request.POST['un']
            a_email = request.POST['em']
            a_password = request.POST['pss']

            data.username = a_name
            data.email = a_email
            data.password = a_password

            data.save()
            return redirect('/dashboard')
        return render(request,'edit_pro.html',{'row':data})

def add_cnt(request):
    if 'add' in request.POST:
        name = request.POST['nm']
        email = request.POST['em']
        contact = request.POST['cnt']
        city = request.POST['ct']
        gender = request.POST['gn']

        obj = contacts_data(
            added_by = request.session['user_id'],
            name = name,
            email = email,
            contact = contact,
            city = city,
            gender = gender
        )
        obj.save()
        return redirect('/dashboard')
    return render(request,'contact_management.html',{'btn':'Add contact'})

def cnt_show(request):
    return render(request,'contact_management.html',{'btn':'Add Contact'})

def remove_contact(request,del_id):
    contacts_data.objects.filter(id=del_id).delete()
    return redirect('/dashboard')

def update_contact(request,upd_id):

    data = contacts_data.objects.filter(id=upd_id).get()
    btn = 'Update'
    if 'add' in request.POST:
        a_name = request.POST['nm']
        a_email = request.POST['em']
        a_contact = request.POST['cnt']
        a_gender = request.POST['gn']
        a_city = request.POST['ct']
        
        data.name = a_name
        data.email = a_email
        data.contact = a_contact
        data.gender = a_gender
        data.city = a_city
        data.save()
        return redirect('/dashboard')
    return render(request,'contact_management.html',{'row':data,'btn':btn})