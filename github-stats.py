from datetime import datetime
import time
import sys
import os
import requests


def get_stats(repo, id, stats):
	url='https://api.github.com/repos/{}/stats/contributors'.format(repo)
	res = requests.get(url)
	for entry in res.json():
		if entry['author']['login']==id:
			total=entry['total']
			if total==0:
				return stats
			for week in entry['weeks']:
				ts = datetime.utcfromtimestamp(int(week['w']))
				for stat in stats:
					if ts.year==stat[0] and ts.month==stat[1]:
						stats[stat]+=week['c']
	return stats


def main(args):
	months = 12
	now = time.localtime()
	m=[time.localtime(time.mktime((now.tm_year, now.tm_mon - n, 1, 0, 0, 0, 0, 0, 0)))[:2] for n in range(months)]
	
	filename = "./input"
	assert os.path.exists(filename), "file {} not found".format(filename)

	output=open("output.csv", 'w')

	# write header
	output.write("Github ID,Repo,{}\n".format(','.join(['{}/{}'.format(v[0], v[1]) for v in m])))

	with open(filename, 'r') as file:
		content = file.readlines()   
		for row in content:
			columns = [x.strip() for x in row.split('\t')]			
			id=columns[0]
			repos=[x for x in columns[1].split(',')]
			for repo in repos:
				print("Fetching stats for", id, repo)
				stats={t: 0 for t in m}
				result=get_stats(repo,id, stats)
				output.write("{},{},{}\n".format(id, repo, ','.join(str(v) for v in result.values())))
	

if __name__ == "__main__":
    main(sys.argv[1:])