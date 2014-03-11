import sys
sys.path.insert(0, 'libs')
import webapp2
import gspread
import logging
from models import Sale
from google.appengine.ext import ndb

class SaleExcelLoghandlerCron(webapp2.RequestHandler):
	def get(self):
		# try:
			gc = gspread.login('test.instamojo@gmail.com', 'insta_mojo_test')
			wks = gc.open("Test").sheet1
			qry = Sale.query(Sale.excel_log_status == True)
			line_count = qry.count()
			qry = Sale.query(Sale.excel_log_status == False)
			results = qry.fetch()
			line_count=line_count+2
			
			for sale_item in results:
				try:
					logging.info("logging to excel , payment id" + str(sale_item.payment_id))
					wks.update_cell(line_count,1,sale_item.currency)
					wks.update_cell(line_count,2,sale_item.buyer_phone)
					wks.update_cell(line_count,3,sale_item.offer_slug)
					wks.update_cell(line_count,4,sale_item.offer_title)
					wks.update_cell(line_count,5,sale_item.custom_fields)
					wks.update_cell(line_count,6,sale_item.payment_id)
					wks.update_cell(line_count,7,sale_item.buyer_name)
					wks.update_cell(line_count,8,sale_item.status)
					wks.update_cell(line_count,9,sale_item.buyer)
					wks.update_cell(line_count,10,sale_item.mac)
					wks.update_cell(line_count,11,sale_item.unit_price)
					wks.update_cell(line_count,12,sale_item.quantity)
					wks.update_cell(line_count,13,sale_item.fees)
					wks.update_cell(line_count,14,sale_item.amount)
					line_count+=1
				except Exception as e:
					logging.error(str(e))
				#	raise e
					continue
				sale_item.excel_log_status=True
				sale_item.put()
				logging.debug("logged")
			self.response.http_status_message(200)
			'''
		# except Exception as e:
		# 	logging.error(str(e))
		# 	raise e
		# 	self.error(500)
		'''
application = webapp2.WSGIApplication([
    ('/excel_logger', SaleExcelLoghandlerCron),
    
], debug=True)


