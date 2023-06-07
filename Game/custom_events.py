import variables as vb


def new_level(num_of_map_list):
    num_of_map_list_tepm = num_of_map_list + 1
    vb.list_of_maps[num_of_map_list] = vb.list_of_maps[num_of_map_list_tepm]
    return num_of_map_list_tepm
