# Copyright (c) 2023, Gopi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Salary(Document):
	def validate(self):
		frappe.log_error(title='validate',message='checking commit works or not')
		print(
			"""   Revert check""")

		print("After revert check")

		frappe.log_error(title='checking',message='revert')