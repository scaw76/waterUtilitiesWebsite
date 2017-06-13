from django.shortcuts import get_object_or_404, render


from .models import Notice

# Create your views here.
def index(request):
	latest_notices_list = Notice.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('publicNotices/index.html')
	context = {'latest_notices_list': latest_notices_list}
	return render(request, 'publicnotices/index.html', context)

def detail(request, notice_id):
	notice = get_object_or_404(Notice, pk=notice_id)
	return render(request,'publicnotices/detail.html', {'notice':notice})