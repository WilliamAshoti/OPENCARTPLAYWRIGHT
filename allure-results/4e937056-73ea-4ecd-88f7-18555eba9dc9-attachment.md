# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: AccountRegistration.spec.ts >> Should register a new account successfully
- Location: tests\AccountRegistration.spec.ts:34:9

# Error details

```
Test timeout of 30000ms exceeded.
```

```
Error: locator.click: Test timeout of 30000ms exceeded.
Call log:
  - waiting for locator('span:has-text("Register")')

```

# Page snapshot

```yaml
- generic [ref=e1]:
  - navigation [ref=e2]:
    - generic [ref=e3]:
      - button "$ Currency " [ref=e7] [cursor=pointer]:
        - strong [ref=e8]: $
        - text: Currency
        - generic [ref=e9]: 
      - list [ref=e11]:
        - listitem [ref=e12]:
          - link "" [ref=e13] [cursor=pointer]:
            - /url: https://naveenautomationlabs.com/opencart/index.php?route=information/contact
            - generic [ref=e14]: 
          - text: "123456789"
        - listitem [ref=e15]:
          - link " My Account" [expanded] [active] [ref=e16] [cursor=pointer]:
            - /url: https://naveenautomationlabs.com/opencart/index.php?route=account/account
            - generic [ref=e17]: 
            - text: My Account
          - list [ref=e19]:
            - listitem [ref=e20]:
              - link "Register" [ref=e21] [cursor=pointer]:
                - /url: https://naveenautomationlabs.com/opencart/index.php?route=account/register
            - listitem [ref=e22]:
              - link "Login" [ref=e23] [cursor=pointer]:
                - /url: https://naveenautomationlabs.com/opencart/index.php?route=account/login
        - listitem [ref=e24]:
          - link " Wish List (0)" [ref=e25] [cursor=pointer]:
            - /url: https://naveenautomationlabs.com/opencart/index.php?route=account/wishlist
            - generic [ref=e26]: 
            - text: Wish List (0)
        - listitem [ref=e27]:
          - link " Shopping Cart" [ref=e28] [cursor=pointer]:
            - /url: https://naveenautomationlabs.com/opencart/index.php?route=checkout/cart
            - generic [ref=e29]: 
            - text: Shopping Cart
        - listitem [ref=e30]:
          - link " Checkout" [ref=e31] [cursor=pointer]:
            - /url: https://naveenautomationlabs.com/opencart/index.php?route=checkout/checkout
            - generic [ref=e32]: 
            - text: Checkout
  - banner [ref=e33]:
    - generic [ref=e35]:
      - link "naveenopencart" [ref=e38] [cursor=pointer]:
        - /url: https://naveenautomationlabs.com/opencart/index.php?route=common/home
        - img "naveenopencart" [ref=e39]
      - generic [ref=e41]:
        - textbox "Search" [ref=e42]
        - button "" [ref=e44] [cursor=pointer]:
          - generic [ref=e45]: 
      - button " 0 item(s) - $0.00" [ref=e48] [cursor=pointer]:
        - generic [ref=e49]: 
        - text: 0 item(s) - $0.00
  - navigation [ref=e51]:
    - generic: 
    - list [ref=e53]:
      - listitem [ref=e54]:
        - link "Desktops" [ref=e55] [cursor=pointer]:
          - /url: https://naveenautomationlabs.com/opencart/index.php?route=product/category&path=20
      - listitem [ref=e56]:
        - link "Laptops & Notebooks" [ref=e57] [cursor=pointer]:
          - /url: https://naveenautomationlabs.com/opencart/index.php?route=product/category&path=18
      - listitem [ref=e58]:
        - link "Components" [ref=e59] [cursor=pointer]:
          - /url: https://naveenautomationlabs.com/opencart/index.php?route=product/category&path=25
      - listitem [ref=e60]:
        - link "Tablets" [ref=e61] [cursor=pointer]:
          - /url: https://naveenautomationlabs.com/opencart/index.php?route=product/category&path=57
      - listitem [ref=e62]:
        - link "Software" [ref=e63] [cursor=pointer]:
          - /url: https://naveenautomationlabs.com/opencart/index.php?route=product/category&path=17
      - listitem [ref=e64]:
        - link "Phones & PDAs" [ref=e65] [cursor=pointer]:
          - /url: https://naveenautomationlabs.com/opencart/index.php?route=product/category&path=24
      - listitem [ref=e66]:
        - link "Cameras" [ref=e67] [cursor=pointer]:
          - /url: https://naveenautomationlabs.com/opencart/index.php?route=product/category&path=33
      - listitem [ref=e68]:
        - link "MP3 Players" [ref=e69] [cursor=pointer]:
          - /url: https://naveenautomationlabs.com/opencart/index.php?route=product/category&path=34
  - generic [ref=e72]:
    - generic [ref=e73]:
      - generic [ref=e75]:
        - img "MacBookAir" [ref=e77]
        - link "iPhone 6" [ref=e79] [cursor=pointer]:
          - /url: index.php?route=product/product&path=57&product_id=49
          - img "iPhone 6" [ref=e80]
        - img "MacBookAir" [ref=e82]
        - link "iPhone 6" [ref=e84] [cursor=pointer]:
          - /url: index.php?route=product/product&path=57&product_id=49
          - img "iPhone 6" [ref=e85]
      - generic:
        - generic [ref=e89] [cursor=pointer]: 
        - generic [ref=e90] [cursor=pointer]: 
    - heading "Featured" [level=3] [ref=e91]
    - generic [ref=e92]:
      - generic [ref=e94]:
        - link "MacBook" [ref=e96] [cursor=pointer]:
          - /url: https://naveenautomationlabs.com/opencart/index.php?route=product/product&product_id=43
          - img "MacBook" [ref=e97]
        - generic [ref=e98]:
          - heading "MacBook" [level=4] [ref=e99]:
            - link "MacBook" [ref=e100] [cursor=pointer]:
              - /url: https://naveenautomationlabs.com/opencart/index.php?route=product/product&product_id=43
          - paragraph [ref=e101]: Intel Core 2 Duo processor Powered by an Intel Core 2 Duo processor at speeds up to 2.16GHz..
          - paragraph [ref=e102]:
            - text: $602.00
            - generic [ref=e103]: "Ex Tax: $500.00"
        - generic [ref=e104]:
          - button " Add to Cart" [ref=e105] [cursor=pointer]:
            - generic [ref=e106]: 
            - text: Add to Cart
          - button "" [ref=e107] [cursor=pointer]:
            - generic [ref=e108]: 
          - button "" [ref=e109] [cursor=pointer]:
            - generic [ref=e110]: 
      - generic [ref=e112]:
        - link "iPhone" [ref=e114] [cursor=pointer]:
          - /url: https://naveenautomationlabs.com/opencart/index.php?route=product/product&product_id=40
          - img "iPhone" [ref=e115]
        - generic [ref=e116]:
          - heading "iPhone" [level=4] [ref=e117]:
            - link "iPhone" [ref=e118] [cursor=pointer]:
              - /url: https://naveenautomationlabs.com/opencart/index.php?route=product/product&product_id=40
          - paragraph [ref=e119]: iPhone is a revolutionary new mobile phone that allows you to make a call by simply tapping a nam..
          - paragraph [ref=e120]:
            - text: $123.20
            - generic [ref=e121]: "Ex Tax: $101.00"
        - generic [ref=e122]:
          - button " Add to Cart" [ref=e123] [cursor=pointer]:
            - generic [ref=e124]: 
            - text: Add to Cart
          - button "" [ref=e125] [cursor=pointer]:
            - generic [ref=e126]: 
          - button "" [ref=e127] [cursor=pointer]:
            - generic [ref=e128]: 
      - generic [ref=e130]:
        - link "Apple Cinema 30\"" [ref=e132] [cursor=pointer]:
          - /url: https://naveenautomationlabs.com/opencart/index.php?route=product/product&product_id=42
          - img "Apple Cinema 30\"" [ref=e133]
        - generic [ref=e134]:
          - heading "Apple Cinema 30\"" [level=4] [ref=e135]:
            - link "Apple Cinema 30\"" [ref=e136] [cursor=pointer]:
              - /url: https://naveenautomationlabs.com/opencart/index.php?route=product/product&product_id=42
          - paragraph [ref=e137]: The 30-inch Apple Cinema HD Display delivers an amazing 2560 x 1600 pixel resolution. Designed sp..
          - paragraph [ref=e138]:
            - text: $110.00 $122.00
            - generic [ref=e139]: "Ex Tax: $90.00"
        - generic [ref=e140]:
          - button " Add to Cart" [ref=e141] [cursor=pointer]:
            - generic [ref=e142]: 
            - text: Add to Cart
          - button "" [ref=e143] [cursor=pointer]:
            - generic [ref=e144]: 
          - button "" [ref=e145] [cursor=pointer]:
            - generic [ref=e146]: 
      - generic [ref=e148]:
        - link "Canon EOS 5D" [ref=e150] [cursor=pointer]:
          - /url: https://naveenautomationlabs.com/opencart/index.php?route=product/product&product_id=30
          - img "Canon EOS 5D" [ref=e151]
        - generic [ref=e152]:
          - heading "Canon EOS 5D" [level=4] [ref=e153]:
            - link "Canon EOS 5D" [ref=e154] [cursor=pointer]:
              - /url: https://naveenautomationlabs.com/opencart/index.php?route=product/product&product_id=30
          - paragraph [ref=e155]: Canon's press material for the EOS 5D states that it 'defines (a) new D-SLR category', while we'r..
          - paragraph [ref=e156]:
            - text: $98.00 $122.00
            - generic [ref=e157]: "Ex Tax: $80.00"
        - generic [ref=e158]:
          - button " Add to Cart" [ref=e159] [cursor=pointer]:
            - generic [ref=e160]: 
            - text: Add to Cart
          - button "" [ref=e161] [cursor=pointer]:
            - generic [ref=e162]: 
          - button "" [ref=e163] [cursor=pointer]:
            - generic [ref=e164]: 
    - generic [ref=e165]:
      - generic [ref=e167]:
        - img "NFL" [ref=e169]
        - img "RedBull" [ref=e171]
        - img "Sony" [ref=e173]
        - img "Starbucks" [ref=e175]
        - img "Nintendo" [ref=e177]
        - img "Harley Davidson" [ref=e179]
        - img "Dell" [ref=e181]
        - img "Disney" [ref=e183]
        - img "Coca Cola" [ref=e185]
        - img "Burger King" [ref=e187]
        - img "Canon" [ref=e189]
        - img "NFL" [ref=e191]
        - img "RedBull" [ref=e193]
        - img "Sony" [ref=e195]
        - img "Starbucks" [ref=e197]
        - img "Nintendo" [ref=e199]
        - img "Harley Davidson" [ref=e201]
        - img "Dell" [ref=e203]
        - img "Disney" [ref=e205]
        - img "Coca Cola" [ref=e207]
        - img "Burger King" [ref=e209]
      - generic:
        - generic [ref=e222] [cursor=pointer]: 
        - generic [ref=e223] [cursor=pointer]: 
  - contentinfo [ref=e224]:
    - generic [ref=e225]:
      - generic [ref=e226]:
        - generic [ref=e227]:
          - heading "Information" [level=5] [ref=e228]
          - list [ref=e229]:
            - listitem [ref=e230]:
              - link "About Us" [ref=e231] [cursor=pointer]:
                - /url: https://naveenautomationlabs.com/opencart/index.php?route=information/information&information_id=4
            - listitem [ref=e232]:
              - link "Delivery Information" [ref=e233] [cursor=pointer]:
                - /url: https://naveenautomationlabs.com/opencart/index.php?route=information/information&information_id=6
            - listitem [ref=e234]:
              - link "Privacy Policy" [ref=e235] [cursor=pointer]:
                - /url: https://naveenautomationlabs.com/opencart/index.php?route=information/information&information_id=3
            - listitem [ref=e236]:
              - link "Terms & Conditions" [ref=e237] [cursor=pointer]:
                - /url: https://naveenautomationlabs.com/opencart/index.php?route=information/information&information_id=5
        - generic [ref=e238]:
          - heading "Customer Service" [level=5] [ref=e239]
          - list [ref=e240]:
            - listitem [ref=e241]:
              - link "Contact Us" [ref=e242] [cursor=pointer]:
                - /url: https://naveenautomationlabs.com/opencart/index.php?route=information/contact
            - listitem [ref=e243]:
              - link "Returns" [ref=e244] [cursor=pointer]:
                - /url: https://naveenautomationlabs.com/opencart/index.php?route=account/return/add
            - listitem [ref=e245]:
              - link "Site Map" [ref=e246] [cursor=pointer]:
                - /url: https://naveenautomationlabs.com/opencart/index.php?route=information/sitemap
        - generic [ref=e247]:
          - heading "Extras" [level=5] [ref=e248]
          - list [ref=e249]:
            - listitem [ref=e250]:
              - link "Brands" [ref=e251] [cursor=pointer]:
                - /url: https://naveenautomationlabs.com/opencart/index.php?route=product/manufacturer
            - listitem [ref=e252]:
              - link "Gift Certificates" [ref=e253] [cursor=pointer]:
                - /url: https://naveenautomationlabs.com/opencart/index.php?route=account/voucher
            - listitem [ref=e254]:
              - link "Affiliate" [ref=e255] [cursor=pointer]:
                - /url: https://naveenautomationlabs.com/opencart/index.php?route=affiliate/login
            - listitem [ref=e256]:
              - link "Specials" [ref=e257] [cursor=pointer]:
                - /url: https://naveenautomationlabs.com/opencart/index.php?route=product/special
        - generic [ref=e258]:
          - heading "My Account" [level=5] [ref=e259]
          - list [ref=e260]:
            - listitem [ref=e261]:
              - link "My Account" [ref=e262] [cursor=pointer]:
                - /url: https://naveenautomationlabs.com/opencart/index.php?route=account/account
            - listitem [ref=e263]:
              - link "Order History" [ref=e264] [cursor=pointer]:
                - /url: https://naveenautomationlabs.com/opencart/index.php?route=account/order
            - listitem [ref=e265]:
              - link "Wish List" [ref=e266] [cursor=pointer]:
                - /url: https://naveenautomationlabs.com/opencart/index.php?route=account/wishlist
            - listitem [ref=e267]:
              - link "Newsletter" [ref=e268] [cursor=pointer]:
                - /url: https://naveenautomationlabs.com/opencart/index.php?route=account/newsletter
      - separator [ref=e269]
      - paragraph [ref=e270]:
        - text: Powered By
        - link "OpenCart" [ref=e271] [cursor=pointer]:
          - /url: http://www.opencart.com
        - text: naveenopencart © 2026
```

