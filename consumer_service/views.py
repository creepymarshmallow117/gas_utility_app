from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest


@login_required
def dashboard(request):
    return render(request, 'consumer_service/dashboard.html')

# code related to requests
@login_required
def create_service_request(request):
    if request.method == "POST":
        request_type = request.POST['request_type']
        details = request.POST['details']
        file_attachment  = request.FILES.get('file_attachment')
        
        ServiceRequest.objects.create(
            user=request.user,
            request_type=request_type,
            details=details,
            file_attachment=file_attachment,
        )

        return redirect('track_requests')
    
    return render(request, 'consumer_service/create_request.html')

@login_required
def track_requests(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'consumer_service/track_requests.html', {'requests': requests})
