# Copyright (c) 2023, Gopi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Salary(Document):
	def validate(self):
		frappe.log_error(title='validate',message='checking commit works or not')
