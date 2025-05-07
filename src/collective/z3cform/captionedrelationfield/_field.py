from collective.z3cform.captionedrelationfield import _
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widgets.contentbrowser import ContentBrowserFieldWidget
from plone.autoform import directives
from z3c.form.object import registerFactoryAdapter
from z3c.relationfield.schema import RelationChoice
from zope import schema
from zope.interface import implementer
from zope.interface import Interface
from zope.schema.interfaces import IObject


class ICaptionedRelationValue(Interface):

    relation = RelationChoice(
        title=_("Related content"),
        source=CatalogSource(),
        required=False,
    )
    directives.widget(
        "relation",
        ContentBrowserFieldWidget,
        vocabulary="plone.app.vocabularies.Catalog",
        pattern_options={"recentlyUsed": True},
    )

    caption = schema.TextLine(
        title=_("Image caption"),
        description=_("Caption for the related image."),
        required=False,
    )


@implementer(ICaptionedRelationValue)
class CaptionedRelationValue:
    """A relation object that can have a caption."""

    def __init__(self, relation=None, caption=None):
        self.relation = relation
        self.caption = caption


registerFactoryAdapter(ICaptionedRelationValue, CaptionedRelationValue)


class ICaptionedRelationField(IObject):
    """A field that stores a relation and an optional caption."""


@implementer(ICaptionedRelationField)
class CaptionedRelationField(schema.Object):

    def __init__(self, **kwargs):

        if "schema" not in kwargs:
            kwargs["schema"] = ICaptionedRelationValue
        super().__init__(**kwargs)
