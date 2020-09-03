from util import GetAnalystsTasks

values = GetAnalystsTasks.GetAnalystsTasks("87")
values.collect_data()

print(values.get_data_collection())