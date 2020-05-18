from flask import Flask, request
import pandas as pd
import numpy as np
import gunicorn 

import sqlite3
app = Flask(__name__)

## end point statis 1
# mendapatkan keseluruhan data dari database chinook untuk trend penyuka music berdasarkan type genre dari tahun ke tahun di negara india
@app.route('/india', methods=['GET']) 
def get_data():
	conn = sqlite3.connect("data/chinook.db")
	DF1 = pd.read_sql_query('''SELECT i.invoiceId, i.invoiceDate, i.BillingCountry, i.BillingCity,
    i.Total, ii.UnitPrice, ii.Quantity, t.Name as Name_Track, a.Title as Name_Album, 
    g.Name as Type_Genre, c.FirstName || ' ' || c.lastName as Fullname_cus,
    c.Country as country_cus
    FROM invoices as i 
    LEFT JOIN invoice_items as ii
    ON i.invoiceId = ii.InvoiceId
    LEFT JOIN tracks as t
    ON t.TrackId = ii.Trackid
    LEFT JOIN Albums as a
    on t.AlbumId = a.AlbumId
    LEFT JOIN genres as g
    on t.GenreId = g.GenreId
    LEFT JOIN customers as c
    ON c.CustomerId = i.CustomerId
    WHERE c.Country = 'India' 
    ''', conn, parse_dates='InvoiceDate')
	DF1['Year'] = DF1['InvoiceDate'].dt.year
	india = DF1.dropna(how = 'all')
	india = pd.crosstab(
            index= [DF1.Year,DF1.BillingCountry, DF1.Type_Genre],
            columns = 'Peminat',
            values= DF1['Total'],
            aggfunc= 'sum').round(2)
	return india.to_json()



# End Point STatis 2
# mendapatkan keseluruhan data dari database chinook untuk penyuka music Rock 10 terbesae di dunia tahun 2012
@app.route('/statis', methods = ['GET'])
def route_static():
	conn = sqlite3.connect("data/chinook.db")
	statis = pd.read_sql_query(
	'''
	SELECT
	invoiceDate, BillingCountry AS Country, g.name AS Genre, count(g.name) as jumlah
	FROM invoices
	LEFT JOIN invoice_items 
	ON invoices.invoiceId = invoice_items.InvoiceId
	LEFT JOIN tracks 
	ON invoice_items.TrackId = tracks.TrackId 
	LEFT JOIN genres as g 
	ON tracks.GenreId = g.GenreId
	where InvoiceDate like ('2012-%') and Genre = 'Rock'
	group by BillingCountry
	order by jumlah
	desc limit 10
	''', conn, parse_dates='InvoiceDate')

	return statis.to_json()


# End Point Dinamis 2
# mendapatkan keseluruhan data sales dari database chinook berdasarkan negara disetiap tahun

@app.route('/Sales_Album/<country_cus>', methods = ['GET'])
def Sales_Album(country_cus):
	conn = sqlite3.connect("data/chinook.db")
	DF1 = pd.read_sql_query('''select 
	i.invoiceId,
	i.invoiceDate,
	i.BillingCountry,
	i.BillingCity,
	i.Total,
	ii.UnitPrice,
	ii.Quantity,
	t.Name as Name_Track,
	a.Title as Name_Album,
	g.Name as Type_Genre,
	c.FirstName || ' ' || c.lastName as Fullname_cus,
	c.Country as country_cus

	from
	invoices as i left join invoice_items as ii
	on i.invoiceId = ii.InvoiceId
	left join tracks as t
	on t.TrackId = ii.Trackid
	left join Albums as a
	on t.AlbumId = a.AlbumId
	left join genres as g
	on t.GenreId = g.GenreId
	left join customers as c
	on c.CustomerId = i.CustomerId

	''',conn, parse_dates='InvoiceDate')

	DF1['sales'] = DF1['UnitPrice'] * DF1['Quantity']
	DF1['Year'] = DF1['InvoiceDate'].dt.year
	#DF1.dropna(how = 'all')

	DF2 = pd.pivot_table(data=DF1,
               index='Year',
               columns=['country_cus','Name_Album'],
               values='sales',
               aggfunc='sum') 
	DF2.sort_values('Year', ascending = False) 
	DF2_multi = DF2.stack(level=1).unstack(level=0).replace(np.nan, 'No Transaksi')
	return(DF2_multi[country_cus].to_json())

@app.route("/docs")
def documentation():
    return '''
        <h1> Documentation </h1>
        <h2> Static Endpoints 1 </h2>
        <ol>
            <li>
                <p> '/india', method = GET </p>
                <p> Negara India, trend peminat music berdasarkan type_genre dinegara india berdasarkan tahun ke tahun. </p>
            </li>
        </ol>
         
        <h2> Static Endpoints 2 </h2>
        <ol>
            <li>
                <p> '/statis', method = GET </p>
                <p> Rocket Dunia, data 10 negara peminat music rock terbesar dunia tahun 2012 </p>
            </li>
        </ol>

        <h2> Dynamic Endpoints </h2>
        <ol start = "2">
            <li>
                <p> '/Sales_Album/<country_cus>' , method = GET </p>
                <p> Dinamis, menampilkan sales berdasarkan penjualan album diseluruh dunia dari tiap tahunnya </p>
				<p> Return full data 'Sales_Album'; in JSON format. Currently available data are: </p>
                <ul style="list-style-type:disc;">
                    <li> Chinook.db </li>
                   
            </li>
 
        	</ol>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=5000) 
