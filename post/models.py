#Wagtail
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import RichTextField

class PostPage(Page):
    """Post Page"""
    
    template = 'post/post.html'

    TLTR = RichTextField(blank=True)
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("TLTR"),
        FieldPanel("body"),
    ]
    
    class Meta:
        verbose_name = "Post Page"
        verbose_name_plural = "Post Pages"
