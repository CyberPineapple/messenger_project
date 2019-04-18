from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp import web


class MessengerTestCase(AioHTTPTestCase):

    @unittest_run_loop
    async def test_connection(self):
        responce = await self.client.request("GET", "/")
        assert responce.status == 200
        text = await responce.text()
        assert "You in root page" in text



test = MessengerTestCase()
test.test_connection()
