size_of_string = int(input())
string_data = []
for i in range(size_of_string):
	string_get = input()
	string_data.append(string_get)
size_of_query = int(input())
query_data = []
for i in range(size_of_query):
	query_get = input()
	query_data.append(query_get)

for query in query_data:
	print(string_data.count(query))
