from django.db import models

class Student(models.Model):
    COMMITTEE_CHOICES = [
        ("United Nations General Assembly- Social, Humanitarian and Cultural Committee (Third Committee)", "United Nations General Assembly- Social, Humanitarian and Cultural Committee (Third Committee)"), #1
        ("Assembly of the African Union", "Assembly of the African Union"), #2
        ("International Seabed Authority (Legal and Technical Commission)", "International Seabed Authority (Legal and Technical Commission)"), #3
        ("United Nations High-Level Advisory Body on Artificial Intelligence (Office of the Secretary-General's Envoy on Technology)", "United Nations High-Level Advisory Body on Artificial Intelligence (Office of the Secretary-General's Envoy on Technology)"), #4
        ("United Nations Security Council", "United Nations Security Council"), #5
        ("Meeting of Harvard Corporation and the Board of Overseers", "Meeting of Harvard Corporation and the Board of Overseers"), #6
        ("Executive Review Meeting of the Directorate-General of Civil Aviation. (Ministry of Civil Aviation, Government of India)", "Executive Review Meeting of the Directorate-General of Civil Aviation. (Ministry of Civil Aviation, Government of India)"), #7
        ("People’s Court of Athens, 399 BCE", "People’s Court of Athens, 399 BCE"), #8
        ("National Emergency Coordination Council", "National Emergency Coordination Council"), #9
        ("The Sovereignty Expropriation Directorate", "The Sovereignty Expropriation Directorate"), #10
        ("Executive Command of the Nasrid Emirate", "Executive Command of the Nasrid Emirate"), #11
        ("International Press - Journalism", "International Press - Journalism"), #12
        ("International Press - Photography", "International Press - Photography"), #13
        ("Ad-Hoc Committee of the Secretary-General", "Ad-Hoc Committee of the Secretary-General"), #14
    ]

    student_name = models.CharField(max_length=100,null=False)
    student_class = models.CharField(max_length=10,null=False)
    student_phone_number = models.CharField(max_length=10,null=False)
    student_email = models.EmailField(max_length=100,primary_key=True)
    student_password = models.CharField(max_length=45,null=False)
    mun_experience = models.CharField(max_length=10,null=False)
    committee_preference_1 = models.CharField(max_length=500, choices=COMMITTEE_CHOICES)
    committee_preference_2 = models.CharField(max_length=500, choices=COMMITTEE_CHOICES)
    is_head_delegate = models.BooleanField(default=False)
    incharge_name = models.CharField(max_length=100,null=False)
    incharge_phone_number = models.CharField(max_length=10,null=False)
    incharge_email = models.EmailField(max_length=100)
    def __str__(self):
        return self.student_name

class School(models.Model):

    school_name = models.CharField(max_length=100,null=False)
    school_class = models.CharField(max_length=10,null=False)
    school_designation = models.CharField(max_length=100,null=False)
    school_phone_number = models.CharField(max_length=10,null=False)
    school_email = models.CharField(max_length=100,primary_key=True)
    school_password = models.CharField(max_length=45,null=False)
    def __str__(self):
        return self.school_name