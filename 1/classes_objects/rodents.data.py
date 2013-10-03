from rodents import Rodent

f = open('./rodents.csv')
rodents={}

for line in f.readlines():
	tag_id,weight = line.split(',')
	if tag_id not in rodents:
		rodents[tag_id] = Rodent(tag_id)
		rodents[tag_id].add_weight(weight)
	else:
		rodents[tag_id].add_weight(weight)

print rodents
for key in rodents:
	print rodents[key].tag_id, rodents[key].weights

f.close()
