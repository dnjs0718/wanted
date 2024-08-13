from anyio.abc import BlockingPortal

from company.db.schema import Language

def test_create_db(portal: BlockingPortal):
    async def create_test_suite():
        await Language.bulk_create(
            [
                Language(id=1, name="ko"),
                Language(id=2, name="en"),
                Language(id=3, name="tw"),
            ]
        )

    portal.call(create_test_suite)


def test_new_company_create_success(client):
    """
    3.  새로운 회사 추가
    새로운 언어(tw)도 같이 추가 될 수 있습니다.
    저장 완료후 header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
    """
    resp = client.post(
        "/companies",
        json={
            "company_name": {
                "ko": "라인 프레쉬",
                "tw": "LINE FRESH",
                "en": "LINE FRESH",
            },
            "tags": [
                {
                    "tag_name": {
                        "ko": "태그_1",
                        "tw": "tag_1",
                        "en": "tag_1",
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_8",
                        "tw": "tag_8",
                        "en": "tag_8",
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_15",
                        "tw": "tag_15",
                        "en": "tag_15",
                    }
                }
            ]
        },
        headers={"x-wanted-language": "tw"},
    )

    assert resp.json() == {
        "company_name": "LINE FRESH",
        "tags": [
            "tag_1",
            "tag_8",
            "tag_15",
        ],
    }
    

def test_new_company_create_error_because_of_the_header(client):
    """
    3.  새로운 회사 추가
    헤더에 언어가 들어가지 않았을 때 에러가 발생합니다.
    """
    resp = client.post(
        "/companies",
        json={
            "company_name": {
                "ko": "라인 프레쉬",
                "tw": "LINE FRESH",
                "en": "LINE FRESH",
            },
            "tags": [
                {
                    "tag_name": {
                        "ko": "태그_1",
                        "tw": "tag_1",
                        "en": "tag_1",
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_8",
                        "tw": "tag_8",
                        "en": "tag_8",
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_15",
                        "tw": "tag_15",
                        "en": "tag_15",
                    }
                }
            ]
        },
    )
    
    assert resp.status_code == 401
    assert resp.json()["detail"] == "language required"


def test_new_company_create_language_not_found(client):
    """
    3.  새로운 회사 추가
    없는 언어로 검색을 시도했을 때 에러가 발생합니다.
    """
    resp = client.post(
        "/companies",
        json={
            "company_name": {
                "ko": "라인 프레쉬",
                "tw": "LINE FRESH",
                "en": "LINE FRESH",
            },
            "tags": [
                {
                    "tag_name": {
                        "ko": "태그_1",
                        "tw": "tag_1",
                        "en": "tag_1",
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_8",
                        "tw": "tag_8",
                        "en": "tag_8",
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_15",
                        "tw": "tag_15",
                        "en": "tag_15",
                    }
                }
            ]
        },
        headers={"x-wanted-language": "jp"},
    )
    
    assert resp.status_code == 404
    assert resp.json()["detail"] == "language not found"
    

def test_new_company_create_korean_not_found(client):
    """
    3.  새로운 회사 추가
    한국어가 Request에 담겨있지 않을 때 에러가 발생합니다.
    """
    resp = client.post(
        "/companies",
        json={
            "company_name": {
                "tw": "LINE FRESH",
                "en": "LINE FRESH",
            },
            "tags": [
                {
                    "tag_name": {
                        "tw": "tag_1",
                        "en": "tag_1",
                    }
                },
                {
                    "tag_name": {
                        "tw": "tag_8",
                        "en": "tag_8",
                    }
                },
                {
                    "tag_name": {
                        "tw": "tag_15",
                        "en": "tag_15",
                    }
                }
            ]
        },
        headers={"x-wanted-language": "tw"},
    )

    assert resp.status_code == 400
    assert resp.json()['detail'] == 'korean must be exist'
    

def test_new_company_create_method_error(client):
    """
    3.  새로운 회사 추가
    새로운 언어(tw)도 같이 추가 될 수 있습니다.
    저장 완료후 header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
    """
    resp = client.patch(
        "/companies",
        json={
            "company_name": {
                "ko": "라인 프레쉬",
                "tw": "LINE FRESH",
                "en": "LINE FRESH",
            },
            "tags": [
                {
                    "tag_name": {
                        "ko": "태그_1",
                        "tw": "tag_1",
                        "en": "tag_1",
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_8",
                        "tw": "tag_8",
                        "en": "tag_8",
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_15",
                        "tw": "tag_15",
                        "en": "tag_15",
                    }
                }
            ]
        },
        headers={"x-wanted-language": "tw"},
    )

    assert resp.status_code == 405