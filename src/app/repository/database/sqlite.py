from sqlite3 import Row as SQLiteRow

class Row(SQLiteRow):

    @property                            # getter
    def column_values(self):
        return tuple(self)

    @property
    def column_keys(self):
        return self.keys()

    @property
    def column(self):
        full_column = {}
        for index, column_key in enumerate(self.column_keys):
            column_value = self.column_values[index]
            full_column[column_key] = column_value
        print(full_column)
        return full_column


    def stringify_field(self,index=0) -> str:
        field = self.column_values[index]
        return str(field)
