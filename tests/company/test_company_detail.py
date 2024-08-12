from anyio.abc import BlockingPortal

from company.db.schema import (
    Company,
    CompanyLanguage,
    Language,
    Tag,
    CompanyTag,
    TagLanguage,
)


def test_create_db(portal: BlockingPortal):
    async def create_test_suite():
        await Company.create(id=1, name="원티드랩")

        await Language.bulk_create(
            [
                Language(id=1, full_name="korean", short_name="ko"),
                Language(id=2, full_name="english", short_name="en"),
                Language(id=3, full_name="chinese", short_name="cn"),
            ]
        )
        await CompanyLanguage.bulk_create(
            [
                CompanyLanguage(company_id=1, language_id=1, name="원티드랩"),
                CompanyLanguage(company_id=1, language_id=2, name="Wantedlab"),
            ]
        )
        await Tag.bulk_create(
            [
                Tag(id=1, name="재택근무"),
                Tag(id=2, name="인원 급성장"),
            ]
        )

        await TagLanguage.bulk_create(
            [
                TagLanguage(tag_id=1, language_id=1, name="재택근무"),
                TagLanguage(tag_id=1, language_id=2, name="remote work"),
                TagLanguage(tag_id=2, language_id=1, name="인원 급성장"),
                TagLanguage(tag_id=2, language_id=2, name="rapid company growth"),
            ]
        )

        await CompanyTag.bulk_create(
            [
                CompanyTag(company_id=1, tag_id=1),
                CompanyTag(company_id=1, tag_id=2),
            ]
        )

    portal.call(create_test_suite)


def test_company_detail_success(client):
    """
    2. 회사 이름으로 회사 검색
    header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
    """
    resp = client.get("/companies/Wantedlab", headers={"x-wanted-language": "ko"})

    assert resp.status_code == 200
    assert resp.json() == {
        "company_name": "원티드랩",
        "tags": ["재택근무", "인원 급성장"],
    }


def test_company_detail_header_not_contains_error(client):
    """
    2. 회사 이름으로 회사 검색
    헤더에 언어가 들어가지 않았을 때 에러가 발생합니다.
    """
    resp = client.get("/companies/Wantedlab")

    assert resp.status_code == 401
    assert resp.json()["detail"] == "language required"


def test_company_detail_language_not_found_error(client):
    """
    2. 회사 이름으로 회사 검색
    없는 언어로 검색을 시도했을 때 에러가 발생합니다.
    """
    resp = client.get("/companies/Wantedlab", headers={"x-wanted-language": "jp"})

    assert resp.status_code == 404
    assert resp.json()["detail"] == "language not found"


def test_company_detail_company_not_applied_language_error(client):
    """
    2. 회사 이름으로 회사 검색
    회사가 해당 언어를 지원하지 않을 때 에러가 발생합니다.
    """
    resp = client.get("/companies/Wantedlab", headers={"x-wanted-language": "cn"})

    assert resp.status_code == 404
    assert resp.json()["detail"] == "company_language not found"
