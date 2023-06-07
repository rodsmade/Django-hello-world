from django.test import TestCase


class RootEndpointTests(TestCase):
    def test_root_endpoint_response_should_return_boilerplate_text(self):
        url = ""
        response = self.client.get(url)
        self.assertContains(response, "this path has no view just straight up returns a response")

    def test_path_with_views_endpoint_response_should_return_boilerplate_text(self):
        url = "/path-with-views"
        response = self.client.get(url)
        self.assertContains(response, "this path has a basic view")
