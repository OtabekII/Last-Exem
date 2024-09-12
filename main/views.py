from django.shortcuts import render, get_object_or_404, redirect
from .models import Staff, Position, Shift, StaffShift, StaffAttendance
from django.shortcuts import render, HttpResponse
from .models import Staff, Position, Shift, StaffShift, StaffAttendance
from faker import Faker
from random import choice
from datetime import timedelta
from django.utils import timezone


def staff_search(request):
    query = request.GET.get('q')  # Qidiruv so'zini olish
    if query:
        # `icontains` yordamida qidiruv so'ziga mos keladigan natijalarni olish (case insensitive)
        results = Staff.objects.filter(full_name__icontains=query)
    else:
        results = Staff.objects.none()  # Agar so'rov bo'lmasa, hech qanday natija qaytarmaslik

    return render(request, 'search_results.html', {'results': results, 'query': query})



def staff_list(request):
    staffs = Staff.objects.all()
    return render(request, 'staff_list.html', {'staffs': staffs})

def staff_create(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        staff = Staff(full_name=full_name, phone_number=phone_number, address=address)
        staff.save()
        return redirect('staff_list')
    
    return render(request, 'staff_form.html')

def staff_update(request, pk):
    staff = get_object_or_404(Staff, pk=pk)

    if request.method == 'POST':
        staff.full_name = request.POST.get('full_name')
        staff.phone_number = request.POST.get('phone_number')
        staff.address = request.POST.get('address')
        staff.save()
        return redirect('staff_list')
    
    return render(request, 'staff_form.html', {'staff': staff})

def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)

    if request.method == 'POST':
        staff.delete()
        return redirect('staff_list')
    
    return render(request, 'staff_confirm_delete.html', {'staff': staff})


def position_list(request):
    positions = Position.objects.all()
    return render(request, 'position_list.html', {'positions': positions})

def position_create(request):
    staffs = Staff.objects.all()
    
    if request.method == 'POST':
        title = request.POST.get('title')
        staff_id = request.POST.get('staff')
        staff = get_object_or_404(Staff, id=staff_id)

        position = Position(title=title, staff=staff)
        position.save()
        return redirect('position_list')
    
    return render(request, 'position_create.html', {'staffs': staffs})

def position_update(request, pk):
    position = get_object_or_404(Position, pk=pk)
    staffs = Staff.objects.all()

    if request.method == 'POST':
        position.title = request.POST.get('title')
        staff_id = request.POST.get('staff')
        position.staff = get_object_or_404(Staff, id=staff_id)
        position.save()
        return redirect('position_list')
    
    return render(request, 'position_form.html', {'position': position, 'staffs': staffs})

def position_delete(request, pk):
    position = get_object_or_404(Position, pk=pk)

    if request.method == 'POST':
        position.delete()
        return redirect('position_list')
    
    return render(request, 'position_confirm_delete.html', {'position': position})

def shift_list(request):
    shifts = Shift.objects.all()
    return render(request, 'shift_list.html', {'shifts': shifts})

def shift_create(request):
    staffs = Staff.objects.all()
    
    if request.method == 'POST':
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        staff_id = request.POST.get('staff')
        staff = get_object_or_404(Staff, id=staff_id)

        shift = Shift(start_time=start_time, end_time=end_time, staff=staff)
        shift.save()
        return redirect('shift_list')
    
    return render(request, 'shift_form.html', {'staffs': staffs})

def shift_update(request, pk):
    shift = get_object_or_404(Shift, pk=pk)
    staffs = Staff.objects.all()

    if request.method == 'POST':
        shift.start_time = request.POST.get('start_time')
        shift.end_time = request.POST.get('end_time')
        staff_id = request.POST.get('staff')
        shift.staff = get_object_or_404(Staff, id=staff_id)
        shift.save()
        return redirect('shift_list')
    
    return render(request, 'shift_form.html', {'shift': shift, 'staffs': staffs})

def shift_delete(request, pk):
    shift = get_object_or_404(Shift, pk=pk)

    if request.method == 'POST':
        shift.delete()
        return redirect('shift_list')
    
    return render(request, 'shift_confirm_delete.html', {'shift': shift})

def shiftstaff_list(request):
    shifts = StaffShift.objects.all()
    return render(request, 'shiftstaff_list.html', {'shifts': shifts})

def shiftstaff_create(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff')
        shift_id = request.POST.get('shift')
        position_id = request.POST.get('position')

        StaffShift.objects.create(
            staff_id=staff_id,
            shift_id=shift_id,
            position_id=position_id
        )
        return redirect('shiftstaff_list')

    staff_list = Staff.objects.all()
    shift_list = Shift.objects.all()
    position_list = Position.objects.all()
    return render(request, 'shiftstaff_create.html', {
        'staff_list': staff_list,
        'shift_list': shift_list,
        'position_list': position_list
    })

def shiftstaff_update(request, pk):
    shift_staff = get_object_or_404(StaffShift, pk=pk)
    if request.method == 'POST':
        shift_staff.staff_id = request.POST.get('staff')
        shift_staff.shift_id = request.POST.get('shift')
        shift_staff.position_id = request.POST.get('position')
        shift_staff.save()
        return redirect('shiftstaff_list')

    staff_list = Staff.objects.all()
    shift_list = Shift.objects.all()
    position_list = Position.objects.all()
    return render(request, 'shiftstaff_update.html', {
        'shift_staff': shift_staff,
        'staff_list': staff_list,
        'shift_list': shift_list,
        'position_list': position_list
    })

def shiftstaff_delete(request, pk):
    shift_staff = get_object_or_404(StaffShift, pk=pk)
    if request.method == 'POST':
        shift_staff.delete()
        return redirect('shiftstaff_list')
    return render(request, 'shiftstaff_confirm_delete.html', {'shift_staff': shift_staff})



def staff_attands_list(request):
    staff_attands = StaffAttendance.objects.all()  
    return render(request, 'staff_attands_list.html', {'staff_attands': staff_attands})



def generate_fake_data(request):
    fake = Faker()

    for _ in range(10):
        staff_member = Staff.objects.create(
            full_name=fake.name(),
            phone_number=fake.phone_number(),
            address=fake.address(),
            email=fake.email(),
        )

        position = Position.objects.create(
            title=fake.job(),
            description=fake.text(),
            staff=staff_member
        )

        start_time = timezone.now() + timedelta(days=fake.random_int(min=1, max=10))
        end_time = start_time + timedelta(hours=fake.random_int(min=4, max=8))
        shift = Shift.objects.create(
            start_time=start_time,
            end_time=end_time
        )

        StaffShift.objects.create(
            staff=staff_member,
            shift=shift,
            position=position
        )

        StaffAttendance.objects.create(
            staff=staff_member,
            shift=shift,
            date=shift.start_time.date(),
            status=choice(['Present', 'Absent', 'Late'])
        )

    return HttpResponse("Fake data has been added successfully!")
