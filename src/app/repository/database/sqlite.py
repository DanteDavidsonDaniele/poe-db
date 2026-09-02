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
        full_column = []
        for index, column_key in enumerate(self.column_keys):
            column_value = self.column_values[index]
            full_column.append({column_key:column_value})
        print(full_column)
        return full_column
        # values = self.column_keys,self.column_values
        # final = []
        # print(values)
        # for index, value in enumerate(values):
        #     print(value)
        #     #final.append([value[0][index],value[1][index]])
        #     #print(final[index])
        # return final

    def stringify_field(self,index=0) -> str:
        field = self.column_values[index]
        return str(field)
