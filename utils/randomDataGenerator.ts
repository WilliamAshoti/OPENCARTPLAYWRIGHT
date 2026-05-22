import { faker } from '@faker-js/faker';

export class RandomDataUtils {
    static getFirstName(): string {
        return faker.person.firstName();
    }

    static getLastName(): string {
        return faker.person.lastName();
    }

    static getEmail(): string {
        return this.getFirstName().toLowerCase() + '.' + this.getLastName().toLowerCase() + '@example.com';
    }

    static getPhoneNumber() {
        return faker.phone.number(); // Generates a 10-digit phone number
    }

    static getUserName(): string {
        return faker.internet.username();
    }

    static getPassword(): string {
        return faker.internet.password();
    }

    static getRandomCountry(): string {
        return faker.location.country();
    }

    static getRandomState(): string {
        return faker.location.state();
    }

    static getRandomCity(): string {
        return faker.location.city();
    }

    static getRandomPin(): string {
        return faker.location.zipCode();
    }

    static getRandomAddress(): string {
        return faker.location.streetAddress();
    }

    static getRandomPassword(length: number = 10): string {
        return faker.internet.password({ length });
    }

    static getRandomAlphanumeric(length: number): string {
        return faker.internet.password({ length });
    }

    static getRandomNumeric(length: number): string {
        return faker.string.numeric(length);
    }

    static getRandomUUID(): string {
        return faker.string.uuid();
    }
}