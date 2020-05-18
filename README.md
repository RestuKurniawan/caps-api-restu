# API Documentation
This API contain chinook.db data with some data wrangling. You can check data folder to get `chinook.db` to look RAW data before process in this end point

Where full URLs are provided in responses they will be rendered as if service is running on 'https://algoritma-api-capstone.herokuapp.com/'.

___
## Open Endpoints : 
Open endpoints require no Authentication.

**Total Peminat music di negara India by genre** : 
> `GET /india`    

Return list of list genre in India, year limited from 2009 - 2013

**List Genre music di dunia tahun 2012 ** : 

> `GET /Statis`    

Return list of type_genre music di tahun 2012 diseluruh dunia

**sales  by Album di dunia berdasarkan range tahun 2009-2013** : 

> `GET /Sales_ALbum/country_cus  

Return sales disemua negara where selected `<country_cus>` memunculkan berdasarkan negara yang dipilih


## Example :

I want get list of county 

**Request** :  

Method = GET  
URL =  https://algoritma-api-capstone.herokuapp.com/

**Response** : 
```json
{
    "0": {
        "0": "Brazil",
        "1": "Germany",
        "2": "Canada",
        "3": "Norway",
        "4": "Czech Republic",
        "5": "Austria",
        "6": "Belgium",
        "7": "Denmark",
        "8": "USA",
        "9": "Portugal",
        "10": "France",
        "11": "Finland",
        "12": "Hungary",
        "13": "Ireland",
        "14": "Italy",
        "15": "Netherlands",
        "16": "Poland",
        "17": "Spain",
        "18": "Sweden",
        "19": "United Kingdom",
        "20": "Australia",
        "21": "Argentina",
        "22": "Chile",
        "23": "India"
    }
}
```