limit = int(input())
data = [input().lower() for x in range(1, limit + 1)]
result = {}


def dict_sort(dict):
    appened = {}
    for key in sorted(dict.keys()):
        appened[key] = dict[key]
    return appened


for index, j in enumerate(data):
    final_data = {}
    for k in j:
        if k not in final_data:
            final_data[k] = 1
        else:
            final_data[k] += 1
    result[index] = dict_sort(final_data)

for key, value in result.items():
    print("Case", str(key + 1), ":")
    for k_index, k_value in value.items():
        print(str(k_index), str(k_value))
