from anyio.abc import BlockingPortal

from company.db.schema import Company, CompanyLanguage, Language


def test_create_db(portal: BlockingPortal):
    async def create_test_suite():
        await Company.bulk_create(
            [
                Company(id=1, name="원티드랩"),
                Company(id=2, name="원티드랩123"),
                Company(id=3, name="주식회사 링크드코리아"),
                Company(id=4, name="스피링크"),
            ]
        )

        await Language.bulk_create(
            [
                Language(id=1, name="ko"),
                Language(id=2, name="en"),
            ]
        )
        await CompanyLanguage.bulk_create(
            [
                CompanyLanguage(company_id=1, language_id=1, name="원티드랩"),
                CompanyLanguage(company_id=1, language_id=2, name="WantedLab"),
                CompanyLanguage(company_id=2, language_id=1, name="원티드랩123"),
                CompanyLanguage(company_id=2, language_id=2, name="WantedLab123"),
                CompanyLanguage(
                    company_id=3, language_id=1, name="주식회사 링크드코리아"
                ),
                CompanyLanguage(company_id=4, language_id=1, name="스피링크"),
            ]
        )

    portal.call(create_test_suite)


def test_company_name_autocomplete_success(client):
    """
    1. 회사명 자동완성
    회사명의 일부만 들어가도 검색이 되어야 합니다.
    header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
    """
    resp = client.get("/search?query=링크", headers={"x-wanted-language": "ko"})

    assert resp.status_code == 200
    assert resp.json() == [
        {"company_name": "주식회사 링크드코리아"},
        {"company_name": "스피링크"},
    ]

    resp = client.get("/search?query=원", headers={"x-wanted-language": "ko"})

    assert resp.status_code == 200
    assert resp.json() == [
        {"company_name": "원티드랩"},
        {"company_name": "원티드랩123"},
    ]

    resp = client.get("/search?query=wan", headers={"x-wanted-language": "en"})

    assert resp.status_code == 200
    assert resp.json() == [
        {"company_name": "WantedLab"},
        {"company_name": "WantedLab123"},
    ]


def test_company_name_autocomplete_header_not_contains_error(client):
    """
    1. 회사명 자동완성
    헤더에 언어가 들어가지 않았을 때 에러가 발생합니다.
    """
    resp = client.get("/search?query=링크")

    assert resp.status_code == 401
    assert resp.json()["detail"] == "language required"


def test_company_name_autocomplete_language_not_found_error(client):
    """
    1. 회사명 자동완성
    없는 언어로 검색을 시도했을 때 에러가 발생합니다.
    """
    resp = client.get("/search?query=링크", headers={"x-wanted-language": "jp"})

    assert resp.status_code == 404
    assert resp.json()["detail"] == "language not found"
