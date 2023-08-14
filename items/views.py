from django.shortcuts import render
from django.contrib import messages
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q

from .forms import ModelForm, ItemForm

from .models import *

from django.urls import reverse

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

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
    try:
        page_num = page_obj.page(page)
    except:
        page_num = page_obj.page(1)

    context = {'page_num': page_num, 'filter': filter, 'items': page_num, 'ram_types': ram_types,
               'cpus': cpus, 'hdd_types': hdd_types, 'gpus': gpus, 'types': types}
    return render(req, 'items/home.html', context)


def item(req, id):
    item = Item.objects.get(id=id)

    # print(item.values())
    context = {'item': item}
    return render(req, 'items/item.html', context)


class ModelBase(LoginRequiredMixin, View):
    model = Model
    form_class = ModelForm
    template_name = 'forms/model2.html'
    login_url = "/auth"
    # redirect_field_name = "next_page"

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

        if images:
            for image in modell.images.all():
                image.delete()

        for image in images:
            modell.images.add(
                Image.objects.create(image=image)
            )

        return super().form_valid(form)


class Models(ModelBase, ListView):
    template_name = 'items/models.html'

    def get_queryset(self):
        qObject = None

        filterr = self.request.GET.get('f')
        page = self.request.GET.get(
            'p') if self.request.GET.get('p') != None else '1'

        if filterr:
            qObject = Q(name__contains=filterr)
        else:
            qObject = Q(id__isnull=False)

        queryset = Model.objects.filter(qObject)

        page_obj = Paginator(queryset, 9)
        page_num = page_obj.page(page)

        return page_num

    def get_context_data(self, **kwargs):
        context = {
            'models': self.get_queryset(),
            'filter': self.request.GET.get('f')
            # 'labels': list(self.get_queryset()[0].keys()),
            # 'labels': self.get_queryset()._meta.get_fields(),
        }

        return context


class ModelCreate(ModelBase, CreateView):

    def get_success_url(self):
        return reverse('model-list')


class ModelUpdate(ModelBase, UpdateView):

    def get_success_url(self):
        return reverse('model-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['manufacturer'] = Model.objects.get(
            id=self.kwargs.get('pk')).manufacturer
        context['type'] = Model.objects.get(id=self.kwargs.get('pk')).typee

        return context


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


class ItemBase(LoginRequiredMixin, View):
    model = Item
    form_class = ItemForm
    login_url = "/auth"

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


class Items(ItemBase, ListView):
    template_name = 'items/items-list.html'

    def get_queryset(self):
        qObject = None

        page = self.request.GET.get(
            'p') if self.request.GET.get('p') != None else '1'
        filterr = self.request.GET.get('f')

        if filterr:
            qObject = Q(model__name__contains=filterr)
        else:
            qObject = Q(id__isnull=False)

        queryset = Item.objects.filter(qObject)

        page_obj = Paginator(queryset, 9)
        page_num = page_obj.page(page)

        return page_num

    def get_context_data(self, **kwargs):
        context = {
            'items': self.get_queryset(),
            'filter': self.request.GET.get('f')
            # 'labels': list(self.get_queryset()[0].keys()),
            # 'labels': self.get_queryset()._meta.get_fields(),
        }

        return context


class ItemCreate(ItemBase, CreateView):
    template_name = 'forms/item.html'
    success_url = '/'


class ItemUpdate(ItemBase, UpdateView):
    template_name = 'forms/item.html'

    def get_success_url(self):
        return reverse('item-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        item = Item.objects.get(id=self.kwargs.get('pk'))

        context['gpu_type'] = item.gpu
        context['ram_type'] = item.ram_type
        context['hdd_type'] = item.hdd_type
        context['screen_resolution'] = item.screen_resolution
        context['sound_type'] = item.sound_type

        return context

# def handler404(request, exception):
#     return render(request, 'items/404.html', status=404)
