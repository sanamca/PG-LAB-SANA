class publisher:
    def __init__ (self,pn):
        self.publishername=pn
        
    def display(self):
        print("Publisher Name:",self.publishername)
        
class book(publisher):
    def __init__ (self,pn,tt,aut):
        super(). __init__(pn)
        self.title=tt
        self.author=aut
    
    def display(self):
        print("Title Name: ",self.title)
        print("Author Name:",self.author)
        
class python(book):
    def __init__ (self,pn,tt,aut,pr,pg):
        super(). __init__(pn,tt,aut)
        self.price=pr
        self.page=pg
    
    def pythondisplay(self):
        print("Price: ",self.price)
        print("No. of Pages: ",self.page)
        
        
obj=python("joy publishers","Python","Guido van Rossum",599,230);
obj.display()
obj.pythondisplay();
        
