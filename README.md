# LASSI Analysis

Python files to parse and analyze trajectories from the LASSI simulation engine

## Contents:

parseToFile.py parses .lammpstrj trajectory file and outputs a dictionary

## json schema:

dictionary output from parseToFile.py has 4 keys `"id_to_atom-type"`, `"dimensions"`, `"natoms"`, and `"structured-data"`<br><br>
output from function = <b>outdict

<b>outdict["id_to_atom-type"]</b> itself is a dictionary with keys corresponding to the unique id assigned to each atom, and the value of each key corresponds to the type of atom that particular key is assigned<br><br><br>

<b>outdict["structured-data"]</b> is itself too a dictionary, however containing much nested information. The keys of the dictionary outdict["structured-data"] are the individual `timesteps`, for example the first three keys are the integers `0, 25000000, and 50000000`. <br>
Keying into and of these individual timesteps returns another dictionary whose keys are unique `molecular identifiers` which range from `0-N`, where N is the number of chains. Each unique molecule dictionary will itself have a dictionary whose keys correspond to the individual atoms in that particular molecule and each molecular will contain `n atoms`. Each unique can then be accessed to obtain its `x, y, and z` coordinate by using the string 'x', string 'y' and string 'z' for that unique id to obtain the desired coordinates <br><br>
Structure of `"structured-data"` key:<br><br>
    outdict["structured-data"] =<br> 
 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
{<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;TIMESTEP(integer value): {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; MOLECULE_ID(integer value): {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;ATOM_ID: {<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"x":(integer value)<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"y":(integer value)<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"z":(integer value)<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}<br>
<br>

outdict["id_to_atom-type"] maps the id of the atom to the type.<br> e.g., atom id `0` is `2` would mean that id `0` is a particular site corresponding to bead 2 (e.g., a sticker).<br><br>
Structure of `"id_to_atom-type"` key:<br><br>
    outdict["id_to_atom-type"] = <br>
 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
{<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;ATOM_ID(integer value): ATOM_TYPE (integer value)<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}

outdict["natoms"] returns the number of atoms in the simulation box. The number is conserved during the simulation.<br><br>
Structure of `"natoms"` key:<br><br>
    outdict["natoms"] = NUMBER OF ATOMS (integer value)<br>

outdict["dimensions"] returns the xmin and xmax of the simulation box as a python list, where the first element corresponds to xmin and the second corresponds to xmax.<br>
NOTE: The box is cubic and the size stays the same during the simulation.<br><br>
Structure of `"dimensions"` key:<br><br>
    outdict["dimensions"] = LIST(XMIN, XMAX)
