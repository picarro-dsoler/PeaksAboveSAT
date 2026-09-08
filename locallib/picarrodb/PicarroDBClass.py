import copy
class DBTable:
    def __init__(self, name, columns=None):
        self.name = name
        # Ensure each instance gets its own columns list
        self.columns = columns if columns is not None else []
        self.acronym = ''.join([char for char in name if char.isupper()])
        for column in self.columns:
            column.parent_table = self  # Set parent reference
            setattr(self, column.name, column)

    def get_table_name(self):
        return self.name

    def get_acronym(self):
        return self.acronym

    def get_table_alias(self):
        return self.alias

    def create_table(self, arguments = None):
        pass
    

    def get_columns(self, format = 'query'):
        if format == 'query':
            query = [f'{self.acronym}.{column.get_column_name()}.STAsText() as {column.get_column_alias()}' if column.datatype == 'geometry' else f'{self.acronym}.{column.get_column_name()} as {column.get_column_alias()}' for column in self.columns]
            query = ' , '.join(query)
            return query
        elif format == 'list':
            list = [f'{column.get_column_name()}' for column in self.columns]
            return list
        else:
            raise ValueError(f'Invalid format: {format}')
    
    def add_column(self, column):
        self.columns.append(column)
        setattr(self, column.name, column)

    def __repr__(self):
        return f'{self.name}'

    def set_column_alias(self, column_name, alias):
        for col in self.columns:
            if col.name == column_name:
                col.set_column_alias(alias)
                break
        else:
            raise ValueError(f'Column {column_name} not found in table {self.name}')

    def delete_column(self, column_name):
        for col in self.columns:    
            if col.name == column_name:
                self.columns.remove(col)
                delattr(self, col.name)
                break
        else:
            raise ValueError(f'Column {column_name} not found in table {self.name}')

    
    def copy(self):
        return DBTable(self.name, self.columns.copy())
class DBColumn:
    def __init__(self, name, datatype = None, key = None):
        self.name = name
        self.datatype = datatype
        self.alias = name
        self.key = key
        if key is not None:
            if key not in ['primary', 'foreign']:
                raise ValueError(f'Invalid key: {key}')
    def get_column_name(self):
        return self.name
    
    def set_column_alias(self, alias):
        self.alias = alias

    def get_column_alias(self):
        return self.alias
    
    def __repr__(self):
        return f'{self.name}'

class DBConstructor:
    def __init__(self):
        self.tables = []
        self.columns = []

    def add_table(self, table):
        self.tables.append(table)

    def add_column(self, column):
        self.columns.append(column)

    def get_tables(self):
        return self.tables

class Condition:
    def __init__(self, column, operator, value):
        """Create a condition for WHERE clauses."""
        if not isinstance(column, DBColumn):
            raise TypeError("Column must be a DBColumn object")
        self.column = column
        self.operator = operator
        self.value = value
    
    def __str__(self):
        # If value is a SQLQuery object, wrap it in parentheses
        if isinstance(self.value, SQLQuery):
            return f"{self.column.get_column_name()} {self.operator} ({self.value})"
        # If value is a string that looks like a SQL query (contains SELECT), wrap it in parentheses
        elif isinstance(self.value, str) and 'SELECT' in self.value.upper():
            return f"{self.column.get_column_name()} {self.operator} ({self.value})"
        else:
            return f"{self.column.get_column_name()} {self.operator} {self.value}"
    
    def __repr__(self):
        return f"Condition({self.column.get_column_name()}, {self.operator}, {self.value})"

