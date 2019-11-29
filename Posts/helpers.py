def modify_input_for_multiple_files(property_id, image, type):
    dict = {}
    dict['post'] = property_id.pk
    dict['file'] = image
    dict['file_type'] = type
    return dict
