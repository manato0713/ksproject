from django.shortcuts import render

# Create your views here.

from django.views.generic import DetailView,ListView
from django.views.generic.base import TemplateView
from .models import Buki,CustomUser
# FormViewにはフォーム処理を行うための機能が搭載されている
from django.views.generic import FormView

# django.urlsからreverse_lazyをインポート
# リダイレクト先のURLを設定するため
from django.urls import reverse_lazy

# formsモジュールからContactFormをインポート
# forms.pyからContactFormクラスをインポート
# forms.pyはP300~作成
from .forms import ContactForm

# django.contribからmesseagesをインポート
from django.contrib import messages

# django.core.mailモジュールからEmailMessageをインポート
from django.core.mail import EmailMessage

from django.db.models import Q

from time import sleep



class IndexView(ListView):
    
   
    template_name = 'index.html'
    context_object_name = 'object_list'
    def get_queryset(self):
       
        return Buki.objects.filter(category = 12)#filter = ()指定した項目のみ


    

class BukiView(ListView):
    template_name = 'all_buki.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        
       
        return Buki.objects.exclude(category = 12).order_by('category')#exclude = ()指定した項目を除く



class SyutaView(ListView):
    template_name = 'syuta.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        return Buki.objects.filter(Q(category=1) | Q(category=13))

class RoraView(ListView):
    template_name = 'rora.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        return Buki.objects.filter(Q(category = 2) | Q(category=14))

class TyazyaView(ListView):
    template_name = 'tyaz.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        return Buki.objects.filter(Q(category = 3) | Q(category=15))

class SuroView(ListView):
    template_name = 'suro.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        return Buki.objects.filter(Q(category = 4) | Q(category=16))


class BurasuView(ListView):
    template_name = 'bura.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        return Buki.objects.filter(Q(category = 5) | Q(category=17))

class HudeView(ListView):
    template_name = 'hude.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        return Buki.objects.filter(Q(category = 6) | Q(category=18))

class SupinView(ListView):
    template_name = 'supin.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        return Buki.objects.filter(Q(category = 7) | Q(category=19))

class ManyuView(ListView):
    template_name = 'manyu.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        return Buki.objects.filter(Q(category = 8) | Q(category=20))

class SyeruView(ListView):
    template_name = 'syeru.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        return Buki.objects.filter(Q(category = 9) | Q(category=21))

class WaipaView(ListView):
    template_name = 'waipa.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        return Buki.objects.filter(Q(category = 10) | Q(category=22))
    
class SutoriView(ListView):
    template_name = 'sutoro.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        return Buki.objects.filter(Q(category = 11) | Q(category=23))







class MainView(DetailView):
    
    
    #使用するテンプレートの名前
    template_name = 'main.html'
    model = Buki


    

    


class ContactView(FormView):
    # 使用するテンプレート
    template_name ='contact.html'

    # 使用するフォームクラス（forms.pyのContactForm）
    form_class = ContactForm

    # フォーム送信が成功した後のリダイレクト(reverse_lazy)先
    success_url = reverse_lazy('splapp:contact')

    # フォームから送信が行われたときに実行する関数
    def form_valid(self, form):
        count = self.request.session.get('contact_count', 0)#count = メッセージの送信回数を制限
      

       
        
        # 1.データの取得
        # フォームに入力されたデータをフィールド名を指定して取得
        # cleaned_data 正しく処理・整えられたデータ
        # clean が日本語できれいにするという意味
        name = form.cleaned_data['name']
        
        comment = form.cleaned_data['comment']

        
        from_email = 'utm2577215@stu.o-hara.ac.jp'

        # 送信するメールの作成
        message = EmailMessage( 
                                from_email=from_email,
                                to=['utm2577215@stu.o-hara.ac.jp'],  # ← リストで渡す
                                subject =name,
                                body= comment,
                                )
                                
        
        # メールサーバーからメールの送信
        

      # 送信完了後に表示するメッセージ
        if  count  > 2:

         messages.success(
            self.request,'送信回数が制限を超えました。1時間お待ちください')
         self.request.session.set_expiry(3600)
         return super().form_invalid(form)
         
       
        kaisu = 2 - count
        messages.success(
            self.request, f'お問い合わせは正常に送信されました。残り{kaisu}回')
        message.send()
        self.request.session['contact_count'] = count + 1#count = メッセージの送信回数を制限を+1
        

            
        return super().form_valid(form)
    

    
