from django.forms import ModelForm
from .models import UserComments

class CommentForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのサブクラス
        
        Attributes:
         model :モデルのクラス
         fields:フォームで使用するモデルのフィールドを設定
        '''

        model = UserComments
        fields = ['title','comment']