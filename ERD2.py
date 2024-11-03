#Version 2 of ERD generator
#By DrMaxD
#This version has the user enter their data directley into the code itself to build the ERD
import graphviz
tables = {
#Creates the table. Format is Name of Attribute; Space; then either (PK) if it's a primary key or (FK) if it's a foriegn key
    "Table1": {
        "attributes": [
            "Attribute1 (PK)",
            "Attribute2",
            "Attribute3 (FK)"
        ]
    },
    "Table2": {
        "attributes": [
            "Attribute1 (PK)",
            "Attribute2",
            "Attribute3 (FK)"
        ]
    },
    "Table3": {
        "attributes": [
            "Attribute1 (PK)",
            "Attribute2",
            "Attribute3 (FK)"
        ]
    }
}

relationships = [
#Establishes relationships. Format is first table; comma space; second table; comma space; then type of relationship
    ("Table1", "Table2", "One-to-Many"),
    ("Table1", "Table3", "One-to-Many"),
    ("Table2", "Table3", "One-to-Many"),
]

def create_er_diagram(tables, relationships):
    graph = graphviz.Digraph('ERD')
    
    for table, data in tables.items():
        attrs = data['attributes']
        graph.node(table, shape='box', label=f"{table}\n" + "\n".join(attrs))

    for rel in relationships:
        table1, table2, relation_type = rel
        graph.edge(table1, table2, label=relation_type)

    graph.render('er_diagram', format='png', cleanup=True)
    print("ER Diagram generated: er_diagram.png")

def main():
    create_er_diagram(tables, relationships)

if __name__ == "__main__":
    print("Made By: DrMaxD")
    main()
