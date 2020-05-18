# API Documentation
This API contain chinook.db data with some data wrangling. You can check data folder to get `chinook.db` to look RAW data before process in this end point

Where full URLs are provided in responses they will be rendered as if service is running on 'https://algoritma-api-capstone.herokuapp.com/'.

___
## Open Endpoints : 
Open endpoints require no Authentication.

**Total Peminat music di negara India by genre** : 
> `GET /india`    

Return list of list genre in India, year limited from 2009 - 2013

**10 List Negara dengan peminat music Rock Terbesar di dunia tahun 2012** : 

> `GET /Statis`    

Return list of type_genre music di tahun 2012 diseluruh dunia

**sales  by Album di dunia berdasarkan range tahun 2009-2013** : 

> `GET /Sales_ALbum/country_cus  

Return sales disemua negara where selected `<country_cus>` memunculkan berdasarkan negara yang dipilih


## Example :

I want get list of county 

**Request** :  


Method = GET 
https://r1capstone-api-restu.herokuapp.com/docs

Method = GET (Dinamis)
https://r1capstone-api-restu.herokuapp.com/Sales_Album/USA

Method = GET (Statis)  
URL = https://r1capstone-api-restu.herokuapp.com/india

URL = https://r1capstone-api-restu.herokuapp.com/statis


**Response** : 
```json
{"InvoiceDate":{"0":1356825600000,"1":1343260800000,"2":1341446400000,"3":1346371200000,"4":1354838400000,"5":1338768000000,"6":1330300800000,"7":1346112000000,"8":1346803200000,"9":1349049600000},"Country":{"0":"USA","1":"Canada","2":"Italy","3":"Australia","4":"Brazil","5":"Denmark","6":"Norway","7":"Poland","8":"Czech Republic","9":"Portugal"},"Genre":{"0":"Rock","1":"Rock","2":"Rock","3":"Rock","4":"Rock","5":"Rock","6":"Rock","7":"Rock","8":"Rock","9":"Rock"},"jumlah":{"0":30,"1":13,"2":13,"3":12,"4":10,"5":10,"6":9,"7":9,"8":8,"9":7}}
