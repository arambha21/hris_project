from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import TrainingSession
from .forms import TrainingSessionForm

@login_required
def training_session_list(request):
    training_sessions = TrainingSession.objects.all()
    return render(request, 'training/training_session_list.html', {'training_sessions': training_sessions})

@login_required
@permission_required('training.add_trainingsession')
def training_session_create(request):
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Training session created successfully.')
            return redirect('training_session_list')
    else:
        form = TrainingSessionForm()
    return render(request, 'training/training_session_form.html', {'form': form})

@login_required
@permission_required('training.change_trainingsession')
def training_session_update(request, pk):
    training_session = get_object_or_404(TrainingSession, pk=pk)
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST, instance=training_session)
        if form.is_valid():
            form.save()
            messages.success(request, 'Training session updated successfully.')
            return redirect('training_session_list')
    else:
        form = TrainingSessionForm(instance=training_session)
    return render(request, 'training/training_session_form.html', {'form': form, 'training_session': training_session})

@login_required
@permission_required('training.delete_trainingsession')
def training_session_delete(request, pk):
    training_session = get_object_or_404(TrainingSession, pk=pk)
    if request.method == 'POST':
        training_session.delete()
        messages.success(request, 'Training session deleted successfully.')
        return redirect('training_session_list')
    return render(request, 'training/training_session_confirm_delete.html', {'training_session': training_session})

@login_required
def training_session_detail(request, pk):
    training_session = get_object_or_404(TrainingSession, pk=pk)
    return render(request, 'training/training_session_detail.html', {'training_session': training_session})
