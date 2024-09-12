from django.db import models

class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return self.full_name


class Position(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Shift(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Smena: {self.start_time} - {self.end_time}"


class StaffShift(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.staff.full_name} -> {self.shift}"


class StaffAttendance(models.Model):
    ATTENDANCE_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ]

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES)

    def __str__(self):
        return f"{self.staff.full_name} - {self.date} - {self.status}"
