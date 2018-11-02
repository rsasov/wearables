from django import forms
import pandas as pd
import random, os

CHOICES = (
    ('00:00','00:00'),
    ('01:00','01:00'),
    ('02:00','02:00'),
    ('03:00','03:00'),
    ('04:00','04:00'),
    ('05:00','05:00'),
    ('06:00','06:00'),
    ('07:00','07:00'),
    ('08:00','08:00'),
    ('09:00','09:00'),
    ('10:00','10:00'),
    ('11:00','11:00'),
    ('12:00','12:00'),
    ('13:00','13:00'),
    ('14:00','14:00'),
    ('15:00','15:00'),
    ('16:00','16:00'),
    ('17:00','17:00'),
    ('18:00','18:00'),
    ('19:00','19:00'),
    ('20:00','20:00'),
    ('21:00','21:00'),
    ('22:00','22:00'),
    ('23:00','23:00'),
    )
SPLITS = (
    (1,'10 мин.'),
    (2,'15 мин.'),
    (3,'30 мин.'),
    (4,'1 час'),
    )

class ActivityPeriodForm(forms.Form):
    start_interval = forms.ChoiceField(choices = CHOICES, widget=forms.Select(), required = True)
    end_interval = forms.ChoiceField(choices = CHOICES, widget=forms.Select(), required = True)
    time_split = forms.ChoiceField(choices = SPLITS, widget=forms.RadioSelect(), required = True)
