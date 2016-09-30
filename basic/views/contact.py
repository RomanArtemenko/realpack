from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def contact(request):
    if request.method == "POST":
        if request.POST.get('send_message') is not None:

            errors = {}
            data = {}

            first_name = request.POST.get('first_name', '').strip()

            if not first_name:
                errors['first_name'] = u"Имя является обязательлным полем"
            else:
                data['first_name'] = first_name#            if not last_name:
#                errors['last_name'] = u"Фамилия является обязательлным полем"
#            else:
#                data['last_name'] = last_name

            phone_number = request.POST.get('phone_number', '').strip()

            if not phone_number:
                errors['phone_number'] = u"Телефон является обязательлным полем"
            else:
                data['phone_number'] = phone_number

            email = request.POST.get('email', '').strip()

            if not email:
                errors['email'] = u"Email является обязательлным полем"
            else:
                data['email'] = email

            message = request.POST.get('message', '').strip()

            if not message:
                errors['message'] = u"Сообщение является обязательлным полем"
            else:
                data['message'] = message

            if not errors:
                return HttpResponseRedirect(u'%s?status_message=Сообщение успешно отправлено!' %reverse('contact'))
            else:
                return render(request, 'basic/contact.html', {'errors' : errors})
    else:
        return render(request, 'basic/contact.html', {})
