"""Setup tests for this package."""

from collective.z3cform.captionedrelationfield.testing import (
    COLLECTIVE_Z3CFORM_CAPTIONEDRELATIONFIELD_INTEGRATION_TESTING,
)
from plone import api
from plone.app.z3cform.widgets.contentbrowser import ContentBrowserWidget
from z3c.form.browser.object import ObjectWidget

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.z3cform.captionedrelationfield is properly installed."""

    layer = COLLECTIVE_Z3CFORM_CAPTIONEDRELATIONFIELD_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        self.demo_view = api.content.get_view(
            "captioned-relation-field-test-page", self.portal
        )

    def test_demo_form_null_submit(self):
        self.request.method = "POST"
        self.request.form.update(
            {
                "form.buttons.save": "Save",
            }
        )
        self.demo_view()

        self.assertDictEqual(
            self.request.get("saved_data"),
            {"regular_relation_field": None, "single": None},
        )

    def test_demo_form_single_captioned_relation(self):
        """Test that the single field of the form."""
        self.request.method = "POST"
        self.request.form.update(
            {
                "form.widgets.single.widgets.relation": self.portal.UID(),
                "form.widgets.single-empty-marker": "1",
                "form.widgets.single.widgets.caption": "Test caption",
                "form.buttons.save": "Save",
            }
        )

        self.demo_view()
        single_widget = self.demo_view.widgets["single"]
        self.assertIsInstance(single_widget, ObjectWidget)
        self.assertIsInstance(single_widget.widgets["relation"], ContentBrowserWidget)

        saved_data = self.request.get("saved_data")["single"]
        self.assertEqual(saved_data.relation.to_object, self.portal)
        self.assertEqual(saved_data.caption, "Test caption")
