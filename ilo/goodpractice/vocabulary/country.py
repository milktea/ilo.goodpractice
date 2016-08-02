from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

from p01.vocabulary.country import ISO3166Alpha2CountryVocabulary 

class Country(grok.GlobalUtility):
    grok.name('ilo.goodpractice.country')
    grok.implements(IVocabularyFactory)

    def __call__(self,context):
		data = [samples for samples in ISO3166Alpha2CountryVocabulary(context)]
		values = ['Africa regional', 
				'Asia regional', 
				'Americas regional', 
				'Europe regional', 'Arab States and Inter-regional/Global']
		for value in values:
			data.append(SimpleTerm(value))
		return SimpleVocabulary(data)