from django.shortcuts import render
from django.urls import reverse_lazy

from diary_app.models import entry
from django.views.generic import CreateView, UpdateView, DeleteView


# Create your views here.
def entry_display(request):
    entries = entry.objects.all()
    context = {
        'entries': entries
    }
    return render(request, 'index.html', context)


class EntryCreate(CreateView):
    model = entry
    fields = ('entry_title', 'entry_body', 'entry_date',)
    template_name = 'create_entry.html'
    success_url = reverse_lazy('entry_list')


class Edit_entry(UpdateView):
    model = entry
    fields = ('entry_title', 'entry_body', 'entry_date')
    template_name = 'edit_entry.html'
    success_url = reverse_lazy('entry_list')


class Delete_entry(DeleteView):
    model = entry
    template_name = 'delete_entry.html'
    success_url = reverse_lazy('entry_list')
