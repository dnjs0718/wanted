from fastapi import APIRouter, Request
from pydantic import BaseModel

from company.db.schema import CompanyLanguage


class CompanySearchResponse(BaseModel):
    company_name: str


router = APIRouter()


@router.get("", response_model=list[CompanySearchResponse], summary="회사명 자동완성")
async def company_search(request: Request, query: str):
    """
    # Author
    - 원재연

    # Description
    - 회사명 자동완성

    # Request Header
    - x-wanted-language : str = 원하는 언어

    # Request Query Parameter
    - query : str = 회사명

    # Response
    ```
    [
        {
            "company_name" : str = 회사명
        }
    ]
    ```

    # Error
    - 401 : 사용 언어를 헤더에 담지 않았을 때
    - 404 : 사용 언어를 지원하지 않을 때
    """
    language = request.state.language
    return await CompanyLanguage.filter(
        language=language, name__icontains=query
    ).values(company_name="name")
