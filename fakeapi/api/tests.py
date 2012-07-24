from django.test import TestCase
from django.test.client import RequestFactory


from fakeapi.api.views import add_instance, remove_instance, bind, unbind, status


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

    def test_add_instance(self):
        request = RequestFactory().post("/", {"name": "plains_of_dawn"})
        response = add_instance(request)
        self.assertEqual(201, response.status_code)


class RemoveInstanceTestCase(TestCase):
    def test_remove_instance_should_returns_405_when_method_is_not_delete(self):
        request = RequestFactory().get("/")
        response = remove_instance(request, "somename")
        self.assertEqual(405, response.status_code)

        request = RequestFactory().put("/")
        response = remove_instance(request, "somename")
        self.assertEqual(405, response.status_code)

        request = RequestFactory().post("/")
        response = remove_instance(request, "somename")
        self.assertEqual(405, response.status_code)

    def test_remove_instance(self):
        request = RequestFactory().delete("/")
        response = remove_instance(request, "somename")
        self.assertEqual(200, response.status_code)


class BindTestCase(TestCase):
    def test_bind_should_returns_405_when_method_is_not_post(self):
        request = RequestFactory().get("/")
        response = bind(request, "somename")
        self.assertEqual(405, response.status_code)

        request = RequestFactory().put("/")
        response = bind(request, "somename")
        self.assertEqual(405, response.status_code)

        request = RequestFactory().delete("/")
        response = bind(request, "somename")
        self.assertEqual(405, response.status_code)

    def test_bind(self):
        request = RequestFactory().post("/", {})
        response = bind(request, "somename")
        self.assertEqual(201, response.status_code)


class UnBindTestCase(TestCase):
    def test_unbind_should_returns_405_when_method_is_not_delete(self):
        request = RequestFactory().get("/")
        response = unbind(request, "somename", "host")
        self.assertEqual(405, response.status_code)

        request = RequestFactory().put("/")
        response = unbind(request, "somename", "host")
        self.assertEqual(405, response.status_code)

        request = RequestFactory().post("/")
        response = unbind(request, "somename", "host")
        self.assertEqual(405, response.status_code)

    def test_unbind(self):
        request = RequestFactory().delete("/")
        response = unbind(request, "somename", "host")
        self.assertEqual(200, response.status_code)


class StatusTestCase(TestCase):
    def test_status_should_returns_405_when_method_is_not_get(self):
        request = RequestFactory().delete("/")
        response = status(request, "somename")
        self.assertEqual(405, response.status_code)

        request = RequestFactory().put("/")
        response = status(request, "somename")
        self.assertEqual(405, response.status_code)

        request = RequestFactory().post("/")
        response = status(request, "somename")
        self.assertEqual(405, response.status_code)
