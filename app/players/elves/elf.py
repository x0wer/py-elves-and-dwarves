from abc import ABC
from app.players.player import Player


class Elf(Player, ABC):
    def __init__(self, nickname: str, musical_instrument: str) -> str:
        super().__init__(nickname=nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> str:
        print(f"{self.nickname} is playing a song "
              f"on the {self._musical_instrument}")

