from scheduling_helper_code.get_music_class import *
def test_get_music_class():
    results = get_music_class()
    assert results[0].get_subject() == 'MUS'
    assert results[0].get_code() == '3314'
    assert results[0].get_name() == "Instrumental Ensemble Music"