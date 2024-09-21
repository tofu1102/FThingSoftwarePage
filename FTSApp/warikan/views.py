from django.shortcuts import render
from .models import Event
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import PaymentForm

@login_required
def index(request):
    user = request.user
    events = Event.objects.filter(members=user).order_by('-last_updated')
    return render(request, 'warikan/index.html', {'events': events})


@login_required
def event_detail(request, uuid):
    event = get_object_or_404(Event, uuid=uuid)

    if request.method == "POST":
        form = PaymentForm(event, request.POST)  # eventを最初の引数として渡す
        if form.is_valid():
            payment = form.save(commit=False)
            payment.event = event
            payment.save()
            form.save_m2m()  # ManyToManyフィールドを保存
            # リダイレクトや他の処理
        else:
            print("Form is invalid:", form.errors)
    else:
        form = PaymentForm(event)  # eventを最初の引数として渡す

    return render(request, 'warikan/event_detail.html', {'event': event, 'form': form})

@login_required
def payment_list(request, event_uuid):
    event = get_object_or_404(Event, uuid=event_uuid)
    payments = event.payment_set.all().order_by('-created_at')
    return render(request, 'warikan/payment_list.html', {'event': event, 'payments': payments})

def payment_detail(request, event_uuid, payment_uuid):
    return HttpResponse("payment_detail")


# Create your views here.
