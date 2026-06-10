from pymongo.errors import ServerSelectionTimeoutError


def test_get_all_documents_returns_503_when_mongo_is_unavailable(
    client,
    mock_document_repo,
):
    mock_document_repo.find_all.side_effect = ServerSelectionTimeoutError(
        "timeout simulado"
    )

    response = client.get("/api/v1/documents")

    assert response.status_code == 503
    assert response.json()["detail"] == "Base de datos no disponible"
