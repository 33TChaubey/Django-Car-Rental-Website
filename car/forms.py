from django import forms
from .models import Car, Order, PrivateMsg, Features


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_name', 'company_name', 'num_of_seats', 'num_of_air_bag', 'fuel_type', 'mileage',
                  'transmission', 'image', 'location', 'const_per_hour', 'cost_par_day', 'cost_of_leasing', 'description', 'is_avaliable', 'like']

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class FeaturesForm(forms.ModelForm):
    class Meta:
        model = Features
        fields = ["airconditions", "child_seat", "gps", "luggage", "music",
                  "seat_belt",
                  "sleeping_bed",
                  "water",
                  "bluetooth",
                  "onboard_computer",
                  "audio_input",
                  "long_term_trips",
                  "car_Kit",
                  "remote_central_locking",
                  "climate_control"]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['cell_no', 'address', 'date', 'to']
        widgets = {
            'date' : forms.DateInput(attrs={"class" : "" , "type": "datetime-local"}) , 
            'to' : forms.DateInput(attrs={"class" : "" , "type": "datetime-local"}) , 
            }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
        


class MessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMsg
        fields = [
            "name",
            "email",
            "message",
        ]

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
