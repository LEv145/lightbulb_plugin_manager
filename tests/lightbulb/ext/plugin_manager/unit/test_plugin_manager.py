import unittest
from unittest.mock import MagicMock

import lightbulb

from src.lightbulb.ext.plugin_manager.plugin_manager import PluginManager


class TestPluginManager(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self._plugin_manager = PluginManager(
            name="Test name",
            description="Test description",
            include_datastore=True,
            default_enabled_guilds=(1, 2),
        )

    def test_load_commands(self):
        # Test with class
        command_like_mock = MagicMock(spec=lightbulb.CommandLike)
        self._plugin_manager.load_commands(
            type(
                "TestComponent",
                (),
                {
                    "command_like": command_like_mock,
                }
            )
        )
        self.assertIn(command_like_mock, self._plugin_manager._plugin.raw_commands)

        # Test with self
        command_like_mock = MagicMock(spec=lightbulb.CommandLike)
        test_plugin_manager = type(
            "TestComponent",
            (PluginManager,),
            {
                "command_like": command_like_mock,
            }
        )(name="Test name", description="Test description")
        test_plugin_manager.load_commands()

        self.assertIn(command_like_mock, test_plugin_manager._plugin.raw_commands)

    def test_get_plugin(self):
        # Test normal
        manager_plugin = self._plugin_manager._plugin
        resulting_plugin = self._plugin_manager.get_plugin()

        self.assertIsNot(manager_plugin, resulting_plugin)

        self.assertEqual(manager_plugin.name, resulting_plugin.name)
        self.assertEqual(
            manager_plugin.description,
            resulting_plugin.description,
        )
        self.assertEqual(
            manager_plugin.default_enabled_guilds,
            resulting_plugin.default_enabled_guilds,
        )
