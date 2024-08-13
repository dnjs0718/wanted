from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from tortoise.transactions import in_transaction

from company.db.schema import (
    CompanyLanguage,
    TagLanguage,
    Company,
    Language,
    Tag,
    CompanyTag,
)
from company.utils.displayer import company_info_displayer


router = APIRouter()


class CompanyDetailResponse(BaseModel):
    company_name: str
    tags: list[str]


@router.get(
    "/{company_name}",
    response_model=CompanyDetailResponse,
    summary="회사 이름으로 회사 검색",
)
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

    return await company_info_displayer(company=company, language=language)


class CompanyTagCreateRequest(BaseModel):
    tag_name: dict


class CompanyCreateRequest(BaseModel):
    company_name: dict
    tags: list[CompanyTagCreateRequest] | None


@router.post(
    "",
    response_model=CompanyDetailResponse,
    summary="회사 생성",
    status_code=201
)
async def company_builder(request: Request, body: CompanyCreateRequest):
    """
    # Author
    - 원재연

    # Description
    - 회사 생성

    # Request Header
    - x-wanted-language : str = 원하는 언어

    # Request Query Parameter
    ```
    {
        "company_name": dict = 각 나라의 언어는 key, alias 이름은 name (ex: {"ko" : "원티드랩"}),
        "tags": [
            {
            "tag_name": dict = 각 나라의 언어는 key, alias 이름은 name (ex: {"ko" : "재택근무"}),
            }
        ]
    }
    ```

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
    - 400 : 한국어가 Request에 담겨있지 않을 때 (한국어 필수) (korean must be exist)
    """
    async with in_transaction(connection_name="default"):
        if "ko" not in body.company_name.keys():
            return JSONResponse(
                status_code=400, content={"detail": "korean must be exist"}
            )
        company = await Company.create(name=body.company_name["ko"])

        company_language_list = []
        for language, company_name in body.company_name.items():
            language_obj, _ = await Language.update_or_create(name=language)
            company_language_list.append(
                CompanyLanguage(
                    language=language_obj, company=company, name=company_name
                )
            )

        await CompanyLanguage.bulk_create(company_language_list)

        for tag in body.tags:
            if "ko" not in tag.tag_name.keys():
                return JSONResponse(
                    status_code=400, content={"detail": "korean must be exist"}
                )
            tag_obj, _ = await Tag.update_or_create(name=tag.tag_name["ko"])
            await CompanyTag.create(company=company, tag=tag_obj)
            for language, tag_name in tag.tag_name.items():
                language_obj, _ = await Language.update_or_create(name=language)
                await TagLanguage.update_or_create(
                    tag=tag_obj, language=language_obj, name=tag_name
                )

        return await company_info_displayer(
            company=company, language=request.state.language
        )
