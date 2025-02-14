from io import StringIO

import pytest

from app.notes_reader.notes_loader import MarkdownNotesLoader


@pytest.fixture(scope="session")
def folder_dir():
    return 42


@pytest.fixture(scope="session")
def note_docker():
    return """

    # Docker

    Multiline Content
    Multiline Content

    #docker#pytest #python
    """


@pytest.fixture(scope="session")
def file_md(note_docker: str):
    return StringIO(note_docker)


def tags_are_normalized_with_mixed_case_and_whitespace():
    tags = ["Python", "  pytest", "#Docker", "PYTHON", "  DOCKER"]

    nl = MarkdownNotesLoader('.', tags)

    assert nl.tags == {"#python", "#pytest", "#docker"}


def find_tags_in_empty_note():
    nl = MarkdownNotesLoader('.', [])
    found_tags = nl.find_tags("")
    assert found_tags == set()


def find_tags_in_note_with_no_tags():
    note = """
    This is a note without any tags.
    """
    nl = MarkdownNotesLoader('.', [])
    found_tags = nl.find_tags(note)
    assert found_tags == set()


def check_tags_with_no_matching_tags():
    nl = MarkdownNotesLoader('.', ["#pytest", "python"])
    assert not nl.check_tags({'#unit_tests', '#docker'})


def check_tags_with_partial_matching_tags():
    nl = MarkdownNotesLoader('.', ["#pytest", "python"])
    assert nl.check_tags({'#pytest', '#docker'})


def test_tags_are_normalized():
    tags = ["python", "#pytest", "#python", "Python", "  docker"]

    nl = MarkdownNotesLoader('.', tags)

    assert nl.tags == {"#python", "#pytest", "#docker"}


# TODO consider to add more test cases for tags func
def test_find_tags_in_multiline_note(note_docker: str):
    nl = MarkdownNotesLoader('.', [])  # name mangling (privet można tylko w tej klasie)
    found_tags = nl.find_tags(note_docker)
    assert found_tags == {"#docker", "#pytest", "#python"}


def test_check_tags_from_note_with_tags():
    nl = MarkdownNotesLoader('.', ["#pytest", "pytest"])
    assert nl.check_tags({'#pytest', '#docker'})


def test_check_tags_from_note_without_tags():
    nl = MarkdownNotesLoader('.', ['python', 'pytest'])
    assert not nl.check_tags({'#unit_tests', '#docker'})
