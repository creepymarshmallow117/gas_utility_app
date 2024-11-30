from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from consumer_service.models import ServiceRequest

@login_required
def dashboard(request):
    requests = ServiceRequest.objects.all().order_by('created_at')
    status_filter = request.GET.get('status')
    if status_filter:
        requests = requests.filter(status=status_filter)
    return render(request, 'customer_support/dashboard.html', {'requests': requests})

@login_required
def request_detail(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    return render(request, 'customer_support/request_detail.html', {'service_request': service_request})


@login_required
def update_request_status(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        service_request.status = new_status
        service_request.save()
        return redirect('customer_support_dashboard')
    return render(request, 'customer_support/update_request.html', {'service_request': service_request})