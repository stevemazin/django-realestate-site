from .models import Listing

bedroom_choices = {
  '1':1,
  '2':2,
  '3':3,
  '4':4,
  '5':5,
  '6':6,
  '7':7,
  '8':8,
  '9':9,
  '10':10
  }

price_choices = {
  '1000000':'Ksh 1,000,000',
  '1500000':'Ksh 1,500,000',
  '2000000':'Ksh 2,000,000',
  '2500000':'Ksh 2,500,000',
  '3000000':'Ksh 3,000,000',
  '3500000':'Ksh 3,500,000',
  '4000000':'Ksh 4,000,000',
  '4500000':'Ksh 4,500,000',
  '5000000':'Ksh 5,000,000',
  '5000001':'Ksh 5M+',
}

locality_choices = {
  'Kasarani': 'Kasarani',
  'Thindigua': 'Kiambu',
  'Machakos': 'Machakos',
  'Mombasa': 'Mombasa',
}

agreement_choices = {
  'rent': 'Rent a space',
  'buy': 'Buy a home',
  'purchasable': 'Rent a space with owning options'
}