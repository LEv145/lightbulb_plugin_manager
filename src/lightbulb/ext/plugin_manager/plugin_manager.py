from __future__ import annotations

import typing
import copy
import inspect

import lightbulb
import hikari


if typing.TYPE_CHECKING:
    from hikari import UndefinedOr


class PluginManager():
    def __init__(
        self,
        name: str,
        description: str | None = None,
        include_datastore: bool = False,
        default_enabled_guilds: UndefinedOr[int | typing.Sequence[int]] = hikari.UNDEFINED,
        **kwargs: typing.Any,
    ):
        self._plugin = lightbulb.Plugin(
            name=name,
            description=description,
            include_datastore=include_datastore,
            default_enabled_guilds=default_enabled_guilds,
            **kwargs,
        )

    def load_commands(self, cls: typing.Any | None = None) -> None:
        if cls is None:
            cls = self

        command: lightbulb.CommandLike
        for name, command in inspect.getmembers(
            object=cls,
            predicate=lambda value: isinstance(value, lightbulb.CommandLike),
        ):
            self._plugin.command(command)

    def get_plugin(self) -> lightbulb.Plugin:
        return copy.copy(self._plugin)
