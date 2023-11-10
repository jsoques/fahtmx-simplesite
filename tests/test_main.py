
def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "A Simple Music Viewer" in response.text
