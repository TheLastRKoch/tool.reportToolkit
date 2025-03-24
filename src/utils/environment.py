from os import environ as env


@classmethod
def get_and_check_variables(variable_list):
    variable_dict = {}
    for variable_name in variable_list:
        if variable_content := env.get(variable_name) is None:
            raise ValueError(f"The env variable {variable_name} could not be empty")
        variable_list[variable_name] = variable_content
    return variable_dict
