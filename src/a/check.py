import requests

def send_request(val1):

	try:
		response = requests.post(
			url="http://check.springhouse.com.tw/",
			headers={
				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
				"Accept-Encoding": "gzip, deflate",
				"Cookie": "PHPSESSID=ppuf7v3n98bkq5j28gpdv8jdd7",
				"Referer": "http://check.springhouse.com.tw/",
				"Connection": "keep-alive",
				"Host": "check.springhouse.com.tw",
				"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0",
				"Content-Type": "application/x-www-form-urlencoded",
				"Accept-Language": "en-US,en;q=0.5",
			},
			data={
				"field": val1,
				"key": "0540",
				"act": "search",
				"file": "09242015",
				"std[]": "0",
			},
		)
		print('Response HTTP Status Code: {status_code}'.format(
			status_code=response.status_code))
		print('Response HTTP Response Body: {content}'.format(
			content=response.content.decode('big5').encode('utf-8')))
	except requests.exceptions.RequestException:
		print('HTTP Request failed')
