import json

def test_default_data_keys():
    with open('default_data.json', 'r') as f:
        data = json.load(f)

    assert 'version' in data, "Missing 'version' key"
    assert 'notes' in data, "Missing 'notes' key"
    assert isinstance(data['notes'], list), "'notes' should be a list"

    if len(data['notes']) > 0:
        for i, note in enumerate(data['notes']):
            assert 'id' in note, f"Note {i} is missing 'id'"
            assert 'text' in note, f"Note {i} is missing 'text'"
            assert 'visible' in note, f"Note {i} is missing 'visible'"
            assert 'x' in note, f"Note {i} is missing 'x'"
            assert 'y' in note, f"Note {i} is missing 'y'"
            assert 'width' in note, f"Note {i} is missing 'width'"
            assert 'height' in note, f"Note {i} is missing 'height'"

def test_default_data_is_valid():
    with open('default_data.json', 'r') as f:
        data = json.load(f)
    assert data is not None

if __name__ == '__main__':
    test_default_data_keys()
    test_default_data_is_valid()
    print("Unit tests passed!")
