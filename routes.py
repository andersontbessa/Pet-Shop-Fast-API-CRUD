from fastapi import APIRouter

from controllers import PetShopController as petshop

router = APIRouter()

router.include_router(petshop.router, prefix='/petshop')