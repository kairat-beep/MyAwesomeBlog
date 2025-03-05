# Wagtail
from django.db import models
from django.utils import timezone
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.search import index
from django.db.models import F


class PageTag(TaggedItemBase):
    content_object = ParentalKey(
        "post.PostPage", on_delete=models.CASCADE, related_name="tagged_items"
    )


class PostPage(Page):
    """Post Page"""

    template = "post/post.html"

    TLTR = RichTextField(blank=True)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=PageTag, blank=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    view_count = models.PositiveBigIntegerField(default=0, db_index=True)

    content_panels = Page.content_panels + [
        FieldPanel("TLTR"),
        FieldPanel("body"),
        FieldPanel("tags"),
        FieldPanel("date"),
    ]

    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField("body"),
        index.FilterField("date"),
    ]

    class Meta:
        verbose_name = "Post Page"
        verbose_name_plural = "Post Pages"

    def serve(self, request):
        # Increment the visit count
        PostPage.objects.filter(pk=self.pk).update(view_count=F("view_count") + 1)
        return super().serve(request)
