from django.shortcuts import render

from django.views.generic import TemplateView,ListView,CreateView

from .models import Quiz
 
import random
from django.db.models import Q
from time import sleep

class ron:
   def rondom(self):
         while True:
          num = random.randint(1,33)
          num2 = random.randint(1,33)
          if num == num2:
           continue
          else:
            break
         self.num = num
         self.num2 = num2
         return num,num2


      
          


   
# Create your views here.
class quizView(ListView,ron):
    
    template_name = 'quiz.html'
    context_object_name = 'object_list'
    
    
    def get_queryset(self):
       
       num,num2 = ron.rondom(self)
       self.request.session['num'] = num
       self.request.session['num2'] = num2

       
       return Quiz.objects.filter(Q(id =num) | Q(id = num2))
    

class KaisetuView(ListView):
    template_name = 'kaisetu.html'
    context_object_name = 'object_list'
    
    
    def get_queryset(self):
      
        num = self.request.session.get('num')
        num2 = self.request.session.get('num2')

       
        return Quiz.objects.filter(Q(id =num) | Q(id = num2))
    