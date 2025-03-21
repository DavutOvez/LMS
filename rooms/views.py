from django.shortcuts import render , redirect
from .forms import RoomForm
from .models import Room
from django.utils import timezone
from django.http import JsonResponse
# Create your views here.

def room_table(request):
    rooms = Room.objects.filter(deleted_at = None)
    return render(request,'rooms/table.html',{'all':rooms})

def room_create(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_table')
    return render(request,'rooms/create.html',{'form':form})

def room_edit(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_table')
    return render(request,'rooms/edit.html',{'form':form})

def room_delete(request,pk):
    room = Room.objects.get(id=pk)
    room.deleted_at = timezone.now()
    room.save()
    return redirect('room_table')


def get_room(request):
    room_id = request.GET.get('room_id')
    if room_id:
        room = Room.objects.get(id = room_id)
        return JsonResponse(room.capacity , safe = False)
    return JsonResponse(0 , safe= False)