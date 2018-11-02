from django import forms
import pandas as pd
import random, os

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
        base_data_dir = "~/Documents/BasisProc/"
        if int(filter(str.isdigit, ActivityPeriodForm.time_split)) == 1:
            split = "1hour"
        else :
            split = filter(str.isdigit,ActivityPeriodForm.time_split) + "min"
        professor_dir = os.listdir(base_data_dir + "Professor/" + split)
        files_num = len(professor_dir)
        file_to_plot = professor_dir[random.randint(1,len(professor_dir)+1)]
        data = pd.read_csv(file_to_plot)
