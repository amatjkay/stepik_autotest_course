def test_substring(full_string, substring):
	full_string = 'fulltext'
	substring = 'some_value'
	assert substring in full_string, "expected {} to be substring of {}".format(substring, full_string)
