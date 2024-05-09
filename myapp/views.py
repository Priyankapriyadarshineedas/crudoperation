from django.http import JsonResponse, HttpResponse
from django.views import View

from .models import Person
from django.shortcuts import render, redirect
from .forms import RegistrationForm, CreateAddressForm
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Address
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import Account
from .forms import AccountForm


class IndexView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        try:
            form = RegistrationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return JsonResponse({'status': 'success'}, status=201)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    def get(self, request):
        form = RegistrationForm()  # Create an instance of the form without data
        return render(request, 'myapp/index.html', {'form': form})


# views.py


class RetrievePersonView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, person_id):
        person = get_object_or_404(Person, pk=person_id)
        return render(request, 'myapp/person_detail.html', {'person': person})

    def post(self, request, person_id):
        return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)


class UpdatePersonView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, person_id):
        person = get_object_or_404(Person, pk=person_id)
        form = RegistrationForm(instance=person)
        return render(request, 'myapp/person_update.html', {'form': form, 'person': person})

    def post(self, request, person_id):
        person = get_object_or_404(Person, pk=person_id)
        form = RegistrationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/update_success.html')
        else:
            return render(request, 'myapp/person_update.html', {'form': form, 'person': person})


class DeletePersonView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, person_id):
        person = get_object_or_404(Person, pk=person_id)
        person.delete()
        return JsonResponse({'status': 'success'})

    def delete(self, request, person_id):
        person = get_object_or_404(Person, pk=person_id)
        person.delete()
        return JsonResponse({'status': 'success'})

    def get(self, request, person_id):
        person = get_object_or_404(Person, pk=person_id)
        return render(request, 'myapp/confirm_delete.html', {'person': person})


class AllPersonsView(View):
    def get(self, request):
        persons = Person.objects.all()
        return render(request, 'myapp/all_persons.html', {'persons': persons})


class SuccessPageView(View):
    def get(self, request):
        return render(request, 'myapp/success_page.html')


class LoginuccessPageView(View):
    def get(self, request):
        return render(request, 'myapp/loginsuccess.html')


class HomePageView(View):
    def get(self, request):
        return render(request, 'myapp/home.html')


class AddressView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        form = CreateAddressForm(request.POST)
        if form.is_valid():
            street = form.cleaned_data['street']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = int(form.cleaned_data['zipcode'])

            # Get list of selected person IDs
            persons_ids = form.cleaned_data['persons']

            # Retrieve Person objects based on IDs
            persons = Person.objects.filter(id__in=persons_ids)

            # Create and save the Address object
            address = Address.objects.create(
                street=street,
                city=city,
                state=state,
                zipcode=zipcode
            )
            address.persons.set(persons)  # Set the many-to-many relationship

            response_data = {'status': 'success'}
            return JsonResponse({'status': 'success'}, status=201)

        else:
            errors = form.errors.as_json()
            response_data = {'status': 'error', 'errors': errors}
            return JsonResponse(response_data, status=400)

    def get(self, request):
        form = CreateAddressForm()
        persons = Person.objects.filter(name__isnull=False).all()
        return render(request, 'myapp/address.html', {'form': form, 'persons': persons, 'msg': 'person added!'})


class RetrieveAddressView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, address_id):
        address = get_object_or_404(Address, pk=address_id)
        return render(request, 'myapp/address_detail.html', {'address': address})

    def post(self, request, address_id):
        return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)


class UpdateAddressView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, address_id):
        address = get_object_or_404(Address, pk=address_id)
        form = CreateAddressForm(instance=address)
        return render(request, 'myapp/address_update.html', {'form': form, 'address': address})

    def post(self, request, address_id):
        address = get_object_or_404(Address, pk=address_id)
        form = RegistrationForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/update_success.html')
        else:
            return render(request, 'myapp/address_update.html', {'form': form, 'address': address})


class DeleteAddressView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, address_id):
        address = get_object_or_404(Address, pk=address_id)
        address.delete()
        return JsonResponse({'status': 'success'})

    def delete(self, request, address_id):
        address = get_object_or_404(Address, pk=address_id)
        address.delete()
        return JsonResponse({'status': 'success'})

    def get(self, request, address_id):
        address = get_object_or_404(Address, pk=address_id)
        return render(request, 'myapp/addconfirm_delete.html', {'address': address})


class AllAddressView(View):
    def get(self, request):
        address = Address.objects.all()
        return render(request, 'myapp/all_address.html', {'address': address})


class PersonDetailView(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, person_id):
        person = get_object_or_404(Person, pk=person_id)
        address = person.address_set.first()  # Assuming OneToOneField or ForeignKey relationship
        return render(request, 'myapp/personfulldetail.html', {'person': person, 'address': address})

    def post(self, request, person_id):
        return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)


class CreateAccountView(View):
    """This class is used for create an account and also have many-to-many relation with persons"""

    def get(self, request):
        form = AccountForm()
        persons = Person.objects.filter(name__isnull=False).all()
        return render(request, 'myapp/account_form.html', {'form': form, 'persons': persons, 'msg': 'person added!'})

    def post(self, request):
        print("enter")
        form = AccountForm(request.POST)
        print("form",form)
        if form.is_valid():
            print("valid")
            account_type = form.cleaned_data['account_type']
            account_number = form.cleaned_data['account_number']
            balance = form.cleaned_data['balance']
            ifsc_code = form.cleaned_data['ifsc_code']
            branch = form.cleaned_data['branch']
            #persons = Person.objects.all()
            persons_ids = form.cleaned_data['persons']
            persons = Person.objects.filter(id__in=persons_ids)

            print("creating objevy")

            account = Account.objects.create(
                account_type=account_type,
                account_number=account_number,
                balance=balance,
                ifsc_code=ifsc_code,
                branch=branch

            )
            account.persons.set(persons)

            response_data = {'status': 'success'}
            return JsonResponse({'status': 'success'}, status=201)

        else:
            errors = form.errors.as_json()
            response_data = {'status': 'error', 'errors': errors}
            return JsonResponse(response_data, status=400)
