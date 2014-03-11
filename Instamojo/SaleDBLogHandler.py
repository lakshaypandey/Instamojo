import sys
sys.path.insert(0, 'libs')
import webapp2
import gspread
import logging
from models import Sale
from google.appengine.ext import ndb

class SaleDBLogHandler(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'

		qry = Sale.query(Sale.excel_log_status == False)
		results = qry.fetch()
		#result_set = query.filter("excel_log_status=",False)
		#gc = gspread.login('test.instamojo@gmail.com', 'insta_mojo_test')
		self.response.write(qry.count())
	def post(self):
		try:
			logging.debug("logging sale")
			logging.debug("payment_id" + str(self.request.get('payment_id')))
			sale_item = Sale()
			sale_item.currency	= self.request.get('currency')
			sale_item.buyer_phone	= self.request.get('buyer_phone')
			sale_item.offer_slug	= self.request.get('offer_slug')
			sale_item.offer_title	= self.request.get('offer_title')
			sale_item.custom_fields	= self.request.get('custom_fields')
			sale_item.payment_id	= self.request.get('payment_id')
			sale_item.buyer_name	= self.request.get('buyer_name')
			sale_item.status	= self.request.get('status')
			sale_item.buyer	= self.request.get('buyer')
			sale_item.mac	= self.request.get('mac')
			sale_item.unit_price	= float(self.request.get('unit_price'))
			sale_item.quantity	= int(self.request.get('quantity'))
			sale_item.fees	= float(self.request.get('fees'))
			sale_item.amount	= float(self.request.get('amount'))
			sale_item.excel_log_status	= False
			sale_item.put()
			logging.debug("logged")
			self.response.http_status_message(200)
		except Exception as e:
			logging.error(str(e))
			self.error(500)
application = webapp2.WSGIApplication([
    ('/log_sale', SaleDBLogHandler),
    
], debug=True)


