import json

backup_json = open('json/anonymized-backup.json', 'rb')

backup_data = json.load(backup_json)

# https://stackoverflow.com/questions/3391076/repeat-string-to-certain-length
def repeat_to_length(s, wanted):
    return (s * (wanted//len(s) + 1))[:wanted]

verbose_keys = {"courses", "reviews", "users"}

def list_keys_and_types(name, data, indent=0, key_max=-1, str_max=64):
    tabs = repeat_to_length("\t", indent)
    data_type = type(data)
    if data_type != dict:
        if data_type == str and len(data) > str_max:
            data = data[:str_max] + "... (truncated at {} characters)".format(str_max)
        print("{}{}: {} {}".format(tabs, name, data, type(data)))
        return

    keys = list(data.keys())
    key_count = len(keys)
    if key_max == -1:
        key_max = key_count

    print("{}{}: {} ({} of {} keys shown)".format(tabs, name, type(data), min(key_count, key_max), key_count))

    for key in keys[:key_max]:
        list_keys_and_types(key, data[key], indent=indent+1, key_max=(2 if key in verbose_keys else -1))

list_keys_and_types("<root>", backup_data)