# Test source

```ts
  1  | import {Page, expect, Locator} from "@playwright/test";
  2  | 
  3  | export class HomePage{
  4  | 
  5  |     private readonly page: Page;
  6  |     //locators
  7  |     private readonly linkMyAccount: Locator;
  8  |     private readonly linkRegister: Locator;
  9  |     private readonly linkLogin: Locator;
  10 |     private readonly textSeachbox: Locator;
  11 |     private readonly buttonSearch: Locator;
  12 |     //constructor
  13 |     constructor(page: Page){
  14 |         this.page = page;
  15 |         this.linkMyAccount = page.locator('span:has-text("My Account")');
  16 |         this.linkRegister = page.locator('span:has-text("Register")');
  17 |         this.linkLogin = page.locator('span:has-text("Login")');
  18 |         this.textSeachbox = page.locator('input[placeholder="Search"]');
  19 |         this.buttonSearch = page.locator('#search button[type="button"]');
  20 |     }
  21 |     //action methods
  22 |     // Check if HomePage exists
  23 |     async isHomePageExist(){
  24 |         
  25 |         let title = await this.page.title();
  26 |         if(title){ // Check if the title is not empty
  27 |             return true;
  28 |         }
  29 |         return false;
  30 |         
  31 |     }
  32 | 
  33 |     // Click on My Account link
  34 |     async clickOnMyAccount(){
  35 |         try{
  36 |         await this.linkMyAccount.click();
  37 |         }
  38 |         catch(error){
  39 |             console.error("Error occurred while clicking on My Account link:", error);
  40 |             throw error;
  41 |         }
  42 |     }
  43 |     // Click on Register link
  44 |     async clickOnRegister(){
  45 |         try{
> 46 |         await this.linkRegister.click();
     |                                 ^ Error: locator.click: Test timeout of 30000ms exceeded.
  47 |         }
  48 |         catch(error){
  49 |             console.error("Error occurred while clicking on Register link:", error);
  50 |             throw error;
  51 |         }
  52 |     }
  53 |     // Click on Login link
  54 |     async clickOnLogin(){
  55 |         try{
  56 |         await this.linkLogin.click();
  57 |         }
  58 |         catch(error){
  59 |             console.error("Error occurred while clicking on Login link:", error);
  60 |             throw error;
  61 |         }
  62 |     }
  63 |     // Search for a product
  64 |     async searchProduct(productName: string){
  65 |         try{
  66 |             await this.textSeachbox.fill(productName);
  67 |             await this.buttonSearch.click();
  68 |         }
  69 |         catch(error){
  70 |             console.error("Error occurred while searching for product:", error);
  71 |             throw error;
  72 |         }
  73 |     } // Get the search results and return the count of products found
  74 |     async getSearchResultsCount(){
  75 |         try{
  76 |             const searchResults = this.page.locator('.product-layout');
  77 |             return await searchResults.count();
  78 |         }
  79 |         catch(error){
  80 |             console.error("Error occurred while getting search results count:", error);
  81 |             throw error;
  82 |         }
  83 |     }
  84 |     }   
```