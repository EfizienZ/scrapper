import csv
import scrapes
import mailing
import analysis
from dotenv import load_dotenv


load_dotenv()

a = analysis.create_analysis()
# d = mailing.send_mail('mariofelectronica@gmail.com')

cities = [
    '/sevilla',
    '/cadiz',
    '/cordoba',
    '/granada',
    '/huelva',
    '/jaen',
    '/malaga'
    
    '/albacete',
    '/ciudad-real',
    '/cuenca',
    '/guadalajara',
    '/toledo'
    
    '/caceres',
    '/badajoz'
    
    '/murcia',

    '/navarra',

    '/cantabria',

    '/asturias',

    '/huesca',
    '/zaragoza',
    '/teruel'
    
    '/valencia',
    '/alicante',
    '/castellon',

    '/valladolid',
    '/leon',
    '/zamora',
    '/avila',
    '/segovia',
    '/soria',
    '/burgos',
    '/palencia',

    '/ourense',
    '/pontevedra',
    '/lugo',
    '/coruna',

    '/la-rioja',

    '/alava',
    '/bizkaia',
    '/gipuzkoa',

    '/baleares',

    '/las-palmas',

    '/girona',
    '/barcelona',
    '/lleida',
    '/tarragona',

    '/madrid'
]

scrapes.scrape(cities)
