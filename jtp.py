import argparse
import json

class JavaClass:
    def __init__(self, class_name, use_getter_setter):
        """
         Initializes the class. This is called by __init__ and should not be called directly.
         The class is initialized with the name of the class to be instantiated and the use_getter_setter flag to determine whether or not to use the getter or setter for the field.
         
         @param class_name - The name of the class to be instantiated
         @param use_getter_setter - True if getter and setter methods should be generated
        """
        self.class_name = class_name
        self.fields = []
        self.nested_classes = []
        self.use_getter_setter = use_getter_setter

    def add_field(self, field_name, field_type):
        """
         Adds a field to the java class.
         
         @param field_name - The name of the field to add.
         @param field_type - The type of the field to add
        """
        self.fields.append((field_name, field_type))

    def add_nested_class(self, nested_class):
        """
         Add a nested class to the java class.
         
         @param nested_class - The name of the nested class to
        """
        self.nested_classes.append(nested_class)

    def to_java_string(self):
        """
         Returns a string representation of the class. This is used to generate code that can be compiled by javac.
         
         
         @return The Java code that will be used to compile the class and its nested classes to Java code.
        """
        lines = []
        lines.append(f'public class {self.class_name} {{')
        # Add a private or public field to the output.
        for field_name, field_type in self.fields:
            # Appends the private or public field declaration.
            if self.use_getter_setter:
                lines.append(f'\tprivate {field_type} {field_name};')
            else:
                lines.append(f'\tpublic {field_type} {field_name};')
        lines.append('')
        if self.use_getter_setter:
            # Generate getter setter for each field.
            for field_name, field_type in self.fields:
                lines.extend(self._generate_getter_setter(field_name, field_type))
        lines.append('}\n')
        for nested_class in self.nested_classes:
            lines.append(nested_class.to_java_string())
            lines.append('')
        return '\n'.join(lines)

    def _generate_getter_setter(self, field_name, field_type):
        """
         Generates getter and setter for field. This method is used to generate getter and setter for fields in the java class.
         
         @param field_name - Name of the field.
         @param field_type - Type of the field.
         
         @return List of lines that make up the getter and setter for the fields. Each line is a line of code
        """
        lines = []
        method_name = field_name.capitalize()
        lines.append(f'\tpublic {field_type} get{method_name}() {{')
        lines.append(f'\t\treturn {field_name};')
        lines.append('\t}')
        lines.append('')
        lines.append(f'\tpublic void set{method_name}({field_type} {field_name}) {{')
        lines.append(f'\t\tthis.{field_name} = {field_name};')
        lines.append('\t}')
        lines.append('')
        return lines

def convert_json_to_pojo(data, class_name, use_getter_setter):
    """
     Convert JSON data to POJO. This is a recursive function that will convert a JSON data structure ( dict list or tuple ) into a POJO.
     
     @param data - The JSON data to convert. Can be a list of dictionaries or a dictionary of dictionaries.
     @param class_name - The name of the POJO class.
     @param use_getter_setter - Whether to use getter setter or not.
     
     @return A POJO representing the JSON data and its nested classes as well as the set of field names that have been used
    """
    java_class = JavaClass(class_name, use_getter_setter)
    field_names = set()
    # This method is used to convert JSON data to POJO.
    if isinstance(data, dict):
        # Add field names to the java class.
        for key, value in data.items():
            field_type = get_java_type(value, key)
            # Add a field to the class.
            if key not in field_names:
                field_names.add(key)
                java_class.add_field(key, field_type)
            # Add a field to the java class.
            if isinstance(value, dict):
                nested_class_name = key.capitalize()
                nested_java_class = convert_json_to_pojo(value, nested_class_name, use_getter_setter)
                java_class.add_nested_class(nested_java_class)
                # Add a field to the class.
                if key not in field_names:
                    field_names.add(key)
                    java_class.add_field(key, nested_class_name)
            elif isinstance(value, list):
                # Add a field to the java class.
                if all(isinstance(item, dict) for item in value):
                    element_class_name = key.capitalize() + "Element"
                    element_java_class = convert_json_to_pojo(value[0], element_class_name, use_getter_setter)
                    java_class.add_nested_class(element_java_class)
                    # Add a field to the list of field names.
                    if key not in field_names:
                        field_names.add(key)
                        java_class.add_field(key, f'List<{element_class_name}>')
                else:
                    list_type = get_java_type(value[0], key) if value else "Object"
                    # Add a field to the list.
                    if key not in field_names:
                        field_names.add(key)
                        java_class.add_field(key, f'List<{list_type}>')
    return java_class

def get_java_type(value, field_name):
    """
     Returns a string representation of the Java type. This is used to print the type of a JSON object.
     
     @param value - The value to convert to a string
     @param field_name - The name of the field that is being converted
     
     @return A string representation of the Java type ( boolean int float str etc. ) for the given value and
    """
    # Returns a string representation of the value.
    if isinstance(value, bool):
        return 'boolean'
    elif isinstance(value, int):
        return 'int'
    elif isinstance(value, float):
        return 'double'
    elif isinstance(value, str):
        return 'String'
    elif isinstance(value, list):
        # List of elements or objects.
        if field_name == "segments" and all(isinstance(item, dict) for item in value):
            return f'List<{field_name.capitalize()[:-1]}Element>'
        else:
            list_type = get_java_type(value[0], field_name) if value else "Object"
            return f'List<{list_type}>'
    elif isinstance(value, dict):
        return field_name.capitalize()
    else:
        return value.__class__.__name__

def main():
    """
     Main function for json-to-pojo command line tool. Parses arguments and calls convert_json_to_pojo
    """
    parser = argparse.ArgumentParser(
        prog='json-to-pojo',
        description='A python parser which takes json and converts it to a Plain Old Java Object'
    )
    parser.add_argument('in_file', help='The input json file which should be converted to a POJO')
    parser.add_argument('out_file', help='The out java POJO file')
    parser.add_argument('--getter-setter', action='store_true', help='Generate getter and setter methods')
    args = parser.parse_args()

    with open(args.in_file, 'r') as json_file:
        json_data = json.load(json_file)

    class_name = 'MainClass'
    use_getter_setter = args.getter_setter
    java_class = convert_json_to_pojo(json_data, class_name, use_getter_setter)
    java_code = java_class.to_java_string()

    with open(args.out_file, 'w') as java_file:
        java_file.write(java_code)

    print(f"Java POJO has been successfully generated to '{args.out_file}'.")

# main function for the main module
if __name__ == "__main__":
    main()