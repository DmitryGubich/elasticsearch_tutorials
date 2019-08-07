from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from forum.models import Post


@registry.register_document
class PostDocument(Document):
    title = fields.TextField()
    content = fields.TextField()
    timestamp = fields.DateField()
    category = fields.NestedField(
        properties={
            'name': fields.TextField(),
            'slug': fields.TextField()
        }
    )

    class Index:
        name = 'posts'

    class Django:
        model = Post
