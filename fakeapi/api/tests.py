from django.test import TestCase
from django.test.client import RequestFactory


from fakeapi.api.views import add_instance


class AddInstanceTestCase(TestCase):
    def test_add_instance_should_returns_405_when_method_is_not_post(self):
        request = RequestFactory().get("/")
        response = add_instance(request)
        self.assertEqual(405, response.status_code)

        request = RequestFactory().put("/")
        response = add_instance(request)
        self.assertEqual(405, response.status_code)

        request = RequestFactory().delete("/")
        response = add_instance(request)
        self.assertEqual(405, response.status_code)
