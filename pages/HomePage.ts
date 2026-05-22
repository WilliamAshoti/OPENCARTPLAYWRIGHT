import {Page, expect, Locator} from "@playwright/test";

export class HomePage{

    private readonly page: Page;
    //locators
    private readonly linkMyAccount: Locator;
    private readonly linkRegister: Locator;
    private readonly linkLogin: Locator;
    private readonly textSeachbox: Locator;
    private readonly buttonSearch: Locator;
    //constructor
    constructor(page: Page){
        this.page = page;
        this.linkMyAccount = page.locator('span:has-text("My Account")');
        this.linkRegister = page.locator("li[class='dropdown open'] li:nth-child(1) a:nth-child(1)");
        this.linkLogin = page.locator('span:has-text("Login")');
        this.textSeachbox = page.locator('input[placeholder="Search"]');
        this.buttonSearch = page.locator('#search button[type="button"]');
    }
    //action methods
    // Check if HomePage exists
    async isHomePageExist(){
        
        let title = await this.page.title();
        if(title){ // Check if the title is not empty
            return true;
        }
        return false;
        
    }

    // Click on My Account link
    async clickOnMyAccount(){
        try{
        await this.linkMyAccount.click();
        }
        catch(error){
            console.error("Error occurred while clicking on My Account link:", error);
            throw error;
        }
    }
    // Click on Register link
    async clickOnRegister(){
        try{
        await this.linkRegister.click();
        }
        catch(error){
            console.error("Error occurred while clicking on Register link:", error);
            throw error;
        }
    }
    // Click on Login link
    async clickOnLogin(){
        try{
        await this.linkLogin.click();
        }
        catch(error){
            console.error("Error occurred while clicking on Login link:", error);
            throw error;
        }
    }

        // Enter product name in the search box
    async enterProductName(pName: string){
        try {
            await this.textSeachbox.fill(pName);
        } catch (error) {
            console.log(`Exception occurred while entering product name: ${error}`);
            throw error;
        }
    }

        // Click the search button
    async clickSearch(){
        try {
            await this.buttonSearch.click();
        } catch (error) {
            console.log(`Exception occurred while clicking 'Search': ${error}`);
            throw error;
        }
    }
    // Search for a product
    async searchProduct(productName: string){
        try{
            await this.textSeachbox.fill(productName);
            await this.buttonSearch.click();
        }
        catch(error){
            console.error("Error occurred while searching for product:", error);
            throw error;
        }
    } // Get the search results and return the count of products found
    async getSearchResultsCount(){
        try{
            const searchResults = this.page.locator('.product-layout');
            return await searchResults.count();
        }
        catch(error){
            console.error("Error occurred while getting search results count:", error);
            throw error;
        }
    }
    }   