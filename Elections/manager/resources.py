from import_export import resources
from counter.models import Vote

class VoteResource(resources.ModelResource):
    class Meta:
        model = Vote