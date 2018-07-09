# import datetime
# import re
#
# from django.utils.html import strip_tags
#
#
# def count_words(html_string):
#
# 		"""
# 		<h1> this test </h1>
#
# 		"""
#
# 		word_string = strip_tags(html_string)
# 		matching_words = re.findall(r'\w+', word_string)
# 		count = len(matching_words)
# 		return count
#
# def get_read_time(html_string):
# 		count =count_words(html_string)
# 		read_time_min = (count/200.0)
# 		read_time
