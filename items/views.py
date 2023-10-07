from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q

from .forms import ModelForm, ItemForm

from .models import *

from django.urls import reverse

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator

from django.core.paginator import Paginator


# @permission_required('items.add_group', login_url="/auth")
def items(req):
    # ram_types = RamType.objects.all()
    # hdd_types = HDDType.objects.all()
    # cpus = CPU.objects.all()
    # types = Type.objects.all()
    page = req.GET.get('p') if req.GET.get('p') != None else '1'
    filter = req.GET.get('f').lower().strip(
    ) if req.GET.get('f') != None else None

    items = Items.objects.filter(is_available=True)

    if filter:
        items = Items.objects.filter((Q(model__name__contains=filter.strip()) | Q(
            gpu__name__contains=filter.strip())) & Q(is_available=True))

    page_obj = Paginator(items, 12)
    try:
        page_num = page_obj.page(page)
    except:
        page_num = page_obj.page(1)

    context = {'page_num': page_num, 'filter': filter, 'items': page_num}
    return render(req, 'items/home.html', context)


def item(req, id):
    item = Items.objects.get(id=id)

    # print(item.values())
    context = {'item': item}
    return render(req, 'items/item.html', context)


class ModelBase(LoginRequiredMixin, View):
    model = Models
    form_class = ModelForm
    template_name = 'forms/model.html'
    login_url = "/auth"
    # redirect_field_name = "next_page"

    def form_valid(self, form):
        model = form.save()

        images = self.request.FILES.getlist('f')

        if images:
            for image in model.images.all():
                image.delete()

        for image in images:
            model.images.add(
                Image.objects.create(image=image)
            )

        return super().form_valid(form)


class Models(ModelBase, ListView):
    template_name = 'items/models.html'

    def get_queryset(self):
        filterr = self.request.GET.get('f')
        page = self.request.GET.get(
            'p') if self.request.GET.get('p') != None else '1'

        qObject = Q(name__contains=filterr) if filterr else Q(id__isnull=False)

        queryset = Models.objects.filter(qObject)

        page_obj = Paginator(queryset, 20)
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
        return self.request.path


class ModelUpdate(ModelBase, UpdateView):

    def get_success_url(self):
        return reverse('model-list')


class ModelDelete(ModelBase, DeleteView):

    def get_success_url(self):
        return reverse('model-list')


class ItemBase(LoginRequiredMixin, View):
    model = Items
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

        queryset = Items.objects.filter(qObject).order_by(
            '-is_available', 'model__name')

        page_obj = Paginator(queryset, 20)
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

    # Toggle Item availabilty Views
    def post(self, request, pk):
        item = get_object_or_404(Item, id=pk)
        item.is_available = not item.is_available
        item.save()

        return JsonResponse({'success': True})

        # return HttpResponseRedirect(reverse('item-list'))


class ItemCreate(ItemBase, CreateView):
    template_name = 'forms/item.html'

    def get_success_url(self):
        return self.request.path


class ItemUpdate(ItemBase, UpdateView):
    template_name = 'forms/item.html'

    def get_success_url(self):
        return reverse('item-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        item = Items.objects.get(id=self.kwargs.get('pk'))

        context['gpu_type'] = item.gpu
        context['ram_type'] = item.ram_type
        context['hdd_type'] = item.hdd_type
        context['screen_resolution'] = item.screen_resolution
        context['sound_type'] = item.sound_type

        return context


class ItemDelete(ItemBase, DeleteView):
    template_name = 'forms/item.html'

    def get_success_url(self):
        return reverse('item-list')

# def handler404(request, exception):
#     return render(request, 'items/404.html', status=404)
