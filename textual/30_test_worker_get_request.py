from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Container
import aiohttp
import asyncio


# ---- ฟังก์ชันดึงข้อมูล Binance ----
async def get_request(session, url):
    try:
        async with session.get(url, timeout=5) as resp:
            if resp.status != 200:
                return {"error": f"HTTP {resp.status}"}
            try:
                data = await resp.json()
            except Exception as e:
                return {"error": f"Invalid JSON: {e}"}
            # Binance error format: {"code":-1121,"msg":"Invalid symbol."}
            if "code" in data and "msg" in data:
                return {"error": data.get("msg")}
            return {"ok": data}
    except asyncio.TimeoutError:
        return {"error": "Timeout"}
    except aiohttp.ClientError as e:
        return {"error": f"ClientError: {e}"}
    except Exception as e:
        return {"error": f"Unexpected: {type(e).__name__}: {e}"}


async def get_binance_data():
    """Worker Task: ดึงข้อมูลราคา และ log ออก console"""
    try:
        async with aiohttp.ClientSession() as session:
            url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
            result = await get_request(session,url)
            print("📡 Binance Result:", result)
    except asyncio.CancelledError:
        # ทำ cleanup ถ้าถูก cancel
        print("⚠️ Worker was cancelled")
        raise


# ---- Textual App ----
class BinanceApp(App):

    CSS = """
    Container {
        align: center middle;
    }
    Static {
        border: solid green;
        padding: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Container(
            Static("Binance Price Fetcher Running...")
        )

    async def interval_loop(self):
        """Worker ยิง request ทุก interval โดยไม่ต้อง cancel เอง"""
        worker = self.run_worker(
            get_binance_data(),
            name="price_fetcher",
            exit_on_error=False,
            exclusive=True  # ✅ ยกเลิก worker เก่าอัตโนมัติ
        )
        print(worker.state)
        print('after interval_loop working')
           

    async def on_mount(self):
        # เริ่ม interval controller
        #interval_controller_worker = self.run_worker(self.interval_loop(10), name="interval_controller")
        self.set_interval(interval=5,callback=self.interval_loop)

if __name__ == "__main__":
    BinanceApp().run()
