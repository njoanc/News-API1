class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,author,title,description,url,image,publishedAt,content):
        self.id =id
        self.name=name 
        self.author=author
        self.title = title
        self.description=description
        self.url = url
        self.image = image
        self.publishedAt = publishedAt
        self.content = content