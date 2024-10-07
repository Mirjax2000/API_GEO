import configs.config as conf

# region VAR
header_btn_config: dict = {
    "height": 96,
    "fg_color": (conf.btn_light, conf.btn_dark),
    "text_color": ("black", "white"),
    "font": conf.small_font,
    "hover_color": (conf.light_color, conf.dark_color),
    "compound": "top",
}

# endregion

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

mapy_cz_server:str = (
    f"{mapy_cz["url"]}{mapy_cz["zoom"]}/{mapy_cz['x']}/{mapy_cz['y']}?lang={mapy_cz['lang']}&apikey={mapy_cz['api_key']}"
)
# endregion

# region Google: normal and satellite
#
google_normal:str = "https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga"
# --
google_sattelite: str= "https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga"

# endregion

# region OpenStreetMap
open_server:str = ("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")

# endregion

# region vrstvy map
vrstvy_map:dict[str,list]={
    "mapy_cz":["basic", "winter", "outdoor", "aerial"],
    "google":['normal','sattelite']
    }
# endregion
