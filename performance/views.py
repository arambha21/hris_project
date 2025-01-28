from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import PerformanceReview
from .forms import PerformanceReviewForm

@login_required
@permission_required('performance.view_performancereview')
def performance_review_list(request):
    performance_reviews = PerformanceReview.objects.all()
    return render(request, 'performance/performance_review_list.html', {'performance_reviews': performance_reviews})

@login_required
@permission_required('performance.add_performancereview')
def performance_review_create(request):
    if request.method == 'POST':
        form = PerformanceReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Performance review created successfully.')
            return redirect('performance_review_list')
    else:
        form = PerformanceReviewForm()
    return render(request, 'performance/performance_review_form.html', {'form': form})

@login_required
@permission_required('performance.change_performancereview')
def performance_review_update(request, pk):
    performance_review = get_object_or_404(PerformanceReview, pk=pk)
    if request.method == 'POST':
        form = PerformanceReviewForm(request.POST, instance=performance_review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Performance review updated successfully.')
            return redirect('performance_review_list')
    else:
        form = PerformanceReviewForm(instance=performance_review)
    return render(request, 'performance/performance_review_form.html', {'form': form, 'performance_review': performance_review})

@login_required
@permission_required('performance.delete_performancereview')
def performance_review_delete(request, pk):
    performance_review = get_object_or_404(PerformanceReview, pk=pk)
    if request.method == 'POST':
        performance_review.delete()
        messages.success(request, 'Performance review deleted successfully.')
        return redirect('performance_review_list')
    return render(request, 'performance/performance_review_confirm_delete.html', {'performance_review': performance_review})

@login_required
@permission_required('performance.view_performancereview')
def performance_review_detail(request, pk):
    performance_review = get_object_or_404(PerformanceReview, pk=pk)
    return render(request, 'performance/performance_review_detail.html', {'performance_review': performance_review})
