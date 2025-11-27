from django import forms

class ContactForm(forms.Form):
    # フォームのフィールドをクラス変数として定義
    # CharField = 文字列
    # EmailField = メールアドレス用の文字列
    name = forms.CharField(label='ニックネーム')
    
    comment = forms.CharField(label='コメント', widget=forms.Textarea)
   
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # nameフィールドのplaceholderにメッセージを登録
        # フォームに表示される薄い文字
        
        self.fields['name'].widget.attrs['placeholder'] = 'ニックネームを入力'
        
        # nameフィールドを出力する<input>タグのclass属性を設定
        self.fields['name'].widget.attrs['class'] = 'form-control'

        
        # messageフィールドのplaceholderにメッセージを登録
        # フォームに表示される薄い文字
        self.fields['comment'].widget.attrs['placeholder'] = \
          'メッセージを入力してください'
        
        # messageフィールドを出力する<input>タグのclass属性を設定
        self.fields['comment'].widget.attrs['class'] = 'form-control'