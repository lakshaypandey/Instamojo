from google.appengine.ext import ndb

class Sale(ndb.Model):
	currency = ndb.StringProperty(indexed=False)
	buyer_phone = ndb.StringProperty(indexed=False)
	offer_slug = ndb.StringProperty(indexed=False)
	offer_title = ndb.StringProperty(indexed=False)
	custom_fields = ndb.StringProperty(indexed=False)
	payment_id = ndb.StringProperty(indexed=False)
	buyer_name = ndb.StringProperty(indexed=False)
	status = ndb.StringProperty(indexed=False)
	buyer = ndb.StringProperty(indexed=False)
	mac = ndb.StringProperty(indexed=False)
	unit_price = ndb.FloatProperty(indexed=False)
	quantity = ndb.IntegerProperty(indexed=False)
	fees = ndb.FloatProperty(indexed=False)
	amount = ndb.FloatProperty(indexed=False)
	excel_log_status = ndb.BooleanProperty(indexed=True)
