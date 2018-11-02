from django import forms
import pandas as pd
import random, os
from rpy2.robjects.packages import importr
from rpy2.robjects import r

CHOICES = (
    ('','-----'),
    ('0','00:00'),
    ('1','01:00'),
    ('2','02:00'),
    ('3','03:00'),
    ('4','04:00'),
    ('5','05:00'),
    ('6','06:00'),
    ('7','07:00'),
    ('8','08:00'),
    ('9','09:00'),
    ('10','10:00'),
    ('11','11:00'),
    ('12','12:00'),
    ('13','13:00'),
    ('14','14:00'),
    ('15','15:00'),
    ('16','16:00'),
    ('17','17:00'),
    ('18','18:00'),
    ('19','19:00'),
    ('20','20:00'),
    ('21','21:00'),
    ('22','22:00'),
    ('23','23:00'),
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

    def prepare_plotting_data(self):
        r.load("~/Documents/django-rsas/wearables/.RData")
        wearableProc = importr("wearableProc", lib_loc="~/Documents/django-rsas/wearables/R/x86_64-pc-linux-gnu-library/3.4")
        make_plots = wearableProc.r['prepare_interval_activity_data(self.start_interval,self.end_interval,self.time_split)']
