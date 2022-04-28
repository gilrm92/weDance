
router = APIRouter(prefix="/login", tags=["Login"], responses={404: {"description": "Not found"}})

@router.get("/login/")