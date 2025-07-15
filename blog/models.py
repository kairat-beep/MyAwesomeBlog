# Wagtail
from django.core.cache import cache
from django.core.paginator import Paginator
from django.http import Http404
from taggit.models import Tag
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page

from post.models import PostPage


class BlogPage(Page):
    """Home Page"""

    template = "blog/blog.html"

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
        # Filter by tag
        all_tags = cache.get("all_tags")
        all_tags_names = cache.get("all_tags_names")
        if all_tags is None:
            all_tags = list(Tag.objects.all())
            all_tags_names = set([_.name for _ in all_tags])
            cache.set("all_tags", all_tags, timeout=120)
            cache.set("all_tags_names", all_tags_names, timeout=120)

        tag = request.GET.get("tag")
        if tag not in all_tags_names and tag is not None:
            raise Http404("Not found. Check back later.")

        # Get blog entries
        blog_entries = PostPage.objects.child_of(self).order_by("-date").live()
        if tag:
            blog_entries = blog_entries.filter(tags__name=tag)
        paginator = Paginator(blog_entries, per_page=15)

        context["page"] = paginator.get_page(request.GET.get("page"))
        context["tags"] = all_tags
        context["tag"] = tag
        return context
