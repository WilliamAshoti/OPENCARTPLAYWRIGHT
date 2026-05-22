
import { test, expect } from '@playwright/test';
import { DataProvider } from '../utils/dataProvider';
import { RegistrationPage } from '../pages/registrationPage';
import { HomePage } from '../pages/HomePage';
import { TestConfig } from '../test.config';
import { RandomDataUtils } from '../utils/randomDataGenerator';



/**
 * Test case Account Registration
 * Tags: @sanity, @master, @regression
 * Steps:
 * 1. Navigate to the registration page
 * 2. Go to My Account and click on Register
 * 3. Fill in the registration form with valid data
 * 4. Agree to the terms and conditions and click on Register
 * 5. Verify that the account is created successfully and the user is redirected to the account dashboard
 * 
*/

// test.describe('Account Registration', () => {
//     let registrationPage: RegistrationPage;
//     let homePage: HomePage;
//     let DataProvider: DataProvider;
//     let testConfig: TestConfig;
//     let randomDataGenerator = new RandomDataUtils();



// });
let registrationPage: RegistrationPage;
let homePage: HomePage;
let config: TestConfig;

test.beforeEach(async ({ page }) => {
    config = new TestConfig();
    homePage = new HomePage(page);
    registrationPage = new RegistrationPage(page);
    await page.goto(config.appUrl) // Navigate to the application URL
});

test('Should register a new account successfully', async ({ page }) => {




    await homePage.clickOnMyAccount();
    await homePage.clickOnRegister();


    // Generate random data for registration
    await registrationPage.setFirstName(RandomDataUtils.getFirstName());
    await page.waitForTimeout(1000);
    registrationPage.setLastName(RandomDataUtils.getLastName());
    await page.waitForTimeout(1000);
    await registrationPage.setEmail(RandomDataUtils.getEmail());
    await page.waitForTimeout(1000);
    await registrationPage.setTelephone(RandomDataUtils.getPhoneNumber());

    const password = RandomDataUtils.getPassword();
    registrationPage.setPassword(password);
    await page.waitForTimeout(2000);
    registrationPage.setConfirmPassword(password);
    await page.waitForTimeout(2000);
    registrationPage.setPrivacyPolicy();
    await page.waitForTimeout(2000);
    await registrationPage.clickContinue();
    const confirmationMsg = await registrationPage.getConfirmationMsg();
    expect(confirmationMsg).toContain("Account Has Been Created!");

    await page.waitForTimeout(3000); // Wait for 3 seconds to observe the result before closing the browser
});