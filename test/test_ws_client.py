import unittest

from lighter.ws_client import WsClient


class TestWsClient(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.client = WsClient(order_book_ids=[0])

    def test_sync_ignores_json_string_message(self):
        self.client.on_message(None, '"heartbeat"')

    async def test_async_ignores_json_string_message(self):
        await self.client.on_message_async(None, '"heartbeat"')

    async def test_async_ignores_decoded_non_object_message(self):
        await self.client.on_message_async(None, ["heartbeat"])


if __name__ == "__main__":
    unittest.main()
