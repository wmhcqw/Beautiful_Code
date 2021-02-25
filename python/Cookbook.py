

def get_first_last(inputs):
    first, *middle, last = inputs
    return first, last


def dict_max_or_min_value_search(input_dict):
	# return max(zip(input_dict.values(), input_dict.keys())
	return min(zip(input_dict.values(), input_dict.keys()))


def dict_same_or_diff_value_search(dict1, dict2):
	# return dict1.keys() - dict2.keys()
	# return dict1.items() & dict2.items()
	return dict1.keys() & dict2.keys()


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)