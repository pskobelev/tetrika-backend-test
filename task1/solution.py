import inspect


def strict(func):
	def wrapper(*args):
		arg_names = inspect.getfullargspec(func).args
		for arg, name in zip(args, arg_names):
			if not isinstance(arg, inspect.get_annotations(func)[name]):
				raise TypeError('Наташ мы все сломали')
		return func(*args)

	return wrapper
