# Wagtail
from django.db import models
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


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

    content_panels = Page.content_panels + [
        FieldPanel("TLTR"),
        FieldPanel("body"),
        FieldPanel("tags"),
    ]

    class Meta:
        verbose_name = "Post Page"
        verbose_name_plural = "Post Pages"
