import re
import json


def generate_dict(open_file: str)->dict:
    '''Function to parse a trajectory file and output a dictionary'''
    p = open(open_file, "r").read() + "ITEM"
    all_timestamps = re.findall("ITEM:\sATOMS.*?\n(.*?)ITEM", p, re.DOTALL)
    all_timestep = re.findall("ITEM: TIMESTEP.*?\n(\d+)\n", p, re.DOTALL)
    natoms = int(re.search("NUMBER\sOF\sATOMS.*?\n(\d+)", p, re.DOTALL)[1])
    dimensions = [
        int(i)
        for i in re.search("BOX\sBOUNDS.*?\n(\d+\s\d+).*?\n", p, re.DOTALL)[1].split()
    ]
    info_dict = {}
    for j, line in enumerate(all_timestamps):
        h = line.split("\n")
        dicts = {}
        for i in h:
            if len(i) == 0:
                pass
            else:
                nums = i.split()
                molecule_id = int(nums[2])
                atom_id = int(nums[0])
                if molecule_id in dicts.keys():
                    dicts[molecule_id][atom_id] = {
                        "x": int(nums[3]),
                        "y": int(nums[4]),
                        "z": int(nums[5]),
                    }
                else:
                    dicts[molecule_id] = {}
                    dicts[molecule_id][atom_id] = {
                        "x": int(nums[3]),
                        "y": int(nums[4]),
                        "z": int(nums[5]),
                    }
        info_dict[j] = dicts

    list_keys = list(info_dict.keys())
    mymap = {list_keys[i]: int(all_timestep[i]) for i in range(len(all_timestep))}

    info_dict = {mymap[i]: info_dict[i] for i in info_dict.keys()}

    # Atom type to id Mapping:

    atom_id_map = {}
    for j in all_timestamps[0].split("\n"):
        info = j.split()
        if len(info) == 0:
            continue
        uid = int(info[0])
        idtype = int(info[1])
        atom_id_map[uid] = idtype

    outdict = {
        "id_to_atom-type": atom_id_map,
        "structured-data": info_dict,
        "dimensions": dimensions,
        "natoms": natoms,
    }

    return outdict

def save_parsed_dict(open_file:str,save_as:str):
    f = generate_dict(open_file)
    with open(f"{save_as}.json", "w") as file:
        json.dump(f, file)
    return