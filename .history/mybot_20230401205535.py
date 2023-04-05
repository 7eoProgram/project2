from highrise import BaseBot
from highrise.models import SessionMetadata, User

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        pass
    async def on_user_join(self, user: User) -> None:
        await self.highrise.chat(f"نورت الروم يا مز✨ {user.username}!")
    
        if message.startswith("السلام عليكم"):
            await self.highrise.chat("وعليكم السلام")
        if message.startswith("شلونك"):
            await self.highrise.chat("الحمد الله وانت ؟")
        if message.startswith("الحمد لله"):
            await self.highrise.chat("دوم")
        if message.startswith("بوت"):
            await self.highrise.chat("انت بوت😡")
        if message.startswith("تحبني"):
            await self.highrise.chat("يا قي")

