def contabilizar(volume,garrafas):
    volume_total=0
    for garrafa in garrafas:
        volume_total+=garrafa[1]*garrafa[0]
    return volume_total//volume