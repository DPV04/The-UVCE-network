from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import *
from .forms import roomcreate,MyUserCreationForm,profileform,UserForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home (request):
    
    q= request.GET.get('q') if request.GET.get('q')!=None else''
    rooms=Room.objects.filter(
      Q (topicname__tname__icontains=q) |
      Q (description__icontains=q) |
      Q (name__icontains=q) 
      )
    
    topics=Topic.objects.all()
    room_count = rooms.count()
    room_messages=Messages.objects.filter(Q(room__topicname__tname__icontains=q))
    you=usercredentials.objects.all()
    context={'rooms':rooms , 'room_count': room_count, 'topics':topics,'room_messages':room_messages,'you':you}

    return render(request,'home.html',context)

@login_required(login_url='login')
def userprofile(request,pk):
  

    q= request.GET.get('q') 
    rooms=Room.objects.filter(
      Q (participants__username=q) 
      

     
      )
    
    room_messages=Messages.objects.filter(Q(user__username=q))
    user=User.objects.get(id=pk)
    topics=Topic.objects.all()
    
    

    context={'user':user,'rooms':rooms ,'room_messages':room_messages,'topics':topics,}
    return render(request,'profile.html',context)
       


@login_required(login_url='login')
def rom(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message.all()
    participants = room.participants.all()

    if request.method == 'POST':
        message = Messages.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {'room': room, 'room_messages': room_messages,
               'participants': participants}
    return render(request, 'room.html', context)



@login_required(login_url='login')
def deleteroom(request,pk):
   rom=Room.objects.get(id=pk)   
   if request.method == 'POST':
      rom.delete()
      return redirect('home')
   return render(request,'delete.html',{'ob':rom})


@login_required(login_url='login')
def deletemessages(request,pk):
  messages=Messages.objects.get(id=pk)   
  if request.method == 'POST':
      messages.delete()
      return redirect('home')
  return render(request,'delete.html',{'ob':messages})


@login_required(login_url='login')
def enterroomdetails(request):
   form=roomcreate()
   topics=Topic.objects.all()
   

  
   if request.method == 'POST':
          topicname=request.POST.get('topic')
          topic , created=Topic.objects.get_or_create(tname=topicname)
          Room.objects.create(
             host=request.user,
             topicname=topic,
             name=request.POST.get('name'),
             Photo=request.FILES.get('Photo'),
             description=request.POST.get('description')
          )
          return redirect('home')
   context={'form':form,'topics':topics}

   return render(request,'chatroom.html',context)

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('userprofile', pk=user.id)

    return render(request, 'updateuser.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/login/')  # Redirect to login page after successful registration
    else:
        form = MyUserCreationForm()
    return render(request, 'login.html', {'form': form})




def user_logout(request):
    logout(request)
    return redirect('login')







def logunpage(request):
   page = 'login'
   if request.user.is_authenticated:
        return redirect('home')

   if request.user.is_authenticated:
      return redirect('home')
   if request.method=="POST":
      username=request.POST.get('username')    
      password=request.POST.get('password')    

      try:
         user=User.objects.get(username=username)
         messages.error(request,"user  exist")  

      except:
         messages.error(request,"user does not exist")  

      user=authenticate(request,username=username,password=password)   

      if user is not None:
         login(request,user)
         return redirect('feed')


      else:
         messages.error(request,"username or password not correct")   
   context={'page':page}
   return render(request,'login.html',context)      





@login_required(login_url='login')
def uploads(request, pk):
 
    room = get_object_or_404(Room, id=pk)


    if request.method == 'POST':
        image = request.FILES.get('image')
        print(image)
        description=request.POST.get('description')

        upload_instance = upload.objects.create(name=room,interestsname=room.topicname.tname, image=image,description=description)
        upload_instance.save()
     

        return redirect('home')  
       

    return render(request, 'upload.html', {'room': room})



@login_required(login_url='login')
def interest(request):
     if request.method == 'POST':
        form = profileform(request.POST)
        if form.is_valid():
      
             year = form.cleaned_data['year']
             branch = form.cleaned_data['branch']
             interests = form.cleaned_data['interests']
             bio = form.cleaned_data['bio']
    

             usercredentials.objects.create(

                name=request.user,
                year=year,
                branch=branch,
                interests=interests,
                bio=bio
                   )
             return redirect('home')
      
      
     else:
      form = profileform()
     
     topics=Topic.objects.all()
     return render(request, 'credentials.html', {'form': form,'topic': topics})







@login_required(login_url='login')
def home (request):
    
    q= request.GET.get('q') if request.GET.get('q')!=None else''
    rooms=Room.objects.filter(
      Q (topicname__tname__icontains=q) |
      Q (description__icontains=q) |
      Q (name__icontains=q) 
      )
    
    topics=Topic.objects.all()
    room_count = rooms.count()
    room_messages=Messages.objects.filter(Q(room__topicname__tname__icontains=q))
    context={'rooms':rooms , 'room_count': room_count, 'topics':topics,'room_messages':room_messages}

    return render(request,'home.html',context)

@login_required(login_url='login')
def feeds(request):
    q= request.GET.get('q') if request.GET.get('q') != None else''

    uploads=upload.objects.filter(
        Q (interestsname__icontains=q) 
    )
    users=User.objects.filter(
        Q (interests__icontains=q) 
    )
    topics=Topic.objects.all()
    context={'uploads':uploads,'users':users,'topics':topics}

    return render(request,'feed.html',context)

