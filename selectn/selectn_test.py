from selectn import selectn


def test_selectn():
    hash = {
        'info': {
            'name': {
                'full': 'ay'
            }
        }
    }

    full = selectn('info.name.full', hash)

    assert full == 'ay'


def test_selectn_return_none():
    hash = {
        'info': {
            'name': {
                'full': 'ay'
            }
        }
    }

    name = selectn('info.name', hash)
    short = selectn('info.name.short', hash)

    assert name == hash['info']['name']
    assert short is None


def test_selectn_empty_return_none():
    hash = {'info': True}

    short = selectn('info.name.short', hash)

    assert short is None
