from Status import Status

class Task:
    def __init__(self, name: str, description: str, status: Status, creation_date: str) -> None:
        self.__name          = name
        self.__description   = description
        self.__status        = status
        self.__creation_date = creation_date

    def __str__(self) -> str:
        return f"Task: {self.__name} | Description: {self.__description} | Status: {self.__status.value} | Date: {self.__creation_date}"

    def get_status(self):
        return self.__status

    def update_status(self, new_status: Status):
        self.__status = new_status

    def update(self, name=None, description=None, status=None):
        if name:
            self.__name = name
        if description:
            self.__description = description
        if status:
            self.__status = status
    
    #===Convert to JSON===
    def to_dict(self):
        return {
            "name"         : self.__name,
            "description"  : self.__description,
            "status"       : self.__status.value,
            "creation_date": self.__creation_date
        }

    @staticmethod
    def from_dict(data):
        return Task(
            name=data["name"],
            description=data["description"],
            status=Status(data["status"]),
            creation_date=data["creation_date"]
        )
