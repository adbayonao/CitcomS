import re

input_file = '500.mesh.10.gpml'  # This is repeated for each GPlates polygon
output_file = 'coordenadas_10.txt'

coord_pattern = re.compile(r'<gml:pos>([\d\.\-]+) ([\d\.\-]+)</gml:pos>')

with open(input_file, 'r') as file:
    data = file.read()
    coordenadas = coord_pattern.findall(data)

with open(output_file, 'w') as file:
    for lat, lon in coordenadas:
        file.write(f'{lat}\t{lon}\n')

