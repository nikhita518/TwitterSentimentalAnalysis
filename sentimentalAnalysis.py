import twitter

api = twitter.Api(consumer_key='ebuklmvsLHTEBfk5kSn9roFz2',
                    consumer_secret='jvdt8tzNpRTXdLa5s4FeTiZZrzfo3js3NnXnW9sdekqcFAL159',
                    access_token_key='906794650920304640-FI13JGDbWYClyqgdSRaxUb30RJ1cEtf',
                    access_token_secret='BKLpark2eqHkKj6bPV62tkIuR8vX82PcpxshBY4wNnFMY')

#print(api.VerifyCredentials())

def createTestData(search_string):
    try:
        tweets_fetched = api.GetSearch(search_string, count = 100)
        #print("fetched")
        return [{"text":status.text,"label":None} for status in tweets_fetched]
    except:
        return None
search_string = input("Hi there! What do you want to search today")
testData = createTestData(search_string)


def createTrainingCorpus(corpusFile,tweetDataFile):
    import csv
    corpus = []
    with open(corpusFile,'rb') as csvfile:
        lineReader = csv.reader(csvfile,delimter=',',quotechar="\"")
        for row in lineReader:
            corpus.append({"tweet_id":row[2],"label":row[1],"topic":row[0]})
            
import time 
rate_limit=180
sleep_time=900/180    
trainingData=[]
