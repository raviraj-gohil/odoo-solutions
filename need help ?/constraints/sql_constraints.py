	_sql_constraints = [
			('check_expected_price','CHECK(expected_price >= 0)','Enter Positive value of expected_price'),
			('check_selling_price','CHECK(selling_price >= 0)','Enter Positive value of selling_price')
	]
