from django.urls import path
from .views import IndexView, RetrievePersonView, UpdatePersonView, DeletePersonView, AllPersonsView, SuccessPageView, \
    AddressView, RetrieveAddressView, UpdateAddressView, DeleteAddressView, AllAddressView, PersonDetailView, \
    HomePageView, CreateAccountView


urlpatterns = [
    path('reg/', IndexView.as_view(), name="index"),
    path('person-details/<int:person_id>/', RetrievePersonView.as_view(), name='retrieve_person'),
    path('update/<int:person_id>/', UpdatePersonView.as_view(), name='update_person'),
    path('delete/<int:person_id>/', DeletePersonView.as_view(), name='delete_person'),
    path('all_persons/', AllPersonsView.as_view(), name='all_persons'),
    path('success/', SuccessPageView.as_view(), name='success-page'),
    path('address/', AddressView.as_view(), name="address"),
    path('add/<int:address_id>/', RetrieveAddressView.as_view(), name='retrieve_address'),
    path('addupdate/<int:address_id>/', UpdateAddressView.as_view(), name='update_address'),
    path('adddelete/<int:address_id>/', DeleteAddressView.as_view(), name='delete_address'),
    path('all_address/', AllAddressView.as_view(), name='all_address'),
    path('person/<int:person_id>/', PersonDetailView.as_view(), name='person_full_detail'),
    path('homepage/', HomePageView.as_view(), name='homepage'),
    path('create_account/', CreateAccountView.as_view(), name='create_account'),
]
