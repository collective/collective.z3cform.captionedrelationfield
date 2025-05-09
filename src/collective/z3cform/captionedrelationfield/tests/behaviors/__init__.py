from collective.z3cform.captionedrelationfield import _
from collective.z3cform.captionedrelationfield._field import CaptionedRelationField
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from z3c.form.interfaces import IAddForm
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
    # FIXME: querying the catalog via @@getSource is not working on add forms
    # It works on edit forms.
    # This is something related to widget traversal, similar to the issue:
    #
    # - https://github.com/plone/plone.z3cform/pull/29
    directives.omitted(IAddForm, "multi")
