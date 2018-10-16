import asyncio
import os
import urllib.request

async def download_coroutine(url):
	request = urllib.request.urlopen(url)
	filename = os.path.basename(url)

	with open(filename, 'wb') as f:
		while True:
			chunk = request.read(1024)
			if chunk:
				f.write(chunk)
			else:
				break
	msg = 'Download complete, {filename}'.format(filename = filename)
	return msg

async def main(urls):
	coroutines = [download_coroutine(url) for url in urls]
	completed, pending = await asyncio.wait(coroutines)

	for item in completed:
		print(item.result())

if __name__ == '__main__':
	urls = ['http://www.irs.gov/pub/irs-pdf/f1040.pdf',
		'http://www.irs.gov/pub/irs-pdf/f1040a.pdf',
		'http://www.irs.gov/pub/irs-pdf/f1040ez.pdf']
	event_loop = asyncio.get_event_loop()
	try:
		event_loop.run_until_complete(main(urls))
	finally:
		event_loop.close()
