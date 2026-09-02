from sqlite3 import Row as SQLiteRow

class Row(SQLiteRow):
    def fields(self):
        return tuple(self)
    def stringify_field(self,index=0) -> str:
        field = tuple(self)[index]
        return str(field)
