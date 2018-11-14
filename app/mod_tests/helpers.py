import os

def get_node_file_path(subject_name, node_id):
    path = os.path.abspath(os.path.dirname(__file__)) + \
                           "/cpp/{}/{}.cpp".format(subject_name, node_id)
    return path
