from collective.z3cform.captionedrelationfield import _
from collective.z3cform.captionedrelationfield._field import CaptionedRelationField
from plone import api
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.z3cform.widgets.contentbrowser import ContentBrowserFieldWidget
from plone.autoform import directives
from plone.autoform.form import AutoExtensibleForm
from plone.supermodel import model
from z3c.form import form
from z3c.form.form import EditForm
from z3c.relationfield.schema import RelationChoice


class ITestSchema(model.Schema):
    """Test schema for the form."""

    regular_relation_field = RelationChoice(
        title=_("Regular captioned relation field"),
        source=CatalogSource(),
        required=False,
    )
    directives.widget(
        "regular_relation_field",
        ContentBrowserFieldWidget,
        vocabulary="plone.app.vocabularies.Catalog",
        pattern_options={"recentlyUsed": True},
    )
    single = CaptionedRelationField(
        title=_("Single"),
        description=_("Single captioned relation field"),
        required=False,
    )


# FIXME: querying the catalog via @@getSource is not working when you have this
# field in a list field in a standalone form.
# It works on edit forms.
# This is something related to widget traversal, similar to the issue:
#
# - https://github.com/plone/plone.z3cform/pull/30
#
#    multi = schema.List(
#        title=_("Multi"),
#        description=_("Multi captioned relation field"),
#        value_type=CaptionedRelationField(
#            title=_("Multi captioned relation field"),
#            description=_("Multi captioned relation field"),
#            required=False,
#        ),
#        required=False,
#    )


class TestFormView(AutoExtensibleForm, EditForm):
    """Test form for the captioned relation field."""

    schema = ITestSchema
    ignoreContext = True
    label = _("Test Form")
    description = _("Test form for the captioned relation field.")

    @form.button.buttonAndHandler(_("Save"), name="save")
    def handle_save(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return

        self.request.set("saved_data", data)
        api.portal.show_message(_("Form saved successfully"))
        self.request.response.redirect(
            f"{self.context.absolute_url()}/@@{self.__name__}"
        )

    @form.button.buttonAndHandler(_("Cancel"), name="cancel")
    def handle_cancel(self, action):
        """Cancel button"""
        api.portal.show_message(_("Action canceled"))
        self.request.response.redirect(
            f"{self.context.absolute_url()}/component-library-canceled"
        )
