# -*- coding: utf-8 -*-
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import collective.z3cform.captionedrelationfield


class CollectiveZ3CformCaptionedrelationfieldLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.z3cform.captionedrelationfield)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.z3cform.captionedrelationfield:default")


COLLECTIVE_Z3CFORM_CAPTIONEDRELATIONFIELD_FIXTURE = (
    CollectiveZ3CformCaptionedrelationfieldLayer()
)


COLLECTIVE_Z3CFORM_CAPTIONEDRELATIONFIELD_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_Z3CFORM_CAPTIONEDRELATIONFIELD_FIXTURE,),
    name="CollectiveZ3CformCaptionedrelationfieldLayer:IntegrationTesting",
)


COLLECTIVE_Z3CFORM_CAPTIONEDRELATIONFIELD_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_Z3CFORM_CAPTIONEDRELATIONFIELD_FIXTURE,),
    name="CollectiveZ3CformCaptionedrelationfieldLayer:FunctionalTesting",
)
