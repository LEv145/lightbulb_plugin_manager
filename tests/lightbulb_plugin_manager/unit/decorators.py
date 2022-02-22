import unittest
from unittest.mock import AsyncMock, MagicMock


from src.lightbulb_plugin_manager.decorators import (
    pass_plugin,
)


class TestDecorators(unittest.IsolatedAsyncioTestCase):
    async def test_pass_plugin(self):
        # Test normal
        function_mock = AsyncMock()
        ctx_mock = MagicMock()

        function = pass_plugin(function_mock)
        await function(ctx_mock, "test_arg", test_kwarg="test_kwarg")

        function_mock.assert_awaited_once_with(
            ctx_mock.command.plugin,
            ctx_mock,
            "test_arg",
            test_kwarg="test_kwarg",
        )

        # Test `ctx.command` is None
        function_mock = AsyncMock()
        ctx_mock = MagicMock()
        ctx_mock.command = None

        function = pass_plugin(function_mock)
        with self.assertRaises(RuntimeError):
            await function(ctx_mock)

        # Test `ctx.command.plugin` is None
        function_mock = AsyncMock()
        ctx_mock = MagicMock()
        ctx_mock.command.plugin = None

        function = pass_plugin(function_mock)
        with self.assertRaises(RuntimeError):
            await function(ctx_mock)

