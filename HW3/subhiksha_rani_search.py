import mysql.connector
import sys
import csv
reload(sys)
sys.setdefaultencoding('cp1252')

def search(keywords):
	cnx = mysql.connector.connect(user='inf551', password='inf551', host='127.0.0.1', database='inf551')
	cursor = cnx.cursor()
	query = "SELECT App, Review, AVG(Sentiment_Polarity) as Sentiment_Polarity FROM googleplaystore_user_reviews WHERE MATCH(Review) AGAINST('"+keywords+"') AND Sentiment_Polarity>=0.8 AND Sentiment_Subjectivity>=0.8 GROUP BY App ORDER BY AVG(Sentiment_Polarity) DESC LIMIT 10;"
	cursor.execute(query)
	with open('subhiksha_rani_q2.csv', 'w') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerow(['App','Review','Sentiment_Polarity'])
		for name in cursor:
			li= []
			for value in name:
				if name[2]:
					li.append(value)
				else:
					li.append(str(value).encode('cp1252'))
			writer.writerow(li)
	csvFile.close()
	cursor.close()
	cnx.close()
	

if __name__=="__main__":    
    search(sys.argv[1])
