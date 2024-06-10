#Wagtail
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import RichTextField

class BlogPage(Page):
    """Home Page"""
    
    template = 'blog/blog.html'

    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
    ]
    
    class Meta:
        verbose_name = "Blog Page"
        verbose_name_plural = "Blog Pages"
