from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import render, redirect
from rest_framework import views, permissions
from rest_framework.response import Response

from DataAggregate.models import AggregateData
from api.orchestrator import orchestrator


class AggregateView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        qs = (
            AggregateData.objects
            .filter(load_file__user=request.user)
            .values('group_by_value')
            .annotate(total=Sum('aggregate_value'))
            .order_by('group_by_value')
        )
        data = [
            {'year': row['group_by_value'], 'total_impr': round(row['total'])}
            for row in qs
        ]
        return Response(data)


@login_required
def index(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if not file:
            messages.error(request, 'No file selected.')
        else:
            try:
                orchestrator(file_name=file.name, file_patch=file, user=request.user)
                messages.success(request, f'File "{file.name}" uploaded successfully.')
            except Exception as e:
                messages.error(request, str(e))
        return redirect('index')

    rows = (
        AggregateData.objects
        .filter(load_file__user=request.user)
        .values('group_by_value')
        .annotate(total=Sum('aggregate_value'))
        .order_by('group_by_value')
    )
    table = [{'year': r['group_by_value'], 'total_impr': round(r['total'])} for r in rows]
    return render(request, 'index.html', {'table': table})