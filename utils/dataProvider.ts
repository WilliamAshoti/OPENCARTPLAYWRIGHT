import fs from 'fs';
import { parse } from 'csv-parse/sync';

export class DataProvider{
    static getTestDataFromJson(filePath: string):unknown
    {
        try 
        {
            const fileContent = fs.readFileSync(filePath, 'utf8'); // Read the file from the specified path
            return JSON.parse(fileContent); // Parse the JSON content and return it as an object
        } catch (error) {
            console.error('Error reading JSON file:', error);
            throw error;
        }
    }

    static getTestDataFromCsv(filePath: string):unknown
    {
        try 
        {
            const fileContent = fs.readFileSync(filePath); // Read the file from the specified path
            const data: unknown = parse(fileContent, {
                columns: true, // Treat the first row as column headers
                skip_empty_lines: true // Skip empty lines in the CSV file
            });
            return data; // Return the parsed records as an array of objects
        } catch (error) {
            console.error('Error reading CSV file:', error);
            throw error;
        }
    }

}