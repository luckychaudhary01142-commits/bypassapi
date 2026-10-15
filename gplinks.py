import asyncio
from .base import BasePlugin

class GPLinks(BasePlugin):
    name = "gplinks"
    domains = [
        "gplinks", "gplink.in", "gplinks.co", "shareus",
        "shrinkme.io", "shrinkearn.com", "clk.sh",
        "za.gl", "za.uy", "za.gl", "mdiskshort",
        "clk.wiki", "urlsopen.com",
    ]

    async def bypass(self, url, page):
        await page.goto(url, wait_until="domcontentloaded", timeout=45000)
        await asyncio.sleep(4)

        for sel in [
            "#btn-main", "button#btn-main", "a#btn-main",
            "button:has-text('Continue')", "button:has-text('Go to Link')",
        ]:
            try:
                btn = await page.query_selector(sel)
                if btn:
                    await btn.click()
                    await page.wait_for_load_state("networkidle", timeout=20000)
                    await asyncio.sleep(2)
                    break
            except Exception:
                continue

        return page.url
