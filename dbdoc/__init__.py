from sqlalchemy import create_engine, inspect
class DbDoc(object):
    def_top_html = ""
    def_bottom_html = ""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db_uri = kwargs['db_uri']
        self.engine = create_engine(self.db_uri)
        self.inspector = inspect(self.engine)
        self.schema_name = self.inspector.default_schema_name
        self.tables = self.get_tables()
        self.content = []
    def write_content(self, content):
        self.content.append(content)
        print(content, file=self.doc_file)
    def get_tables(self):
        return self.inspector.get_table_names()
    def get_columns(self, table_name):
        return self.inspector.get_columns(table_name)
    def get_table_name(self, table):
        return table
    def get_table_comment(self, table):
        return self.inspector.get_table_comment(self.get_table_name(table))
    def get_column_name(self, column):
        return column['name']
    def get_column_type(self, column):
        return column['type']
    def get_column_comment(self, column):
        return column['comment']
    def build_top(self):
        return ""
    def build_menus(self):
        menus_html = []
        menus_html.append("<dl class='menus>")
        for t in self.tables:
            table_name = self.get_table_name(t)
            menus_html.append("<dt><a href='#%s'>%s</a></dt><dd>%s</dd>" % (table_name, table_name, self.get_table_comment(t)))
        menus_html.append("</dl>")
        return "".join(menus_html)
    def build_table(self, table):
        table_name = self.get_table_name(table)
        table_html = []
        table_html.append("<table id='%s'>" %(table_name))
        table_html.append("<caption>%s -> %s</caption>" % (table_name, self.get_table_comment(table)))
        table_html.append("<thead>")
        table_html.append("<tr><th colspan='3'>Columns</th></tr>")
        # TODO PK FK Default
        table_html.append("<tr><th>Name</th><th>Type</th><th>Comment</th></tr>")
        table_html.append("</thead>")
        table_html.append("<tbody>")
        for column in self.get_columns(table_name):
            table_html.append("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (self.get_column_name(column), self.get_column_type(column), self.get_column_comment(column)))
        table_html.append("</tbody>")
        table_html.append("</table>")
        return "".join(table_html)
    
    def build_body(self):
        body = []
        for t in self.tables:
            body.append(self.build_table(t))
        return "".join(body)
    def build_bottom(self):
        return ""

    def save_doc(self):
        self.write_content(self.def_top_html)
        self.write_content(self.build_top())
        self.write_content(self.bulid_menus())
        self.write_content(self.build_body())
        self.write_content(self.build_bottom())
        self.write_content(self.def_bottom_html)