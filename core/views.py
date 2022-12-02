from django.shortcuts import render


def root(request):
    return render(request, 'root.html')


def index(request):
    return render(request, 'pages/index.html')


def charts_flot(request):
    return render(request, 'pages/flot.html')


def charts_morris(request):
    return render(request, 'pages/morris.html')


def tables(request):
    return render(request, 'pages/tables.html')


def forms(request):
    return render(request, 'pages/forms.html')


def ui_panels_wells(request):
    return render(request, 'pages/panels-wells.html')


def ui_buttons(request):
    return render(request, 'pages/buttons.html')


def ui_notifications(request):
    return render(request, 'pages/notifications.html')


def ui_typography(request):
    return render(request, 'pages/typography.html')


def ui_icons(request):
    return render(request, 'pages/icons.html')


def ui_grid(request):
    return render(request, 'pages/grid.html')


def samples_blank(request):
    return render(request, 'pages/blank.html')


def samples_login(request):
    return render(request, 'pages/login.html')
