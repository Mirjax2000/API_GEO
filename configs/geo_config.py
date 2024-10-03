# region MAPY.CZ
mapy_cz: dict = {
    "url": "https://api.mapy.cz/v1/maptiles/basic/256/",
    "zoom": "{z}",
    "x": "{x}",
    "y": "{y}",
    "lang": "cs",
    "api_key": "tS3213LT9X_tLBWD3vmiynClzyn32dpj5etTL1BaT54",
    "max_zoom": 18,
}

mapy_cz_server = (
    f"{mapy_cz["url"]}{mapy_cz["zoom"]}/{mapy_cz['x']}/{mapy_cz['y']}?lang={mapy_cz['lang']}&apikey={mapy_cz['api_key']}"
)
# endregion
