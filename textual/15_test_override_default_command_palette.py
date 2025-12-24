from typing import Iterable
from textual.app import App, SystemCommand
from textual.command import CommandPalette
from textual.widgets import Input
from textual.screen import Screen


class PrefilledCommandPalette(CommandPalette):
    """Custom Command Palette with prefill support."""

    def __init__(self, *, prefill: str = "", **kwargs):
        super().__init__(**kwargs)
        self._prefill = prefill

    async def on_show(self) -> None:
        """
        เมื่อ Command Palette แสดงขึ้นมา จะทำการเติมข้อความที่กำหนดไว้ล่วงหน้า
        และตั้งค่า cursor ไปยังตำแหน่งสุดท้ายของข้อความนั้น
        """
        print('work in on_show: Setting prefill value')
        input_widget = self.query_one(Input)
        input_widget.value = self._prefill
        input_widget.cursor_position = len(self._prefill)


class BellCommandApp(App):
    """App ที่ override command palette ด้วย prefill."""

    # กำหนด BINDINGS เพื่อ override action_command_palette
    # ให้เรียก action_open_prefilled_palette แทน
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        # เดิม: ("ctrl+slash", "command_palette", "Command palette"),
        # เดิม: ("ctrl+p", "command_palette", "Command palette"),
        # เราจะ override action_command_palette โดยตรงในคลาส
        # ดังนั้นไม่จำเป็นต้องระบุใน BINDINGS นี้อีก
    ]

    # Override action_command_palette ของ Textual.App
    # เพื่อให้ Ctrl+P (ซึ่งผูกกับ action_command_palette)
    # ไปเรียก action_open_prefilled_palette แทน
    async def action_command_palette(self) -> None:
        """
        Override the default command palette action to open the prefilled one.
        """
        print('action_command_palette overridden: Calling action_open_prefilled_palette')
        await self.action_open_prefilled_palette()

    async def action_open_prefilled_palette(self) -> None:
        """
        Action ที่ใช้เปิด Command Palette พร้อมข้อความที่เติมไว้ล่วงหน้า
        """
        print('working open: Opening prefilled palette')
        await self.push_screen(PrefilledCommandPalette(prefill="Bell"))


    def get_system_commands(self, screen: Screen) -> Iterable[SystemCommand]:
        """
        Override เมธอดนี้เพื่อเพิ่มคำสั่งระบบที่กำหนดเอง
        และรวมคำสั่งระบบเดิมจากคลาสแม่
        """
        print('working get_system_commands: Fetching system commands')
        # เรียก generator ของคลาสแม่
        # ในกรณีนี้ get_system_commands ของ Textual.App เป็น generator ปกติ
        # จึงสามารถใช้ yield from ได้
        yield from super().get_system_commands(screen)

        # เพิ่ม SystemCommand ใหม่ ที่เรียก action แบบ custom
        # คำสั่งนี้จะปรากฏใน Command Palette เมื่อผู้ใช้กด Ctrl+/
        yield SystemCommand(
            "Open Bell Prefill",
            "Open CommandPalette with 'Bell' prefilled",
            self.action_open_prefilled_palette
        )

        # เพิ่มคำสั่ง Bell เข้าไปใน Command Palette
        yield SystemCommand("Bell", "Ring the console bell", self.bell)

    def bell(self) -> None:
        """
        เมธอดสำหรับส่งเสียง Bell ไปยัง console
        """
        print('Bell action triggered!')
        self.console.bell()


if __name__ == "__main__":
    app = BellCommandApp()
    app.run()