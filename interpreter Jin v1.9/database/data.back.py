# except Exception as e:
#    print(e)
for a_class in new_module.all_my_classbuilders:
    print("first loop")
    format_str = """
INSERT INTO class (class_id, class_name) 
VALUES (NULL, "{first}");
            """
    sql_command = format_str.format(first=a_class.name)
    c.execute(sql_command)

    cls_id = c.execute(f"SELECT class_id FROM {a_class.name}")

    for an_a in a_class.all_my_attributes:
        format_str = """
INSERT INTO attribute (attribute_id, attribute_name, attribute_type, class_id) 
VALUES (NULL, "{first}", {second}, {third});
                """
        sql_command = format_str.format(first=an_a.name,
                                        second=an_a.type,
                                        third=cls_id)
        c.execute(sql_command)

    for an_m in a_class.all_my_methods:
        format_str = """
INSERT INTO attribute (method_id, method_name, method_input, method_type, class_id) 
VALUES (NULL, "{first}", {second}, {third}, {fourth});
                """
        sql_command = format_str.format(first=an_m.name,
                                        second=an_m.input,
                                        third=an_m.return_type,
                                        fourth=cls_id)

        c.execute(sql_command)