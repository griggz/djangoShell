from .models import Post
from django.forms import ModelForm, HiddenInput
from django.core.validators import ValidationError


class PostForm(ModelForm):
    class Meta:
        model = Post
        widgets = {'unsplash_url': HiddenInput()}
        fields = ['user', 'title', 'content', 'post_image', 'width_field',
                  'height_field', 'unsplash_url', 'draft',
                  'publish', 'read_time']
        # exclude = ('field1',)
        labels = {'user': 'Author', 'title': 'Title', 'slug': 'Slug',
                  'content': 'Content', 'post_image': 'Post Image',
                  'height_field': 'Image Height', 'width_field': 'Image Width',
                  'draft': "Draft", 'publish': 'Publish Date'}
        help_texts = {
            'post_image': 'Get your photo ID from <a href="https://unsplash.com" '
                          'target="_blank">Unsplash.com</a>. Use this '
                          '<a href="http://quick.as/x3vycpgog" target="_blank">'
                          'guide</a> if you need help. Or, if you want a random '
                          'image, copy/paste this url "https://source.unsplash.com/random" '
                          'to pull random images from unsplash.',
            'draft': 'Is this post a draft? (Any post marked as "draft" will '
                     'not be displayed to unauthorized users)',
            'publish': 'When would you like this post published? (Any post '
                       'marked with a date in the future will not be displayed '
                       'to public users until the future date arrives.)'
            }

    def clean_unsplash_url(self):
        post_image = self.cleaned_data.get("post_image")
        image_height = self.cleaned_data.get("height_field")
        image_width = self.cleaned_data.get('width_field')

        if not post_image:
            raise ValidationError('Error')
        else:
            unsplash_api = str("https://source.unsplash.com")
            unsplash_image_id = str(post_image)
            image_size = str(image_width), str(image_height)
            join_size = 'x'.join(image_size)
            join_fields = unsplash_api, unsplash_image_id, join_size
            compile_url = '/'.join(join_fields)

        return compile_url
