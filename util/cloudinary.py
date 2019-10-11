import cloudinary
import cloudinary.api
from util.config import CLOUD_NAME, API_KEY, API_SECRET

cloudinary.config(
	cloud_name = CLOUD_NAME,
	api_key = API_KEY,
	api_secret = API_SECRET
)

catagory = {
	'飛龍種': '雄火龍/蒼火龍/金火龍\n雌火龍/櫻火龍/銀火龍\n角龍/黑角龍\n風漂龍/霜翼風漂龍\n浮空龍/浮眠龍\n爆鱗龍/紅蓮爆鱗龍\n冰牙龍\n轟龍/黑轟龍\n迅龍',
	'牙龍種': '大凶豺龍\n大凶顎龍\n岩賊龍\n飛雷龍/痺毒龍\n慘爪龍/兇爪龍\n雷狼龍',
	'鳥龍種': '搔鳥\n眩鳥\n毒妖鳥/水妖鳥\n黑狼鳥/戰痕黑狼鳥',
	'獸龍種': '土砂龍\n爆鎚龍/骨鎚龍\n蠻顎龍/雷顎龍\n恐暴龍/煌怒恐暴龍\n碎龍\n斬龍/硫斬龍\n猛牛龍',
	'牙獸種': '金獅子',
	'魚龍種': '泥魚龍\n熔岩龍\n冰魚龍',
	'古龍種': '麒麟\n鋼龍\n炎王龍\n炎妃龍\n屍套龍/霧瘴屍套龍\n滅盡龍/殲世滅盡龍\n熔山龍\n絢輝龍\n冰呪龍\n溟波龍\n天地煌啼龍\n貝希摩斯',
	'遺存種': '鹿首精/古代鹿首精'
}

monsters = {
	'角龍': 'mhw/DIABLOS',
	'黑角龍': 'mhw/BDIABLOS',
	'雄火龍': 'mhw/RATHALOS',
	'蒼火龍': 'mhw/ARATHALOS',
	'金火龍': 'mhw/RATHIAN_GOLD',
	'雌火龍': 'mhw/RATHIAN',
	'櫻火龍': 'mhw/PRATHIAN',
	'銀火龍': 'mhw/RATHALOS_SILVER',
	'風漂龍': 'mhw/LEGIANA',
	'霜翼風漂龍': 'mhw/LEGIANA_KING',
	'浮空龍': 'mhw/PAOLUMU',
	'浮眠龍': 'mhw/PAOLUMU_SLEEP',
	'爆鱗龍': 'mhw/BAZELGEUSE',
	'紅蓮爆鱗龍': 'mhw/BAZEL_G',
	'冰牙龍': 'mhw/BARIOTH',
	'轟龍': 'mhw/TIGREX',
	'黑轟龍': 'mhw/TEMP',
	'迅龍': 'mhw/NARGACUGA',
	'大凶豺龍': 'mhw/GJAGRAS',
	'大凶顎龍': 'mhw/GGIRROS',
	'岩賊龍': 'mhw/DODOGAMA',
	'飛雷龍': 'mhw/TKADACHI',
	'痺毒龍': 'mhw/TKADACHI_P',
	'慘爪龍': 'mhw/ODOGARON',
	'兇爪龍': 'mhw/ODOGARON_G',
	'雷狼龍': 'mhw/ZINOGRE',
	'搔鳥': 'mhw/KYK',
	'眩鳥': 'mhw/TTYK',
	'毒妖鳥': 'mhw/PUKEI',
	'水妖鳥': 'mhw/PUKEI_G',
	'黑狼鳥': 'mhw/GARUGA',
	'戰痕黑狼鳥': 'mhw/GARUGA_G',
	'土砂龍': 'mhw/BARROTH',
	'蠻顎龍': 'mhw/ANJANATH',
	'雷顎龍': 'mhw/ANJANATH_THUNDER',
	'暴錘龍': 'mhw/URAGAAN',
	'骨錘龍': 'mhw/RADOBAAN',
	'碎龍': 'mhw/BRACHYDIOS',
	'斬龍': 'mhw/GLAVENUS',
	'硫斬龍': 'mhw/GLAVENUS_G',
	'猛牛龍': 'mhw/BANABARO',
	'金獅子': 'mhw/RAJANG',
	'泥魚龍': 'mhw/JYURATODUS',
	'熔岩龍': 'mhw/LAASIOTH',
	'冰魚龍': 'mhw/BEOTODUS',
	'麒麟': 'mhw/KIRIN',
	'鋼龍': 'mhw/KDAORA',
	'炎王龍': 'mhw/TEOSTRA',
	'炎妃龍': 'mhw/LUNASTRA',
	'屍套龍': 'mhw/VAALHAZAK',
	'霧瘴屍套龍': 'mhw/VAALHAZAK_G',
	'滅盡龍': 'mhw/NERGIGANTE',
	'殲世滅盡龍': 'mhw/NERGIGANTE_G',
	'熔山龍': 'mhw/ZMAGDAROS',
	'冥燈龍': 'mhw/XENOJIIVA',
	'恐暴龍': 'mhw/DEVILJHO',
	'煌怒恐暴龍': 'mhw/DEVILJHO_G',
	'絢輝龍': 'mhw/KULVETAROTH',
	'冰呪龍': 'mhw/VELKHANA',
	'冰咒龍': 'mhw/VELKHANA',
	'溟波龍': 'mhw/NAMIELLE',
	'天地煌啼龍': 'mhw/SHARAs',
	'貝希摩斯': 'mhw/BEHEMOTH',
	'鹿首精': 'mhw/LESHY',
	'古代鹿首精': 'mhw/KERNUN'
}