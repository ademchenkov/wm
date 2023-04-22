class AsyncContextManager:
	# enter the async context manager
	async def __aenter__(self):
		# report a message
		print('>entering the context manager')

	# exit the async context manager
	async def __aexit__(self, exc_type, exc, tb):
		# report a message
		print('>exiting the context manager')