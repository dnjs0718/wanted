from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from company.db.schema import CompanyLanguage, TagLanguage, Company


router = APIRouter()


class CompanyDetailResponse(BaseModel):
    company_name: str
    tags: list[str]


@router.get("", response_model=CompanyDetailResponse, summary="회사 이름으로 회사 검색")
async def company_detail(request: Request, company_name: str):
    """
    # Author
    - 원재연

    # Description
    - 회사 이름으로 회사 검색

    # Request Header
    - x-wanted-language : str = 원하는 언어

    # Request Query Parameter
    - company_name : str = 회사명

    # Response
    ```
    {
        "company_name": str = 회사명,
        "tags": list(str) = 태그 리스트
    }
    ```

    # Error
    - 401 : 사용 언어를 헤더에 담지 않았을 때
    - 404 : 사용 언어를 지원하지 않을 때 (language not found)
    - 404 : 회사를 찾을 수 없을 때 (company not found)
    - 404 : 회사가 해당언어를 지원하지 않을 때 (company_language not found)
    """
    language = request.state.language

    if not (
        company := await Company.get_or_none(
            company_languages__name=company_name
        ).prefetch_related("company_languages")
    ):
        return JSONResponse(status_code=404, content={"detail": "company not found"})

    if not (
        company_language := await CompanyLanguage.get_or_none(
            company=company, language=language
        )
    ):
        return JSONResponse(
            status_code=404, content={"detail": "company_language not found"}
        )

    tags = (
        await TagLanguage.filter(tag__company_tags__company=company, language=language)
        .prefetch_related("tag__company_tags__company")
        .values_list("name", flat=True)
    )

    return CompanyDetailResponse(company_name=company_language.name, tags=tags)
