#Wagtail
from post.models import PostPage
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

    def get_context(self, request):
        context = super().get_context(request)

        # Get blog entries
        blog_entries= PostPage.objects.child_of(self).live()

        # Filter by tag
        tag = request.GET.get('tag')
        if tag:
            blog_entries = blog_entries.filter(tags__name=tag)

        context['blog_entries'] = blog_entries
        return context
