from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from forum.models import Category, Post


@registry.register_document
class CategoryDocument(Document):
    posts = fields.NestedField(
        properties={
            'author_set': fields.NestedField(
                properties={
                    'car': fields.NestedField(
                        properties={
                            'brand': fields.StringField()
                        }
                    )
                }
            )
        }
    )

    class Index:
        name = 'categories'

    class Django:
        model = Category

    def get_instances_from_related(self, related_instance):
        """If related_models is set, define how to retrieve the Book instance(s) from the related model."""
        if isinstance(related_instance, Post):
            return related_instance.post_set.all()