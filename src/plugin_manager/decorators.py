from __future__ import annotations

from typing import (
    Callable,
    Awaitable,
    Any,
)
from mypy_extensions import Arg, VarArg, KwArg

import lightbulb


def pass_plugin(
    function: Callable[[Arg(lightbulb.Context), VarArg(), KwArg()], Awaitable[None]],
) -> Callable[[lightbulb.Context], Awaitable[None]]:
    async def decorated(ctx: lightbulb.Context, *args: Any, **kwargs: Any) -> None:
        if ctx.command is None:
            raise RuntimeError("The command was not found with context")
        if ctx.command.plugin is None:
            raise RuntimeError("The plugin was not found with command")

        await function(ctx.command.plugin, ctx, *args, **kwargs)

    return decorated
