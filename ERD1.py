#Version 1 of ERD generator
#By DrMaxD
#This version has the user run the command and enter the information into the console to build the ER Diagram
import graphviz

def create_er_diagram(tables, relationships):
    graph = graphviz.Digraph(format='png')
    
    for table, attributes in tables.items():
        label = f"{table} | " + " | ".join(attributes)
        graph.node(table, label=label)

    for rel in relationships:
        graph.edge(rel[0], rel[1], label=rel[2])

    graph.render('er_diagram', format='png', cleanup=True)

def get_input_data():
    tables = {}
    #User first is asked to enter name of table. Only type done when you have finished making all tables
    print("Enter table data. Type 'done' when you are finished entering tables.")

    while True:
        table_name = input("Enter table name: ")
        if table_name.lower() == 'done':
            break
        
        attributes = []
        print(f"Enter attributes for {table_name}")
        
        while True:
            attribute = input("Enter attribute: ")
            if attribute.lower() == 'done':
                break
            attributes.append(attribute)

        tables[table_name] = attributes

    return tables

def get_relationships():
    relationships = []
    #User is asked to input the relationships. Only enter done when all relationships have been added
    print("\nEnter relationships between tables:")

    while True:
        relation = input("Enter relationship: ")
        if relation.lower() == 'done':
            break
        table1, table2, rel_type = relation.split(',')
        relationships.append((table1.strip(), table2.strip(), rel_type.strip()))

    return relationships

def main():
    tables = get_input_data()
    relationships = get_relationships()
    create_er_diagram(tables, relationships)

if __name__ == "__main__":
    print("DrMaxD")
    main()
