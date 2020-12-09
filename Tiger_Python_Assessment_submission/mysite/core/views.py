from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import BookForm
from .models import Book
from .main import main

from IPython import embed
import os

class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


def book_list(request):
    books = Book.objects.all()
    for book in books:

        csv_files_address = "/home/sahit/Documents/MLE_opportunities_with_Tiger_Analytics/simple_dj_docker/media/CSV_files/"
        html_files_address = "/home/sahit/Documents/MLE_opportunities_with_Tiger_Analytics/simple_dj_docker/media/HTML_files/"

        if os.path.isfile(os.path.join(csv_files_address, os.path.basename(book.__dict__['chicago_collision_data']).replace('.json', '.csv'))):

            # CSV files
            book.csv_chicago_collision_data = os.path.join('CSV_files', os.path.basename(book.__dict__['chicago_collision_data']).replace('.json', '.csv'))
            book.csv_flight_call = os.path.join('CSV_files', os.path.basename(book.__dict__['flight_call']).replace('.json', '.csv'))
            book.csv_light_levels = os.path.join('CSV_files', os.path.basename(book.__dict__['light_levels']).replace('.json', '.csv'))
            book.csv_chicago_collision_data_merged = os.path.join('CSV_files', os.path.basename(book.__dict__['chicago_collision_data']).replace('.json', '_merged.csv'))

            # HTML files
            book.html_chicago_collision_data = os.path.join('HTML_files', os.path.basename(book.__dict__['chicago_collision_data']).replace('.json', '.html'))
            book.html_flight_call = os.path.join('HTML_files', os.path.basename(book.__dict__['flight_call']).replace('.json', '.html'))
            book.html_light_levels = os.path.join('HTML_files', os.path.basename(book.__dict__['light_levels']).replace('.json', '.html'))
            book.html_chicago_collision_data_merged = os.path.join('HTML_files', os.path.basename(book.__dict__['chicago_collision_data']).replace('.json', '_merged.html'))

        else:
            # call methods from Data_Processing
            # EDA of the individual files and the cumulative files
            # save the summary PDFs to seperate folders
            path_chicago_collision_data = os.path.join('/home/sahit/Documents/MLE_opportunities_with_Tiger_Analytics/simple_dj_docker/media', str(book.chicago_collision_data))
            path_flight_call = os.path.join('/home/sahit/Documents/MLE_opportunities_with_Tiger_Analytics/simple_dj_docker/media', str(book.flight_call))
            path_light_levels = os.path.join('/home/sahit/Documents/MLE_opportunities_with_Tiger_Analytics/simple_dj_docker/media', str(book.light_levels))
            main(path_chicago_collision_data, path_flight_call, path_light_levels)
            # os.system('python mysite/core/main.py path_chicago_collision_data path_flight_call path_light_levels')

            # Save the addresses to the the "book" dictionary
            # CSV files
            book.csv_chicago_collision_data = os.path.join('CSV_files', os.path.basename(path_chicago_collision_data).replace('.json', '.csv'))
            book.csv_flight_call = os.path.join('CSV_files', os.path.basename(path_flight_call).replace('.json', '.csv'))
            book.csv_light_levels = os.path.join('CSV_files', os.path.basename(path_light_levels).replace('.json', '.csv'))
            book.csv_chicago_collision_data_merged = os.path.join('CSV_files', os.path.basename(path_chicago_collision_data).replace('.json', '_merged.csv'))

            # HTML files
            book.html_chicago_collision_data = os.path.join('HTML_files', os.path.basename(path_chicago_collision_data).replace('.json', '.html'))
            book.html_flight_call = os.path.join('HTML_files', os.path.basename(path_flight_call).replace('.json', '.html'))
            book.html_light_levels = os.path.join('HTML_files', os.path.basename(path_light_levels).replace('.json', '.html'))
            book.html_chicago_collision_data_merged = os.path.join('HTML_files', os.path.basename(path_chicago_collision_data).replace('.json', '_merged.html'))

    return render(request, 'book_list.html', {
        'books': reversed(books)
    })


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })