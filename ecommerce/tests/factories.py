import factory
from django.contrib.sites.models import Site
from factory.fuzzy import FuzzyText     # pylint: disable=ungrouped-imports
from oscar.core.loading import get_model
from oscar.test.factories import StockRecordFactory as OscarStockRecordFactory
from oscar.test.factories import ProductFactory

from ecommerce.core.models import SiteConfiguration


class PartnerFactory(factory.DjangoModelFactory):
    class Meta(object):
        model = get_model('partner', 'Partner')
        django_get_or_create = ('name',)

    name = FuzzyText(prefix='test-partner-')
    short_code = FuzzyText(length=8)


class SiteFactory(factory.DjangoModelFactory):
    class Meta(object):
        model = Site

    domain = FuzzyText(suffix='.fake')
    name = FuzzyText()


class SiteConfigurationFactory(factory.DjangoModelFactory):
    class Meta(object):
        model = SiteConfiguration

    lms_url_root = factory.LazyAttribute(lambda obj: "http://lms.testserver.fake")
    site = factory.SubFactory(SiteFactory)
    partner = factory.SubFactory(PartnerFactory)
    send_refund_notifications = False
    enable_sdn_check = False


class StockRecordFactory(OscarStockRecordFactory):
    product = factory.SubFactory(ProductFactory)
    price_currency = 'USD'
