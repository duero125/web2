from django import forms
from tinymce import TinyMCE
from .models import Post, Comment


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'overview', 'content', 'thumbnail', 
        'categories', 'featured', 'previous_post', 'next_post')


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'u-border-1 u-border-grey-30 u-input u-input-round',
        'placeholder': 'Type your comment',
        'id': 'message-59b1',
        'rows': '4',
        'cols': '50',
        'name' : 'message',
        'required' : '',
        'maxlength': '500'    
    }))
    class Meta:
        model = Comment
        fields = ('content', )