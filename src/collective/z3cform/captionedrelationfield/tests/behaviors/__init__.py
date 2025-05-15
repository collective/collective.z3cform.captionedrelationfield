from collective.z3cform.captionedrelationfield import _
from collective.z3cform.captionedrelationfield._field import CaptionedRelationField
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class ICaptionRelationBehavior(model.Schema):
    """Behavior for captioned relation field."""

    single = CaptionedRelationField(
        title=_("Single"),
        description=_("Single captioned relation field"),
        required=False,
    )

    multi = schema.List(
        title=_("Multi"),
        description=_("Multi captioned relation field"),
        value_type=CaptionedRelationField(
            title=_("Multi captioned relation field"),
            description=_("Multi captioned relation field"),
            required=False,
        ),
    )
