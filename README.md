# Lightbulb plugin manager  (Plugin object-oriented ext)


## How to use
```
... \
    __main__.py
    components \ 
        music_component.py
```

`misc_component.py:`
```py
import lightbulb
from lightbulb_plugin_manager import PluginManager, pass_plugin


@dataclass
class MusicPluginDataStore(lightbulb.utils.DataStore):
    music_client: ABCMusicClient


class PluginType(lightbulb.Plugin):
    d: PluginDataStoreType


class MusicPluginManager(PluginManager):
    def __init__(self, name: str, data_store: MusicPluginDataStore) -> None:
        super().__init__(name=name)
        
        self._plugin._d = data_store
        self.load_commands(self)

    @staticmethod
    @lightbulb.command(name="play", description="Play music!")
    @lightbulb.implements(lightbulb.SlashCommand)
    @pass_plugin
    async def play_command(plugin: PluginType, ctx: lightbulb.Context) -> None:
        plugin.music_client.play(...)
        await ctx.respond("Playing")
```

`__main__.py:`
```py
from components.music_component import MusicPluginManager, MusicPluginDataStore


def main() -> None:
    ...
    bot.add_plugin(
        MiscPluginManager(
            "Music", 
            "Music commands!", 
            data_store=MusicPluginDataStore(
                music_client=LavalinkClient(...),
            ),  # Dependency Injection
        ).get_plugin(),
    )
    ...


if __name__ == "__main__":
    main()
```
And now we provide complete independence of the client from the component!

## What are the advantages? OwO

* We have completely independent entities
* Inheritance
Gives you the opportunity to inherit from the component and make the command in your own way!
```py
class MyPluginManager(MyFriendPluginManager):
    @staticmethod
    @lightbulb.command(name="stop", description="Stop music")
    @lightbulb.implements(lightbulb.SlashCommand)
    def stop_command(...): ...
```
* The ability to make abstraction over components
* And More!

## Links
* https://martinfowler.com/articles/injection.html
