from .models import Event, Payment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import PaymentForm, EventForm
from .warikan_calculater import calculate_settlement
import json

@login_required
def index(request):
    user = request.user
    events = Event.objects.filter(members=user).order_by('-last_updated')
    return render(request, 'warikan/index.html', {'events': events})


@login_required
def event_detail(request, uuid):
    event = get_object_or_404(Event, uuid=uuid)
    latest_payments = event.payment_set.order_by('-created_at')[:5]

    if request.method == "POST":
        form = PaymentForm(event, request.POST, request.FILES)  # request.FILESを追加
        if form.is_valid():
            payment = form.save(commit=False)
            payment.event = event
            payment.save()
            form.save_m2m()  # ManyToManyフィールドを保存
            return redirect("warikan:event_detail", uuid=event.uuid)
        else:
            print("Form is invalid:", form.errors)
    else:
        form = PaymentForm(event)

    return render(request, 'warikan/event_detail.html', {
        'event': event,
        'form': form,
        'latest_payments': latest_payments
    })


@login_required
def payment_list(request, event_uuid):
    event = get_object_or_404(Event, uuid=event_uuid)
    payments = event.payment_set.all().order_by('-created_at')
    return render(request, 'warikan/payment_list.html', {'event': event, 'payments': payments})

@login_required
def payment_detail(request, event_uuid, payment_uuid):
    event = Event.objects.get(uuid=event_uuid)
    payment = get_object_or_404(Payment, uuid=payment_uuid)

    if request.method == "POST":
        form = PaymentForm(event, request.POST, request.FILES, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('warikan:payment_detail', event_uuid=event_uuid, payment_uuid=payment_uuid)
    else:
        form = PaymentForm(event, instance=payment)
        # payeeフィールドの初期値を設定
        form.fields['payee'].initial = payment.payee.all().values_list('uuid', flat=True)

    return render(request, 'warikan/payment_detail.html', {
        'form': form,
        'event': payment.event
    })


@login_required
def confirmation(request, uuid):
    event = Event.objects.get(uuid=uuid)
    settlements = calculate_settlement(event)
    
    # settlementsのキーをユーザーのusernameに変更
    settlements_dict = {payer.username: {recipient.username: amount for recipient, amount in recipients.items()} for payer, recipients in settlements.items()}
    
    context = {
        'event': event,
        'settlements': json.dumps(settlements_dict),  # 修正後のsettlements_dictを渡す
    }
    return render(request, 'warikan/confirmation.html', context)

@login_required
def add_event(request):
    user = request.user
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)  # 一旦保存を延期
            event.save()  # イベントを保存してから
            event.members.add(user)  # userをmembersに追加
            return redirect('warikan:index')
    else:
        form = EventForm()

    return render(request, 'warikan/add_event.html', {'form': form})

@login_required
def invite(request, event_uuid):
    user = request.user
    event =  Event.objects.get(uuid=event_uuid)
    event.members.add(user)
    return redirect("warikan:index")

# Create your views here.
