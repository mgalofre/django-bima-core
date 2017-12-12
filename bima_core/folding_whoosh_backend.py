from haystack.backends.whoosh_backend import WhooshEngine, WhooshSearchBackend
from whoosh.analysis import CharsetFilter, StemmingAnalyzer
from whoosh.support.charset import accent_map
from whoosh.fields import TEXT


class FoldingWhooshSearchBackend(WhooshSearchBackend):

    def build_schema(self, fields):
        schema = super(FoldingWhooshSearchBackend, self).build_schema(fields)

        for name, field in schema[1].items():
            if isinstance(field, TEXT):
                field.analyzer = StemmingAnalyzer() | CharsetFilter(accent_map)

        return schema


class FoldingWhooshEngine(WhooshEngine):
    backend = FoldingWhooshSearchBackend
