from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.views import View

from .models import *

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.core.paginator import Paginator


# @permission_required('items.add_group', login_url="/auth")
def items(req):
    print(req.path)
    ram_types = RamType.objects.all()
    hdd_types = HDDType.objects.all()
    cpus = CPU.objects.all()
    gpus = GPUType.objects.all()
    types = Type.objects.all()

    page = req.GET.get('p') if req.GET.get('p') != None else '1'
    filter = req.GET.get('f') if req.GET.get('f') != None else None

    items = Item.objects.all()

    if filter:
        items = Item.objects.filter(
            Q(model__name__contains=filter) |
            Q(ram_type__name__contains=filter) |
            Q(gpu__name__contains=filter) |
            Q(hdd_type__name__contains=filter))

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


# class Model(View):
#     model = Model
#     template_name = 'forms/model.html'

#     @method_decorator(login_required)
#     def get(self, req, *args, **kwargs):
#         manufacturers = Manufacturer.objects.all()
#         types = Type.objects.all()

#         ctx = {'manufacturers': manufacturers, 'types': types}
#         return render(req, self.template_name, ctx)

#     @method_decorator(login_required)
#     def post(self, req, *args, **kwargs):
#         manufacturer, created = Manufacturer.objects.get_or_create(
#             name=req.POST.get('manufacturer').lower().strip())
#         typee, created = Type.objects.get_or_create(
#             name=req.POST.get('type').lower().strip())
#         model = req.POST.get('model').lower().strip()
#         note = req.POST.get('note').lower().strip()
#         images = req.FILES.getlist('images')

#         try:
#             model = self.model.objects.create(
#                 manufacturer=manufacturer,
#                 typee=typee,
#                 name=model,
#                 note=note,
#             )

#             for image in images:
#                 model.images.add(
#                     Image.objects.create(image=image)
#                 )
#         except IntegrityError:
#             messages.error(req, 'This model is already exists')

#         return render(req, self.template_name)


@login_required(login_url='/auth')
def modelForm(req):
    manufacturers = Manufacturer.objects.all()
    types = Type.objects.all()

    if req.method == 'POST':
        manufacturer, created = Manufacturer.objects.get_or_create(
            name=req.POST.get('manufacturer').lower().strip())
        typee, created = Type.objects.get_or_create(
            name=req.POST.get('type').lower().strip())
        model = req.POST.get('model').lower().strip()
        note = req.POST.get('note').lower().strip()
        images = req.FILES.getlist('images')

        try:
            m = Model.objects.create(
                manufacturer=manufacturer,
                typee=typee,
                name=model,
                note=note,
            )

            for image in images:
                i = Image.objects.create(image=image)
                m.images.add(i)
        except IntegrityError:
            messages.error(req, 'This model is already exists')

    context = {'manufacturers': manufacturers,
               'types': types}
    return render(req, 'forms/model.html', context)


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


@login_required(login_url='/auth')
def itemForm(req):
    # form = ModelForm()
    models = Model.objects.all()
    cpu_types = CPUType.objects.all()
    ram_types = RamType.objects.all()
    hdd_types = HDDType.objects.all()
    gpu_types = GPUType.objects.all()
    screen_resolutions = ScreenResolution.objects.all()
    sound_types = SoundType.objects.all()

    if req.method == 'POST':
        model = None
        cpu_type = None
        try:
            model = Model.objects.get(
                name=req.POST.get('model').lower().strip())
        except Model.DoesNotExist:
            messages.error(req, 'Model is not exists')
        try:
            cpu_type = CPUType.objects.get(
                cpu_type=req.POST.get('cpu_type').lower().strip())
        except CPUType.DoesNotExist:
            messages.error(req, 'CPUType is not exists')
        cpu_speed = req.POST.get('cpu_speed').lower().strip()
        ram_type, created = RamType.objects.get_or_create(
            name=req.POST.get('ram_type').lower().strip())
        ram_size = req.POST.get('ram_size').lower().strip()
        hdd_type, created = HDDType.objects.get_or_create(
            name=req.POST.get('hdd_type').lower().strip())
        hdd_size = req.POST.get('hdd_size').lower().strip()
        gpu, create = GPUType.objects.get_or_create(
            name=req.POST.get('gpu_type').lower().strip())
        screen_resol, created = ScreenResolution.objects.get_or_create(
            name=req.POST.get('screen_resolution').lower().strip())
        sound_t, created = SoundType.objects.get_or_create(
            name=req.POST.get('sound_type').lower().strip())
        screen_size = req.POST.get('screen_size').strip()
        rotation = req.POST.get('rotation').lower().strip()
        touch_screen = True if req.POST.get('touch_screen') == 'on' else False
        illuminated_keyboard = True if req.POST.get(
            'illuminated_keyboard') == 'on' else False
        original_windows = True if req.POST.get('original_windows') else False
        price = req.POST.get('price').strip()
        disc = req.POST.get('disc').strip()

        try:
            Item.objects.create(
                model=model,
                cpu_type=cpu_type,
                cpu_speed=cpu_speed,
                ram_type=ram_type,
                ram_cache=ram_size,
                hdd_type=hdd_type,
                hdd_size=hdd_size,
                gpu=gpu,
                screen_resolution=screen_resol,
                sound_type=sound_t,
                screen_size=screen_size,
                rotation=rotation,
                touch_screen=touch_screen,
                illuminated_keyboard=illuminated_keyboard,
                original_windows=original_windows,
                price=price,
                disc=disc,
            )
            return redirect('home')
        except IntegrityError:
            messages.error(req, 'Item Already exists...')
        except ValueError:
            messages.error(req, 'Invalid inputs')
        except:
            messages.error(req, 'an error occured')

    context = {'models': models, 'cpu_types': cpu_types, 'ram_types': ram_types, 'hdd_types': hdd_types,
               'gpu_types': gpu_types, 'screen_resolutions': screen_resolutions, 'sound_types': sound_types}
    return render(req, 'forms/item.html', context)


@login_required(login_url='/auth')
def specificationsForm(req):
    screen_resolutions = ScreenResolution.objects.all()
    sound_types = SoundType.objects.all()

    if req.method == 'POST':
        screen_resol, created = ScreenResolution.objects.get_or_create(
            name=req.POST.get('screen_resolution').lower())
        sound_t, created = SoundType.objects.get_or_create(
            name=req.POST.get('sound_type').lower())
        screen_size = req.POST.get('screen_size')
        rotation = req.POST.get('rotation').lower()
        touch_screen = True if req.POST.get('touch_screen') == 'on' else False
        illuminated_keyboard = True if req.POST.get(
            'illuminated_keyboard') == 'on' else False
        original_windows = True if req.POST.get('original_windows') else False

        try:
            Specifications.objects.create(
                screen_resolution=screen_resol,
                sound_type=sound_t,
                screen_size=screen_size,
                rotation=rotation,
                touch_screen=touch_screen,
                illuminated_keyboard=illuminated_keyboard,
                original_windows=original_windows
            )
        except ValueError:
            messages.error(req, 'Invalid values')
        except IntegrityError:
            messages.error(req, 'This specifications alredy exists')

    context = {'screen_resolutions': screen_resolutions,
               'sound_types': sound_types}
    return render(req, 'forms/specifications.html', context)
