from fastapi.responses import JSONResponse
from pydantic import BaseModel

from company.db.schema import Language, Company, CompanyLanguage, TagLanguage


class CompanyDetailResponse(BaseModel):
    company_name: str
    tags: list[str]


async def company_info_displayer(
    company: Company, language: Language
) -> CompanyDetailResponse:
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
