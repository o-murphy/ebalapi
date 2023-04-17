from .bullet import BulletCRUDView, BulletView
from .bullet import BulletView, BulletCRUDView
from .caliber import CaliberCRUDView, CaliberView, CaliberDetailView
from .catridge import CartridgeView, CartridgeCRUDView
from .diameter import DiameterView, DiameterCRUDView
from .drag_function import DragFunctionView, DragFunctionCRUDView
from .rifle import RifleCRUDView, RifleView
from .token_auth import AuthView, CustomAuthToken
from .vendor import VendorView, VendorCRUDView

# search views here
from .bullet_search import BulletSearchListView
from .cartridge_search import CartridgeSearchListView
