from urllib import response
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

from django.db.models import Q

from .forms import ModelForm, ManufacturerForm, ItemForm

from .models import *

from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator

from django.core.paginator import Paginator


# @permission_required('items.add_group', login_url="/auth")
def items(req):
    ram_types = RamType.objects.all()
    hdd_types = HDDType.objects.all()
    cpus = CPU.objects.all()
    gpus = GPUType.objects.all()
    types = Type.objects.all()

    page = req.GET.get('p') if req.GET.get('p') != None else '1'
    filter = req.GET.get('f') if req.GET.get('f') != None else None

    items = Item.objects.filter(is_available=True)

    if filter:
        items = Item.objects.filter(
            Q(model__name__contains=filter.strip()) & Q(is_available=True))

    page_obj = Paginator(items, 9)
    page_num = page_obj.page(page)

    context = {'page_num': page_num, 'filter': filter, 'items': page_num, 'ram_types': ram_types,
               'cpus': cpus, 'hdd_types': hdd_types, 'gpus': gpus, 'types': types}
    return render(req, 'items/home.html', context)


def item(req, id):
    item = Item.objects.get(id=id)

    # print(item.values())
    context = {'item': item}
    return render(req, 'items/item.html', context)


class ModelBase(View):
    model = Model
    form_class = ModelForm
    template_name = 'forms/model2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['manufacturers'] = Manufacturer.objects.all()
        context['types'] = Type.objects.all()

        return context

    def form_valid(self, form):
        modell = form.save(commit=False)

        manufacturer, create = Manufacturer.objects.get_or_create(
            name=self.request.POST.get('manufacturer').lower().strip())
        typee, create = Type.objects.get_or_create(
            name=self.request.POST.get('type').lower().strip())

        modell.manufacturer = manufacturer
        modell.typee = typee
        modell.save()

        images = self.request.FILES.getlist('f')

        modell.images.all().delete()
        for image in images:
            modell.images.add(
                Image.objects.create(image=image)
            )

        return super().form_valid(form)


class ModelCreate(ModelBase, CreateView):
    success_url = 'create'
    pass


class ModelUpdate(ModelBase, UpdateView):
    success_url = ''
    pass


class ManufacturerBase(View):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = 'forms/manufacturer.html'
    success_url = 'create'


class ManufacturerCreate(ManufacturerBase, CreateView):
    pass


@login_required(login_url='/auth')
def cpuForm(req):
    cpus = CPU.objects.all()

    if req.method == 'POST':
        cpu, created = CPU.objects.get_or_create(
            name=req.POST.get('manufacturer').lower().strip())
        typee = req.POST.get('type').lower().strip()

        try:
            CPUType.objects.create(
                name=cpu,
                cpu_type=typee,
            )
            # return redirect('home')
        except:
            messages.error(req, 'This cpu type is already exists')

    context = {'cpus': cpus}
    return render(req, 'forms/cpu.html', context)


class ItemBase(View):
    model = Item
    form_class = ItemForm
    template_name = 'forms/item.html'

    def form_valid(self, form):
        item = form.save(commit=False)

        ram_type, create = RamType.objects.get_or_create(
            name=self.request.POST.get('ram_type').lower().strip())
        hdd_type, create = HDDType.objects.get_or_create(
            name=self.request.POST.get('hdd_type').lower().strip())
        gpu, create = GPUType.objects.get_or_create(
            name=self.request.POST.get('gpu_type').lower().strip())
        screen_resolution, create = ScreenResolution.objects.get_or_create(
            name=self.request.POST.get('screen_resolution').lower().strip())
        sound_type, create = SoundType.objects.get_or_create(
            name=self.request.POST.get('sound_type').lower().strip())

        item.ram_type = ram_type
        item.hdd_type = hdd_type
        item.gpu = gpu
        item.screen_resolution = screen_resolution
        item.sound_type = sound_type

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['gpu_types'] = GPUType.objects.all()
        context['ram_types'] = RamType.objects.all()
        context['hdd_types'] = HDDType.objects.all()
        context['screen_resolutions'] = ScreenResolution.objects.all()
        context['sound_types'] = SoundType.objects.all()

        return context


class ItemCreate(ItemBase, CreateView):
    success_url = '/'


# def handler404(request, exception):
#     return render(request, 'items/404.html', status=404)
