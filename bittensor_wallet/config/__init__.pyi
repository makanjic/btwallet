from typing import Optional

class Config:
    def __init__(
            self,
            name: Optional[str] = None,
            hotkey: Optional[str] = None,
            path: Optional[str] = None,
    ) -> None: ...

    def __str__(self) -> str: ...

    @property
    def name(self) -> str: ...

    @property
    def path(self) -> str: ...

    @property
    def hotkey(self) -> str: ...