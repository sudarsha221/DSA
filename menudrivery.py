class BrowserHistory:
    def __init__(self):
        self.stack=[]
    def details(self):
        print("1 enter the website")
        print("2 Go back ")
        print("3 view  the current page")
        print("4 view visited pages history")
        print(" 5 exit")
    
    def push(self,url):
        # self.url=input("enter the url")
        self.stack.append(url)
        print("visited",url)
    def is_empty(self):
        return len(self.stack)==0 
    def pop(self):
        if self.is_empty():
            print("no pages ") 
        else:
            removed=self.stack.pop()
            print(removed)
    def peek(self):
        if self.is_empty():
            print("no  url")
        else:
            print(self.stack[-1])
    def show_history(self):
        if self.is_empty():
            print("No browsing history")
        else:
            print("Browsing History:")
            for page in self.stack:
                print(page)
    def disp(self):
        while True:
            print("========browser menu options========")
            self.details()
            ch=int(input("enter your choice"))
            if ch==1:
                url=input("enter the url")
                self.push(url)
            elif ch==2:
                self.pop()
            elif ch==3:
                self.peek()
            elif ch == 4:
                self.show_history()

            elif ch == 5:
                print("Exiting Browser History")
                break

            else:
                print("Invalid choice")
                
ob=BrowserHistory()
ob.disp()


        
    

