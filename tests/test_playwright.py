import asyncio
from playwright.async_api import async_playwright

async def login_exitoso():
    async with async_playwright() as p:
        b = await p.chromium.launch(headless=True)
        ctx = await b.new_context(viewport={"width":1280,"height":800})
        page = await ctx.new_page()
        await page.goto("https://the-internet.herokuapp.com/login")
        await page.fill("#username", "tomsmith")
        await page.fill("#password", "SuperSecretPassword!")
        await page.click("button.radius")
        flash = await page.text_content("#flash")
        assert "You logged into a secure area!" in flash
        await page.screenshot(path="evidencias_pw_login.png")
        await b.close()

async def calculator_suma():
    async with async_playwright() as p:
        b = await p.chromium.launch(headless=True)
        page = await b.new_page()
        await page.goto("https://testsheepnz.github.io/BasicCalculator.html")
        await page.fill("#number1Field", "5")
        await page.fill("#number2Field", "7")
        await page.select_option("#selectOperationDropdown", label="Add")
        await page.click("#calculateButton")
        value = await page.get_attribute("#numberAnswerField","value")
        print("Resultado:", value)
        await b.close()

if __name__ == "__main__":
    asyncio.run(login_exitoso())
    asyncio.run(calculator_suma())