class SQLQuery:
    def __init__(self):
        self.select_fields = []
        self.from_table = None
        self.into_table = None
        self.join_clauses = []
        self.where_conditions = []
        self.group_by_fields = []
        self.order_by_fields = []
        self.limit_count = None
    
    def SELECT(self, fields=None):
        """Set the fields to select. Must be a list of DBColumn objects. If None, selects all (*)."""
        if fields is None:
            self.select_fields = None
        elif isinstance(fields, DBColumn):
            self.select_fields = [fields]
        elif isinstance(fields, list) and all(isinstance(field, DBColumn) for field in fields):
            self.select_fields = fields
        else:
            raise TypeError("Fields must be DBColumn objects or a list of DBColumn objects")
        return self
        
    def FROM(self, table, alias=None):
        """Set the table to query from. Must be a DBTable object or string."""
        if isinstance(table, DBTable):
            table_name = table.get_table_name()
            if alias:
                self.from_table = f"{table_name} {alias}"
            else:
                # Use the table's acronym as the default alias
                table_alias = table.get_acronym()
                self.from_table = f"{table_name} {table_alias}"
        elif isinstance(table, str):
            if alias:
                self.from_table = f"{table} {alias}"
            else:
                self.from_table = table
        else:
            raise TypeError("Table must be a string or DBTable object")
        return self
    
    def INTO(self, table):
        """Set the table to insert into. Table name must be a string."""
        if not isinstance(table, str):
            raise TypeError("Table name must be a string")
        self.into_table = table
        return self
    
    def JOIN(self, table, on_condition, join_type="INNER"):
        """Add a JOIN clause. Table can be DBTable or string, on_condition should be a Condition object."""
        if isinstance(table, DBTable):
            table_name = table.get_table_name()
            # Use the table's acronym as the default alias
            table_alias = table.get_acronym()
            table_name = f"{table_name} {table_alias}"
        elif isinstance(table, str):
            table_name = table
        else:
            raise TypeError("Table must be a string or DBTable object")
        
        if not isinstance(on_condition, Condition):
            raise TypeError("ON condition must be a Condition object")
        
        if join_type.upper() not in ["INNER", "LEFT", "RIGHT", "FULL", "CROSS"]:
            raise ValueError("Join type must be one of: INNER, LEFT, RIGHT, FULL, CROSS")
        
        self.join_clauses.append(f"{join_type.upper()} JOIN {table_name} ON {on_condition.build_condition()}")
        return self
    
    def LEFT_JOIN(self, table, on_condition):
        """Add a LEFT JOIN clause."""
        return self.JOIN(table, on_condition, "LEFT")
    
    def RIGHT_JOIN(self, table, on_condition):
        """Add a RIGHT JOIN clause."""
        return self.JOIN(table, on_condition, "RIGHT")
    
    def INNER_JOIN(self, table, on_condition):
        """Add an INNER JOIN clause."""
        return self.JOIN(table, on_condition, "INNER")
    
    def WHERE(self, conditions):
        """Add WHERE conditions. Can be a Condition object or list of Condition objects."""
        if isinstance(conditions, Condition):
            self.where_conditions = [conditions]
        elif isinstance(conditions, list) and all(isinstance(cond, Condition) for cond in conditions):
            self.where_conditions = conditions
        else:
            raise TypeError("Conditions must be Condition objects or a list of Condition objects")
        return self
    
    def GROUP_BY(self, fields):
        """Add GROUP BY fields. Must be DBColumn objects or a list of DBColumn objects."""
        if isinstance(fields, DBColumn):
            self.group_by_fields = [fields]
        elif isinstance(fields, list) and all(isinstance(field, DBColumn) for field in fields):
            self.group_by_fields = fields
        else:
            raise TypeError("Fields must be DBColumn objects or a list of DBColumn objects")
        return self
    
    def ORDER_BY(self, fields):
        """Add ORDER BY fields. Must be DBColumn objects or a list of DBColumn objects."""
        if isinstance(fields, DBColumn):
            self.order_by_fields = [fields]
        elif isinstance(fields, list) and all(isinstance(field, DBColumn) for field in fields):
            self.order_by_fields = fields
        else:
            raise TypeError("Fields must be DBColumn objects or a list of DBColumn objects")
        return self
    
    def LIMIT(self, count):
        """Set the LIMIT count."""
        self.limit_count = count
        return self
    
    def build_query(self):
        """Build and return the SQL query string."""
        if not self.from_table:
            raise ValueError("FROM is required")
        
        if self.select_fields is None:
            select_clause = "*"
        elif not self.select_fields:
            raise ValueError("SELECT fields cannot be empty list")
        else:
            select_names = [field.get_full_column_name() for field in self.select_fields]
            select_clause = ', '.join(select_names)
        
        query = f"SELECT {select_clause}"
        
        if self.into_table:
            query += f" INTO {self.into_table}"
        
        if isinstance(self.from_table, DBTable):
            query += f" FROM {self.from_table.get_table_name()}"
        else:
            query += f" FROM {self.from_table}"
        
        if self.join_clauses:
            query += " " + " ".join(self.join_clauses)
        
        if self.where_conditions:
            condition_strings = [str(condition) for condition in self.where_conditions]
            query += f" WHERE {' AND '.join(condition_strings)}"
        
        if self.group_by_fields:
            group_names = [field.get_column_name() for field in self.group_by_fields]
            query += f" GROUP BY {', '.join(group_names)}"
        
        if self.order_by_fields:
            order_names = [field.get_column_name() for field in self.order_by_fields]
            query += f" ORDER BY {', '.join(order_names)}"
        
        if self.limit_count:
            query += f" LIMIT {self.limit_count}"
        
        return query
    
    def __str__(self):
        """Return the built SQL query when converting to string."""
        return self.build_query()
    
    def __repr__(self):
        """Return the built SQL query for representation."""
        return f"SQLQuery('{self.build_query()}')"