class Article:
    all_articles = []

    def __init__(self,id,name,author,title,description,url,urlToImage,publishedAt,):
        self.id =id
        self.name =name
        self.author = author
        self.title =title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt  = publishedAt

        def save_articles(self):
            
