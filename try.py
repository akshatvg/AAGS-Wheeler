import requests	 

def NewsFromBBC(): 
	
	main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=e4313a22f54042c9aba095ce5354be51"

	open_bbc_page = requests.get(main_url).json() 

	article = open_bbc_page["articles"] 

    
	results = [] 
	
	for ar in article: 
		results.append(ar["title"]) 
		
	for i in range(len(results)): 
        print(i + 1, results[i])				 

if __name__ == '__main__': 
	
	NewsFromBBC() 
