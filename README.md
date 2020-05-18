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
{"Peminat":{"[2009,"India","R&B\/Soul"]":23.76,"[2009,"India","Rock"]":27.72,"[2010,"India","Jazz"]":13.86,"[2010,"India","Latin"]":69.3,"[2010,"India","Rock"]":114.84,"[2010,"India","Sci Fi & Fantasy"]":1.99,"[2011,"India","Alternative & Punk"]":40.59,"[2011,"India","Blues"]":26.73,"[2011,"India","Jazz"]":69.3,"[2011,"India","Latin"]":55.44,"[2011,"India","Metal"]":3.96,"[2011,"India","Rock"]":82.17,"[2012,"India","Alternative & Punk"]":62.37,"[2012,"India","Classical"]":3.96,"[2012,"India","Rock"]":17.82,"[2013,"India","Jazz"]":15.84,"[2013,"India","Metal"]":35.64,"[2013,"India","TV Shows"]":1.99}}
