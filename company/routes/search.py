from fastapi import APIRouter, Request
from pydantic import BaseModel

from company.db.schema import CompanyLanguage


class CompanySearchResponse(BaseModel):
    company_name: str


router = APIRouter()


@router.get("", response_model=list[CompanySearchResponse], summary="회사명 자동완성")
async def company_search(request: Request, query: str):
    language = request.state.language
    return await CompanyLanguage.filter(
        language=language, name__icontains=query
    ).values(company_name="name")