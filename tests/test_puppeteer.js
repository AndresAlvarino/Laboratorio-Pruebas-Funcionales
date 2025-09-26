const puppeteer = require("puppeteer");

async function loginExitoso() {
  const browser = await puppeteer.launch({ headless: "new" });
  const page = await browser.newPage();
  await page.goto("https://the-internet.herokuapp.com/login", { waitUntil: "domcontentloaded" });
  await page.type("#username", "tomsmith");
  await page.type("#password", "SuperSecretPassword!");
  await page.click("button.radius");
  await page.waitForSelector("#flash");
  const flash = await page.$eval("#flash", el => el.textContent);
  if (!flash.includes("You logged into a secure area!")) throw new Error("Login no exitoso");
  await page.screenshot({ path: "evidencias_pp_login.png" });
  await browser.close();
}

async function calculatorSuma() {
  const browser = await puppeteer.launch({ headless: "new" });
  const page = await browser.newPage();
  await page.goto("https://testsheepnz.github.io/BasicCalculator.html", { waitUntil: "domcontentloaded" });
  await page.type("#number1Field", "5");
  await page.type("#number2Field", "7");
  await page.select("#selectOperationDropdown", "0"); // "Add"
  await page.click("#calculateButton");
  const value = await page.$eval("#numberAnswerField", el => el.value);
  console.log("Resultado:", value);
  await browser.close();
}

(async () => {
  await loginExitoso();
  await calculatorSuma();
})();