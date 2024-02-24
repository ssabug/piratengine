

class playlist():
    def __init__(self,id,title,parentListId,nextListId,lastEditTime,isExplicitlyExported):
        self.id=id;
        self.title=title;
        self.parentListId=parentListId;
        self.nextListId=nextListId;
        self.lastEditTime=lastEditTime;
        self.isExplicitlyExported=isExplicitlyExported;

